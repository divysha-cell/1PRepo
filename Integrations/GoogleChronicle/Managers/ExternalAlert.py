import json

from SiemplifyConnectorsDataModel import AlertInfo
from SiemplifyUtils import unix_now
from TIPCommon.filters import filter_old_alerts
from TIPCommon.smp_io import read_content, read_ids, write_content, write_ids

from consts import ALERT_TYPES, ALERT_TYPE_NAMES, UNIFIED_CONNECTOR_DEFAULT_MAX_LIMIT

from utils import (
    UNIX_FORMAT,
    convert_hours_to_milliseconds,
    get_filters_by_alert_type,
    get_formatted_date_from_timestamp,
    get_last_success_time,
    pass_filters,
    save_timestamp_by_timestamp_file,
)

IDS_FILE_NAME = "EXTERNAL_ids.json"
IDS_DB_KEY = "EXTERNAL_ids"
TIMESTAMP_FILE_NAME = "EXTERNAL_timestamp.stmp"
TIMESTAMP_DB_KEY = "EXTERNAL_timestamp"
TIMESTAMP_KEY = "timestamp_ms"
STORED_IDS_LIMIT = 1000


class ExternalAlert:
    def __init__(
        self, siemplify, manager, python_process_timeout, connector_starting_time
    ):
        self.siemplify = siemplify
        self.manager = manager
        self.python_process_timeout = python_process_timeout
        self.connector_starting_time = connector_starting_time
        self.alert_type = ALERT_TYPES.get("external")
        self.timestamp_key = TIMESTAMP_KEY
        self.page_token = ""
        self.page_start_time = None

    def read_ids(self) -> dict[str, int]:
        """
        Read ids and creation timestamps from ids file
        """
        cache_str = read_content(
            self.siemplify,
            file_name=IDS_FILE_NAME,
            db_key=IDS_DB_KEY,
            default_value_to_return="{}",
        )
        try:
            cached_data = json.loads(cache_str)
            if isinstance(cached_data, list):
                cached_data = {item: 0 for item in cached_data}
            self.siemplify.LOGGER.info(
                f"Successfully loaded {len(cached_data)} existing "
                f"{ALERT_TYPE_NAMES.get(ALERT_TYPES.get('external'))} ids"
            )
            return cached_data
        except Exception as e:
            self.siemplify.LOGGER.info(
                f"read_ids exception caught: {e}. Returning empty dict."
            )
            return {}

    def get_alerts(
        self,
        existing_ids,
        fetch_limit,
        hours_backwards,
        fallback_severity=None,
        padding_period=None,
    ):
        """
        Get alerts
        :param existing_ids: {list} list of existing ids
        :param fetch_limit: {int} limit for results
        :param hours_backwards: {int} amount of hours from where to fetch alerts
        :param fallback_severity: {str} fallback severity
        :param padding_period: {int} padding period for alerts in hours
        :return: {list} list of EXTERNAL objects
        """
        last_success_timestamp = get_last_success_time(
            siemplify=self.siemplify,
            offset_with_metric={"hours": hours_backwards},
            time_format=UNIX_FORMAT,
            timestamp_file_name=TIMESTAMP_FILE_NAME,
            timestamp_db_key=TIMESTAMP_DB_KEY,
        )

        if (
            padding_period
            and last_success_timestamp
            > unix_now() - convert_hours_to_milliseconds(padding_period)
        ):
            last_success_timestamp = unix_now() - convert_hours_to_milliseconds(
                padding_period
            )
            self.siemplify.LOGGER.info(
                f"Last success time is greater than {ALERT_TYPE_NAMES.get(ALERT_TYPES.get('external'))} "
                f"alerts padding period. Unix: {last_success_timestamp} will be used as "
                f"last success time"
            )

        alert_types, total_seconds = self.manager.list_alerts(
            limit=max(fetch_limit, UNIFIED_CONNECTOR_DEFAULT_MAX_LIMIT),
            start_time=get_formatted_date_from_timestamp(last_success_timestamp),
            fetch_user_alerts=True,
            fallback_severity=fallback_severity,
        )

        alerts = []
        for alert_type in alert_types:
            alerts.extend(alert_type.alert_infos)

        alerts = sorted(alerts, key=lambda alert: int(getattr(alert, TIMESTAMP_KEY)))
        ids_to_filter = (
            list(existing_ids.keys())
            if isinstance(existing_ids, dict)
            else existing_ids
        )
        filtered_alerts = filter_old_alerts(self.siemplify, alerts, ids_to_filter, "id")
        self.siemplify.LOGGER.info(
            f"Fetched {len(filtered_alerts)} {ALERT_TYPE_NAMES.get(ALERT_TYPES.get('external'))} "
            f"alerts"
        )
        return filtered_alerts

    def pass_filters(self, alert):
        filters = get_filters_by_alert_type(
            self.siemplify.LOGGER, self.siemplify.whitelist, ALERT_TYPES.get("external")
        )
        return pass_filters(self.siemplify.LOGGER, alert, filters)

    def _prune_ids_by_checkpoint(
        self, existing_ids: dict[str, int], active_checkpoint_ts: int
    ) -> dict[str, int]:
        """
        Prune stored IDs dictionary cache based on active checkpoint timestamp
        """
        pruned_ids = {
            k: v for k, v in existing_ids.items() if v >= active_checkpoint_ts
        }
        if len(pruned_ids) < len(existing_ids):
            self.siemplify.LOGGER.info(
                f"Pruned stored IDs cache from {len(existing_ids)} to {len(pruned_ids)} "
                f"based on active checkpoint timestamp >= {active_checkpoint_ts}."
            )
        return pruned_ids

    def write_ids(self, existing_ids: dict[str, int] | list[str]) -> None:
        """
        Write ids to ids file dynamically pruned by active checkpoint timestamp
        """
        # If we are in the middle of token pagination, we prune using the initial query start time
        # to protect against duplicates of slightly delayed alerts across page boundaries.
        # If we timed out or completed the session, we prune based on the last successfully processed alert timestamp in DB.
        if self.page_token:
            active_checkpoint_ts = self.page_start_time or 0
        else:
            try:
                active_checkpoint_ts = int(
                    read_content(
                        self.siemplify,
                        file_name=TIMESTAMP_FILE_NAME,
                        db_key=TIMESTAMP_DB_KEY,
                        default_value_to_return="0",
                    )
                )
            except Exception:
                active_checkpoint_ts = 0

        if isinstance(existing_ids, dict):
            pruned_ids = self._prune_ids_by_checkpoint(
                existing_ids, active_checkpoint_ts
            )
            write_content(
                self.siemplify,
                json.dumps(pruned_ids),
                file_name=IDS_FILE_NAME,
                db_key=IDS_DB_KEY,
            )
        else:
            self.siemplify.LOGGER.info(
                f"EXTERNAL existing ids is a {type(existing_ids)}. Falling back to standard SDK list write..."
            )
            write_ids(
                self.siemplify,
                existing_ids,
                ids_file_name=IDS_FILE_NAME,
                db_key=IDS_DB_KEY,
                default_value_to_set=[],
                stored_ids_limit=STORED_IDS_LIMIT,
            )

    def save_timestamp(self, alerts, fetched_alerts_count=0):
        """
        Save last timestamp for given alerts
        :param alerts: {list} list of EXTERNAL objects
        :param fetched_alerts_count: {int} total number of alerts that were fetched from API
        :return: {void}
        """
        save_timestamp_by_timestamp_file(
            self.siemplify,
            alerts,
            TIMESTAMP_KEY,
            timestamp_file_name=TIMESTAMP_FILE_NAME,
            timestamp_db_key=TIMESTAMP_DB_KEY,
            fetched_alerts_count=fetched_alerts_count,
        )

    @staticmethod
    def get_alert_info(alert, environment_common, device_product_field):
        """
        Get alert info
        :param alert: {EXTERNAL} EXTERNAL object
        :param environment_common: {EnvironmentHandle} environment common object for fetching the environment
        :param device_product_field: {str} key to use for device product extraction
        :return: {AlertInfo} AlertInfo object
        """
        return alert.as_unified_alert_info(
            AlertInfo(), environment_common, device_product_field
        )

from __future__ import annotations

import datetime
import json

from SiemplifyConnectorsDataModel import AlertInfo
from SiemplifyUtils import convert_string_to_datetime, unix_now
from TIPCommon.consts import NUM_OF_MILLI_IN_SEC
from TIPCommon.filters import filter_old_alerts
from TIPCommon.smp_io import read_content, read_ids, write_content, write_ids
from TIPCommon.smp_time import convert_string_to_timestamp

from consts import (
    ALERT_TYPES,
    ALERT_TYPE_NAMES,
    MAX_ALLOWED_INGESTION_DELAY_MINUTES,
    DEFAULT_PADDING_PERIOD,
)
from datamodels import Detection
from utils import (
    UNIX_FORMAT,
    get_filters_by_alert_type,
    get_formatted_date_from_timestamp,
    get_last_success_time,
    pass_filters,
)

IDS_FILE_NAME = "RULE_ids.json"
IDS_DB_KEY = "RULE_ids"
TIMESTAMP_FILE_NAME = "RULE_timestamp.stmp"
TIMESTAMP_DB_KEY = "RULE_timestamp"
NEXT_PAGE_KEY = "RULE_page_token"
BACKLOG_TIMESTAMP_FILE_NAME = "RULE_backlog_timestamp.stmp"
BACKLOG_TIMESTAMP_DB_KEY = "RULE_backlog_timestamp"
HISTORIC_DATA_FILE_NAME = "RULE_historic_data.stmp"
HISTORIC_DATA_DB_KEY = "RULE_historic_data"
RULE_PREVIOUS_TIMESTAMP_FILE_NAME = "RULE_previous_timestamp.stmp"
RULE_PREVIOUS_TIMESTAMP_DB_KEY = "RULE_previous_timestamp"
TIMESTAMP_KEY = "timestamp"
STORED_IDS_LIMIT = 1000
STORED_IDS_DICT_LIMIT = 2000
TIMEOUT_THRESHOLD = 0.8
TOTAL_FETCH_LIMIT = 1000


class RuleAlert:
    def __init__(
        self,
        siemplify,
        manager,
        python_process_timeout,
        connector_starting_time,
        fail_on_invalid: bool = False,
    ):
        self.siemplify = siemplify
        self.manager = manager
        self.python_process_timeout = python_process_timeout
        self.connector_starting_time = connector_starting_time
        self.fail_on_invalid = fail_on_invalid
        self.alert_type = ALERT_TYPES.get("rule")
        self.timestamp_key = TIMESTAMP_KEY
        self.page_token = None
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
                f"{ALERT_TYPE_NAMES.get(ALERT_TYPES.get('rule'))} ids"
            )
            return cached_data
        except Exception as e:
            self.siemplify.LOGGER.info(
                f"read_ids exception caught: {e}. Returning empty dict."
            )
            return {}

    def get_alerts(
        self,
        existing_ids: list[str],
        fetch_limit: int,
        hours_backwards: int,
        fallback_severity: str | None = None,
    ) -> list[Detection]:
        """Get alerts from Chronicle API.

        Args:
            existing_ids (list[str]): List of existing detection ids.
            fetch_limit: {int} limit for results
            hours_backwards: {int} amount of hours from where to fetch alerts
            fallback_severity: {str} fallback severity

        Returns:
            New continuation time, list of Detection objects
        """
        self.page_start_time = get_last_success_time(
            siemplify=self.siemplify,
            offset_with_metric={"hours": hours_backwards},
            time_format=UNIX_FORMAT,
            timestamp_file_name=TIMESTAMP_FILE_NAME,
            timestamp_db_key=TIMESTAMP_DB_KEY,
        )
        self.page_token = read_content(
            siemplify=self.siemplify,
            default_value_to_return="",
            file_name=NEXT_PAGE_KEY,
            db_key=NEXT_PAGE_KEY,
        )

        # 1. Check and initialize backlog boundary on first run after upgrade
        backlog_ts_val = read_content(
            siemplify=self.siemplify,
            default_value_to_return="0",
            file_name=BACKLOG_TIMESTAMP_FILE_NAME,
            db_key=BACKLOG_TIMESTAMP_DB_KEY,
        )
        is_first_run = backlog_ts_val == "0"

        if is_first_run:
            current_now = unix_now()
            self.siemplify.LOGGER.info(
                f"First run after upgrade detected. Initializing backlog_timestamp boundary to {current_now}."
            )
            write_content(
                self.siemplify,
                str(current_now),
                file_name=BACKLOG_TIMESTAMP_FILE_NAME,
                db_key=BACKLOG_TIMESTAMP_DB_KEY,
            )
            write_content(
                self.siemplify,
                "True",
                file_name=HISTORIC_DATA_FILE_NAME,
                db_key=HISTORIC_DATA_DB_KEY,
            )
            backlog_timestamp = current_now
            historic_data = True
        else:
            backlog_timestamp = int(backlog_ts_val)
            historic_data = (
                read_content(
                    siemplify=self.siemplify,
                    default_value_to_return="True",
                    file_name=HISTORIC_DATA_FILE_NAME,
                    db_key=HISTORIC_DATA_DB_KEY,
                )
                == "True"
            )

        previous_start_time_str = read_content(
            siemplify=self.siemplify,
            default_value_to_return="0",
            file_name=RULE_PREVIOUS_TIMESTAMP_FILE_NAME,
            db_key=RULE_PREVIOUS_TIMESTAMP_DB_KEY,
        )
        try:
            previous_start_time = int(previous_start_time_str)
        except ValueError:
            previous_start_time = 0

        page_token, page_start_time, alerts = (
            self.manager.stream_detection_alerts_in_connector(
                existing_ids=existing_ids,
                limit=fetch_limit,
                python_process_timeout=self.python_process_timeout,
                connector_starting_time=self.connector_starting_time,
                timeout_threshold=TIMEOUT_THRESHOLD,
                page_token=self.page_token,
                page_start_time=get_formatted_date_from_timestamp(self.page_start_time),
                fallback_severity=fallback_severity,
                total_fetch_limit=TOTAL_FETCH_LIMIT,
            )
        )

        for _alert in alerts:
            self.siemplify.LOGGER.info(
                f"Fetched detection {_alert.id} with timestamp {_alert.timestamp}."
            )

        # 2. Transition from backlog to real-time mode if caught up
        if historic_data and self.page_start_time >= backlog_timestamp:
            self.siemplify.LOGGER.info(
                f"Historical backlog fully processed. Query start time {self.page_start_time} "
                f">= backlog_timestamp {backlog_timestamp}. Transitioning to real-time mode."
            )
            write_content(
                self.siemplify,
                "False",
                file_name=HISTORIC_DATA_FILE_NAME,
                db_key=HISTORIC_DATA_DB_KEY,
            )
            historic_data = False

        # 3. Progression-Based Ingestion Warning Muting
        mute_warning = False
        if historic_data:
            if self.page_start_time == previous_start_time:
                # Cursor did not advance -> Stuck on backlog page -> Fire warning!
                self.siemplify.LOGGER.info(
                    "Cursor progress frozen during backlog catch-up. Slow ingestion warning unmuted."
                )
                mute_warning = False
            else:
                # Healthy catch-up progress -> Safe to mute warning
                mute_warning = True
        else:
            # Real-time mode -> Do NOT mute
            mute_warning = False

        if self.is_alert_ingestion_delayed(alerts) and not mute_warning:
            self.siemplify.LOGGER.warn(
                "WARNING: Slow Alert Ingestion! "
                "Security alerts are taking longer than expected to be processed "
                f"(over {MAX_ALLOWED_INGESTION_DELAY_MINUTES} minutes). "
                "This may delay incident response. Please check your connector "
                "configuration to improve performance, or contact support for help."
            )

        # Write the current start time as the previous start time for the next run
        write_content(
            self.siemplify,
            str(self.page_start_time),
            file_name=RULE_PREVIOUS_TIMESTAMP_FILE_NAME,
            db_key=RULE_PREVIOUS_TIMESTAMP_DB_KEY,
        )

        self.siemplify.LOGGER.info(
            f"Received nextPageToken: {page_token}, "
            f"nextPageStartTime: {page_start_time}."
        )
        self.page_token = page_token or ""
        if page_start_time is not None:
            self.page_start_time = int(
                convert_string_to_timestamp(page_start_time) * NUM_OF_MILLI_IN_SEC
            )

        return sorted(alerts, key=lambda alert: int(getattr(alert, TIMESTAMP_KEY)))

    def filter_alerts(
        self, alerts: list[Detection], existing_ids: dict[str, int] | list[str]
    ) -> list[Detection]:
        """Filter detections based on existing ids."""
        ids_to_filter = (
            list(existing_ids.keys())
            if isinstance(existing_ids, dict)
            else existing_ids
        )
        filtered_alerts = filter_old_alerts(self.siemplify, alerts, ids_to_filter, "id")
        self.siemplify.LOGGER.info(
            f"Filtered {len(filtered_alerts)} "
            f"{ALERT_TYPE_NAMES.get(ALERT_TYPES.get('rule'))} alerts."
        )
        return filtered_alerts

    def validate_filters(self) -> None:
        """Validate Dynamic List filter configuration early.

        Raises:
            GoogleChronicleValidationError: If filter configuration is invalid
                and fail_on_invalid is True.
        """
        get_filters_by_alert_type(
            self.siemplify.LOGGER,
            self.siemplify.whitelist,
            self.alert_type,
            fail_on_invalid=self.fail_on_invalid,
        )

    def pass_filters(self, alert):
        filters = get_filters_by_alert_type(
            self.siemplify.LOGGER,
            self.siemplify.whitelist,
            self.alert_type,
            fail_on_invalid=self.fail_on_invalid,
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

        if len(pruned_ids) > STORED_IDS_DICT_LIMIT:
            self.siemplify.LOGGER.info(
                f"Pruned stored IDs cache size ({len(pruned_ids)}) exceeds the limit ({STORED_IDS_DICT_LIMIT}). "
                "Sorting and keeping only the most recent IDs to prevent database overflow."
            )
            # Sort ascending by timestamp to keep insertion order stable for identical timestamps
            sorted_items = sorted(pruned_ids.items(), key=lambda item: item[1])
            # Slice from the end to retain the newest items
            pruned_ids = dict(sorted_items[-STORED_IDS_DICT_LIMIT:])

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
                f"RULE existing ids is a {type(existing_ids)}. Falling back to standard SDK list write..."
            )
            write_ids(
                self.siemplify,
                existing_ids,
                ids_file_name=IDS_FILE_NAME,
                db_key=IDS_DB_KEY,
                default_value_to_set=[],
                stored_ids_limit=STORED_IDS_LIMIT,
            )

    def _calculate_last_timestamp_with_padding(self, alerts: list) -> int:
        """
        Finds the timestamp of the last alert and applies padding to handle exclusive API query filters.
        """
        last_alert = max(alerts, key=lambda a: int(getattr(a, TIMESTAMP_KEY)))
        last_timestamp = int(getattr(last_alert, TIMESTAMP_KEY))
        return last_timestamp - DEFAULT_PADDING_PERIOD

    def save_timestamp(self, alerts: list, fetched_alerts_count: int = 0) -> None:
        """Save last timestamp for given alerts.

        Args:
            alerts: {list} list of Detection objects that were successfully processed
            fetched_alerts_count: {int} total number of alerts that were fetched from API
        """
        if len(alerts) < fetched_alerts_count:
            # Partial processing detected (timeout occurred)
            self.siemplify.LOGGER.info(
                f"Partial processing detected ({len(alerts)}/{fetched_alerts_count}). "
                "Clearing nextPageToken to prevent skipping unprocessed alerts."
            )
            self.page_token = ""
            write_content(
                self.siemplify, "", file_name=NEXT_PAGE_KEY, db_key=NEXT_PAGE_KEY
            )

            if alerts:
                last_timestamp_padded = self._calculate_last_timestamp_with_padding(
                    alerts
                )
                self.siemplify.LOGGER.info(
                    f"Saving last processed alert timestamp with 1ms padding: {last_timestamp_padded}"
                )
                write_content(
                    self.siemplify,
                    last_timestamp_padded,
                    file_name=TIMESTAMP_FILE_NAME,
                    db_key=TIMESTAMP_DB_KEY,
                )
            else:
                self.siemplify.LOGGER.info(
                    "No alerts were successfully processed in this run. "
                    "Keeping the previous committed timestamp cursor unchanged."
                )
        else:
            # Full success or no alerts - save the tokens provided by the API
            self.siemplify.LOGGER.info(
                f"Full batch processed or no alerts. Saving API state. "
                f"Token: {self.page_token}, StartTime: {self.page_start_time}"
            )
            write_content(
                self.siemplify,
                self.page_token,
                file_name=NEXT_PAGE_KEY,
                db_key=NEXT_PAGE_KEY,
            )
            write_content(
                self.siemplify,
                self.page_start_time or 0,
                file_name=TIMESTAMP_FILE_NAME,
                db_key=TIMESTAMP_DB_KEY,
            )

    @staticmethod
    def is_alert_ingestion_delayed(alerts: list[Detection]) -> bool:
        """checks for possible ingestion delays between SIEM and SOAR

        Args:
            detections: list of Detection objects

        Returns:
            bool:
                `True` if the detections creation is much earlier then current time,
                `False` otherwise
        """
        if not alerts:
            return False

        latest_detection_dt = max(
            convert_string_to_datetime(detection.created_time) for detection in alerts
        ).astimezone(datetime.timezone.utc)
        allowed_delay = datetime.timedelta(minutes=MAX_ALLOWED_INGESTION_DELAY_MINUTES)
        now = datetime.datetime.now(datetime.timezone.utc)
        return now - latest_detection_dt > allowed_delay

    @staticmethod
    def get_alert_info(alert, environment_common, device_product_field):
        """
        Get alert info
        :param alert: {Detection} Detection object
        :param environment_common: {EnvironmentHandle} environment common object for fetching the environment
        :param device_product_field: {str} key to use for device product extraction
        :return: {AlertInfo} AlertInfo object
        """
        return alert.as_unified_alert_info(
            AlertInfo(), environment_common, device_product_field
        )

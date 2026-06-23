import sys

from EnvironmentCommon import GetEnvironmentCommonFactory
from SiemplifyConnectors import SiemplifyConnectorExecution
from SiemplifyUtils import output_handler, unix_now
from TIPCommon.extraction import extract_connector_param
from TIPCommon.smp_io import read_content, write_content
from TIPCommon.utils import is_overflowed

from consts import (
    ALERT_TYPES,
    ALERT_TYPE_NAMES,
    FALLBACK_SEVERITY_VALUES,
    UNIFIED_CONNECTOR_CONNECTOR_NAME,
    UNIFIED_CONNECTOR_DEFAULT_LIMIT,
    UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME,
    UNIFIED_CONNECTOR_DYNAMIC_FETCH_LIMIT_DB_KEY,
    UNIFIED_CONNECTOR_IS_TIMEOUT_DB_KEY,
    UNIFIED_CONNECTOR_MAX_TIME_FRAME,
    UNIFIED_CONNECTOR_MIN_DYNAMIC_FETCH_LIMIT,
    UNIFIED_CONNECTOR_MAX_SAFE_FETCH_LIMIT,
)
from exceptions import GoogleChronicleValidationError
from ExternalAlert import ExternalAlert
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from IOCAlert import IOCAlert
from RuleAlert import RuleAlert
from utils import convert_list_to_comma_string, is_approaching_timeout

ALERT_TYPE_OBJECTS = {
    ALERT_TYPES.get("rule"): RuleAlert,
    ALERT_TYPES.get("external"): ExternalAlert,
    ALERT_TYPES.get("ioc"): IOCAlert,
}


connector_starting_time = unix_now()


@output_handler
def main(is_test_run):
    siemplify = SiemplifyConnectorExecution()
    siemplify.script_name = UNIFIED_CONNECTOR_CONNECTOR_NAME
    processed_alerts = []
    is_timeout_occurred = False
    initialized = False

    # Log startup status for external log collectors
    siemplify.LOGGER.info("Initializing connector and parameters.")

    if is_test_run:
        siemplify.LOGGER.info(
            '***** This is an "IDE Play Button"\\"Run Connector once" test run ******'
        )

    try:
        siemplify.LOGGER.info(
            "------------------- Main - Param Init -------------------"
        )

        api_root = extract_connector_param(
            siemplify, param_name="API Root", is_mandatory=True, print_value=True
        )
        users_service_account = extract_connector_param(
            siemplify, param_name="User's Service Account", is_mandatory=False
        )
        workload_identity_email = extract_connector_param(
            siemplify, param_name="Workload Identity Email", print_value=False
        )
        verify_ssl = extract_connector_param(
            siemplify,
            param_name="Verify SSL",
            input_type=bool,
            is_mandatory=True,
            print_value=True,
        )
        environment_field_name = extract_connector_param(
            siemplify, param_name="Environment Field Name", print_value=True
        )
        environment_regex_pattern = extract_connector_param(
            siemplify, param_name="Environment Regex Pattern", print_value=True
        )
        script_timeout = extract_connector_param(
            siemplify,
            param_name="PythonProcessTimeout",
            is_mandatory=True,
            input_type=int,
            print_value=True,
        )
        hours_backwards = extract_connector_param(
            siemplify,
            param_name="Max Hours Backwards",
            input_type=int,
            default_value=UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME,
            print_value=True,
        )
        base_fetch_limit = extract_connector_param(
            siemplify,
            param_name="Max Alerts To Fetch",
            input_type=int,
            default_value=UNIFIED_CONNECTOR_DEFAULT_LIMIT,
            print_value=True,
        )
        if base_fetch_limit > UNIFIED_CONNECTOR_MAX_SAFE_FETCH_LIMIT:
            siemplify.LOGGER.info(
                f'"Max Alerts To Fetch" ({base_fetch_limit}) exceeds maximum safe threshold. '
                f"Capping value to {UNIFIED_CONNECTOR_MAX_SAFE_FETCH_LIMIT}."
            )
            base_fetch_limit = UNIFIED_CONNECTOR_MAX_SAFE_FETCH_LIMIT
        fallback_severity = extract_connector_param(
            siemplify,
            param_name="Fallback Severity",
            is_mandatory=True,
            print_value=True,
        )
        device_product_field = extract_connector_param(
            siemplify, param_name="DeviceProductField", is_mandatory=True
        )
        disable_overflow = extract_connector_param(
            siemplify,
            param_name="Disable Overflow",
            input_type=bool,
            default_value=False,
            print_value=True,
        )
        fail_on_invalid = extract_connector_param(
            siemplify,
            param_name="Validate Dynamic List Entries",
            input_type=bool,
            default_value=False,
            print_value=True,
        )

        cached_fetch_limit_str = read_content(
            siemplify,
            file_name=UNIFIED_CONNECTOR_DYNAMIC_FETCH_LIMIT_DB_KEY,
            db_key=UNIFIED_CONNECTOR_DYNAMIC_FETCH_LIMIT_DB_KEY,
            default_value_to_return="",
        )
        effective_fetch_limit = (
            int(cached_fetch_limit_str)
            if cached_fetch_limit_str.isdigit()
            else base_fetch_limit
        )

        is_previous_run_timeout = read_content(
            siemplify,
            file_name=UNIFIED_CONNECTOR_IS_TIMEOUT_DB_KEY,
            db_key=UNIFIED_CONNECTOR_IS_TIMEOUT_DB_KEY,
            default_value_to_return="False",
        )

        if is_previous_run_timeout == "True":
            effective_fetch_limit = max(
                UNIFIED_CONNECTOR_MIN_DYNAMIC_FETCH_LIMIT, effective_fetch_limit // 2
            )
            siemplify.LOGGER.warn(
                f"Previous run timed out. Halving fetch limit to "
                f"{effective_fetch_limit} (base limit: {base_fetch_limit}) to improve stability."
            )
            write_content(
                siemplify,
                str(effective_fetch_limit),
                file_name=UNIFIED_CONNECTOR_DYNAMIC_FETCH_LIMIT_DB_KEY,
                db_key=UNIFIED_CONNECTOR_DYNAMIC_FETCH_LIMIT_DB_KEY,
            )

        alert_types = [ALERT_TYPES.get("rule")]

        siemplify.LOGGER.info("------------------- Main - Started -------------------")

        if not all(alert_type in ALERT_TYPES.values() for alert_type in alert_types):
            raise GoogleChronicleValidationError(
                f'Invalid value provided for "Alert Types". Possible values: '
                f"{convert_list_to_comma_string(list(ALERT_TYPE_NAMES.values()))}"
            )

        if fallback_severity.lower() not in FALLBACK_SEVERITY_VALUES:
            raise GoogleChronicleValidationError(
                f'Invalid value provided for the parameter "Fallback Severity": {fallback_severity}. '
                f"Possible values: {convert_list_to_comma_string(FALLBACK_SEVERITY_VALUES)}."
            )

        if effective_fetch_limit < 0:
            siemplify.LOGGER.info(
                f'"Max Alerts To Fetch" must be non-negative. The default value '
                f"{UNIFIED_CONNECTOR_DEFAULT_LIMIT} will be used"
            )
            effective_fetch_limit = UNIFIED_CONNECTOR_DEFAULT_LIMIT

        if hours_backwards < 0:
            siemplify.LOGGER.info(
                f'"Max Hours Backwards" must be non-negative. The default value '
                f"{UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME} will be used"
            )
            hours_backwards = UNIFIED_CONNECTOR_DEFAULT_TIME_FRAME

        if hours_backwards > UNIFIED_CONNECTOR_MAX_TIME_FRAME:
            siemplify.LOGGER.info(
                f'"Max Hours Backwards" is greater than maximum allowed value. The maximum value '
                f"{UNIFIED_CONNECTOR_MAX_TIME_FRAME} will be used"
            )
            hours_backwards = UNIFIED_CONNECTOR_MAX_TIME_FRAME

        manager = GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=users_service_account,
            workload_identity_email=workload_identity_email,
            chronicle_soar=siemplify,
            api_root=api_root,
            verify_ssl=verify_ssl,
        )

        # Mark as successfully initialized for monitoring
        initialized = True

        for alert_type in alert_types:
            alert_type_name = ALERT_TYPE_NAMES.get(alert_type)
            siemplify.LOGGER.info(f"Started processing {alert_type_name} alert type")

            if is_approaching_timeout(script_timeout, connector_starting_time):
                siemplify.LOGGER.warn(
                    f"Timeout is approaching before starting "
                    f"{alert_type_name} loop. Connector will gracefully exit."
                )
                is_timeout_occurred = True
                break

            alert_type_processed_alerts = []
            fetched_alerts = []
            alert_class = ALERT_TYPE_OBJECTS.get(alert_type)

            if alert_type == ALERT_TYPES.get("rule"):
                alert_object = alert_class(
                    siemplify,
                    manager,
                    script_timeout,
                    connector_starting_time,
                    fail_on_invalid,
                )
                alert_object.validate_filters()
            else:
                alert_object = alert_class(
                    siemplify,
                    manager,
                    script_timeout,
                    connector_starting_time,
                )

            # Read already existing alerts ids
            existing_ids = alert_object.read_ids()

            # Log start of the fetch cycle
            siemplify.LOGGER.info(
                f"Fetch cycle started for alert type {alert_type_name}. "
                f"Max Alerts To Fetch: {effective_fetch_limit}, Max Hours Backwards: {hours_backwards}."
            )

            # Fetch alerts
            filtered_alerts = alert_object.get_alerts(
                existing_ids=existing_ids,
                fetch_limit=effective_fetch_limit,
                hours_backwards=hours_backwards,
                fallback_severity=fallback_severity,
            )

            # Log completion of the fetch cycle and initial queue size
            fetched_count = len(filtered_alerts)
            siemplify.LOGGER.info(
                f"Fetch cycle completed for alert type {alert_type_name}. Fetched {fetched_count} alerts."
            )
            siemplify.LOGGER.info(
                f"Initial backlog queue size: {fetched_count} alerts."
            )

            processed_count = 0
            created_count = 0
            overflow_count = 0
            filtered_count = 0
            failed_count = 0

            for alert in filtered_alerts:
                try:
                    processed_count += 1
                    if is_approaching_timeout(script_timeout, connector_starting_time):
                        siemplify.LOGGER.warn(
                            f"Timeout is approaching. Gracefully exiting loop. "
                            f"Remaining backlog: {fetched_count - processed_count + 1} alerts."
                        )
                        is_timeout_occurred = True
                        break

                    siemplify.LOGGER.info(
                        f"Started processing {alert_type_name} alert {alert.id}"
                    )
                    if is_test_run and alert_type_processed_alerts:
                        siemplify.LOGGER.info(
                            "This is a TEST run. Only 1 alert will be processed."
                        )
                        alert_type_processed_alerts = alert_type_processed_alerts[:1]
                        break
                    if isinstance(existing_ids, dict):
                        existing_ids[alert.id] = int(
                            getattr(alert, alert_object.timestamp_key, 0)
                        )
                    else:
                        existing_ids.append(alert.id)
                    fetched_alerts.append(alert)

                    if not alert_object.pass_filters(alert):
                        filtered_count += 1
                        continue

                    alert_info = alert_object.get_alert_info(
                        alert,
                        GetEnvironmentCommonFactory().create_environment_manager(
                            siemplify,
                            environment_field_name,
                            environment_regex_pattern,
                        ),
                        device_product_field,
                    )

                    if not disable_overflow:
                        if is_overflowed(siemplify, alert_info, is_test_run):
                            overflow_count += 1
                            siemplify.LOGGER.info(
                                f"{str(alert_info.rule_generator)}"
                                f"-{str(alert_info.ticket_id)}"
                                f"-{str(alert_info.environment)}"
                                f"-{str(alert_info.device_product)} "
                                "found as overflow alert. Skipping..."
                            )
                            # If is overflowed we should skip
                            continue

                    alert_type_processed_alerts.append(alert_info)
                    created_count += 1
                    siemplify.LOGGER.info(
                        f"{alert_type_name} alert {alert.id} was created."
                    )

                except Exception as e:
                    failed_count += 1
                    siemplify.LOGGER.error(
                        f"Failed to process {alert_type_name} alert {alert.id}. Error: {e}"
                    )
                    siemplify.LOGGER.exception(e)

                    if is_test_run:
                        raise

                siemplify.LOGGER.info(
                    f"Finished processing {alert_type_name} alert {alert.id}"
                )

            if not is_test_run:
                siemplify.LOGGER.info(f"Saving {alert_type_name} timestamp.")
                alert_object.save_timestamp(
                    fetched_alerts, fetched_alerts_count=len(filtered_alerts)
                )

            if not is_test_run:
                siemplify.LOGGER.info(f"Saving {alert_type_name} existing ids.")
                if isinstance(existing_ids, dict):
                    alert_object.write_ids(existing_ids)
                else:
                    alert_object.write_ids(list(set(existing_ids)))

            processed_alerts.extend(alert_type_processed_alerts)
            siemplify.LOGGER.info(
                f"Processed {len(alert_type_processed_alerts)} "
                f"{alert_type_name} alerts"
            )

            # Log pipeline state cycle summary
            duplicates_count = getattr(manager, "duplicates_count", 0)
            siemplify.LOGGER.info(
                f"Cycle summary for {alert_type_name}: "
                f"Fetched: {fetched_count}, Iterated: {processed_count}, "
                f"Created: {created_count}, Already Processed and Skipped: {duplicates_count}, "
                f"Overflowed: {overflow_count}, Filtered: {filtered_count}, "
                f"Failed: {failed_count}."
            )

    except Exception as e:
        if not initialized:
            siemplify.LOGGER.error(
                f"Connector setup and parameter extraction failed. Error: {e}"
            )
        else:
            siemplify.LOGGER.error(f"Pipeline execution failed and crashed. Error: {e}")
        siemplify.LOGGER.exception(e)

        if is_test_run:
            raise

    siemplify.LOGGER.info(f"Created total of {len(processed_alerts)} cases")

    if not is_test_run:
        write_content(
            siemplify,
            str(is_timeout_occurred),
            file_name=UNIFIED_CONNECTOR_IS_TIMEOUT_DB_KEY,
            db_key=UNIFIED_CONNECTOR_IS_TIMEOUT_DB_KEY,
        )
        if is_timeout_occurred:
            siemplify.LOGGER.info(f"Saving timeout status: {is_timeout_occurred}")

        if not is_timeout_occurred and cached_fetch_limit_str:
            siemplify.LOGGER.info(
                "Run completed successfully without timeouts. Resetting dynamic fetch limit."
            )
            write_content(
                siemplify,
                "",
                file_name=UNIFIED_CONNECTOR_DYNAMIC_FETCH_LIMIT_DB_KEY,
                db_key=UNIFIED_CONNECTOR_DYNAMIC_FETCH_LIMIT_DB_KEY,
            )

    # Shutdown log for monitoring
    siemplify.LOGGER.info("Connector execution finished.")
    siemplify.LOGGER.info("------------------- Main - Finished -------------------")
    siemplify.return_package(processed_alerts)


if __name__ == "__main__":
    # Connectors are run in iterations. The interval is configurable from the ConnectorsScreen UI.
    is_test = not (len(sys.argv) < 2 or sys.argv[1] == "True")
    main(is_test)

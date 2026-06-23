from __future__ import annotations

import ipaddress
from typing import Any

from SiemplifyUtils import convert_dict_to_json_result_dict
from TIPCommon import validation
from TIPCommon.base.action import Action
from TIPCommon.extraction import (
    extract_action_param,
    extract_configuration_param,
)
from TIPCommon.transformation import convert_list_to_comma_string
from TIPCommon.utils import is_empty_string_or_none
from TIPCommon.types import SingleJson

import consts
from datamodels import ReferenceList
from exceptions import GoogleChronicleNotFoundError
from GoogleChronicleManager import GoogleChronicleManager
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2


class IsValueInReferenceList(Action):

    def __init__(self) -> None:
        super().__init__(consts.IS_VALUE_IN_REFERENCE_IN_LIST_SCRIPT_NAME)
        self.output_message: str = (
            "Successfully searched provided values in the "
            f"reference lists in {consts.INTEGRATION_DISPLAY_NAME}."
        )
        self.error_output_message: str = f'Error executing action "{self.name}".'

    def _extract_action_parameters(self) -> None:
        self.params.user_service_account = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="User's Service Account",
            remove_whitespaces=False,
        )
        self.params.workload_identity_email = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Workload Identity Email",
        )
        self.params.api_root = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="API Root",
            is_mandatory=True,
            print_value=True,
        )
        self.params.verify_ssl = extract_configuration_param(
            self.soar_action,
            provider_name=consts.INTEGRATION_NAME,
            param_name="Verify SSL",
            is_mandatory=True,
            input_type=bool,
            print_value=True,
        )
        self.params.reference_list_names = extract_action_param(
            self.soar_action,
            param_name="Reference List Names",
            is_mandatory=True,
            print_value=True,
        )
        self.params.values = extract_action_param(
            self.soar_action,
            param_name="Values",
            is_mandatory=True,
            print_value=True,
        )
        self.params.case_insensitive_search = extract_action_param(
            self.soar_action,
            param_name="Case Insensitive Search",
            is_mandatory=False,
            print_value=True,
            input_type=bool,
            default_value=True,
        )

    def _validate_params(self) -> None:
        validator: validation.ParameterValidator = validation.ParameterValidator(
            self.soar_action
        )

        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        self.params.reference_list_names = validator.validate_csv(
            param_name="Reference List",
            csv_string=self.params.reference_list_names,
        )
        self.params.values = validator.validate_csv(
            param_name="Values",
            csv_string=self.params.values,
        )

    def _init_api_clients(self) -> GoogleChronicleManager:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _) -> None:
        fetched_lists: list[ReferenceList] = self._fetch_and_validate_lists()
        results: SingleJson = {}

        for value in self.params.values:
            found_in_lists: list[str] = []
            not_found_in_lists: list[str] = []

            for ref_list in fetched_lists:
                is_found: bool = self._is_value_in_list(
                    value, ref_list, self.params.case_insensitive_search
                )
                if is_found:
                    found_in_lists.append(ref_list.name)
                    continue

                not_found_in_lists.append(ref_list.name)

            overall_status: str = (
                consts.REFERENCE_LIST_FOUND_STRING
                if found_in_lists
                else consts.REFERENCE_LIST_NOT_FOUND_STRING
            )
            results[value] = {
                "found_in": convert_list_to_comma_string(found_in_lists),
                "not_found_in": convert_list_to_comma_string(
                    not_found_in_lists
                ),
                "overall_status": overall_status,
            }

        self.json_results: SingleJson = convert_dict_to_json_result_dict(results)

    def _fetch_and_validate_lists(self) -> list[Any]:
        self.logger.info("Getting the reference list")
        found_lists: list[ReferenceList] = []
        not_found_lists: list[str] = []

        for list_name in self.params.reference_list_names:
            try:
                reference_list: ReferenceList
                reference_list = self.api_client.get_reference_list_details(
                    list_name
                )
                found_lists.append(reference_list)
            except GoogleChronicleNotFoundError:
                not_found_lists.append(list_name)

        if not_found_lists:
            not_found_csv: str = convert_list_to_comma_string(not_found_lists)
            raise Exception(
                "The following reference lists were not found in "
                f"{consts.INTEGRATION_NAME}: {not_found_csv}. Please use "
                'action "Get Reference Lists" to see, what reference lists '
                "are available."
            )

        return found_lists

    def _is_value_in_list(
        self,
        value: str,
        reference_list: ReferenceList,
        case_insensitive: bool,
    ) -> bool:
        for line in reference_list.lines:
            stripped_line: str = line.strip()
            if not stripped_line:
                continue

            try:
                ip_to_check: ipaddress.IPv4Address | ipaddress.IPv6Address = (
                    ipaddress.ip_address(value)
                )
                network_to_check: ipaddress.IPv4Network | ipaddress.IPv6Network = (
                    ipaddress.ip_network(stripped_line)
                )
                if ip_to_check in network_to_check:
                    return True
            except ValueError:
                value_to_compare: str = value.lower() if case_insensitive else value
                line_to_compare: str = (
                    stripped_line.lower() if case_insensitive else stripped_line
                )
                if value_to_compare == line_to_compare:
                    return True

        return False


def main() -> None:
    IsValueInReferenceList().run()


if __name__ == "__main__":
    main()

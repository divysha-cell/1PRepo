from __future__ import annotations

import ipaddress
from functools import lru_cache
from typing import Any, Iterator, TYPE_CHECKING

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param, extract_configuration_param
from TIPCommon.transformation import string_to_multi_value
from TIPCommon.utils import is_empty_string_or_none
from TIPCommon.validation import ParameterValidator

import consts
from exceptions import (
    GoogleChronicleAPILimitError,
    GoogleChronicleManagerError,
    GoogleChronicleValidationError,
)
from GoogleChronicleManagerV2 import GoogleChronicleManagerV2
from utils import validate_api_root_for_backstory

if TYPE_CHECKING:
    from typing import Never

    from TIPCommon.types import SingleJson

    from datamodels import AddedDataTableRow, DataTableDetails


class IsCIDRInDataTableAction(Action):

    def __init__(self) -> None:
        super().__init__(consts.IS_CIDR_IN_DATA_TABLE_SCRIPT_NAME)

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
        self.params.data_table_name = extract_action_param(
            self.soar_action,
            param_name="Data Table Name",
            print_value=True,
            is_mandatory=True,
        )
        self.params.column_data_str = extract_action_param(
            self.soar_action,
            param_name="Column",
            print_value=True,
        )
        self.params.cidr_data_str = extract_action_param(
            self.soar_action,
            param_name="CIDR",
            print_value=True,
            is_mandatory=True,
        )
        self.params.max_data_table_rows_to_return = extract_action_param(
            self.soar_action,
            param_name="Max Data Table Rows To Return",
            print_value=True,
            is_mandatory=True,
            input_type=int,
            default_value=consts.MAX_DATA_TABLE_ROWS_TO_RETURN,
        )
        self.params.columns_to_search: list[str] = []
        self.params.cidrs_to_search: list[str] = []

    def _validate_params(self) -> None:
        validator: ParameterValidator = ParameterValidator(self.soar_action)

        if not is_empty_string_or_none(self.params.user_service_account):
            self.params.user_service_account = validator.validate_json(
                param_name="User's Service Account",
                json_string=self.params.user_service_account,
                print_value=False,
            )

        validator.validate_range(
            param_name="Max Data Table Rows To Return",
            value=self.params.max_data_table_rows_to_return,
            min_limit=consts.MINIMUM_DATA_TABLE_ROWS_TO_RETURN,
            max_limit=consts.MAX_DATA_TABLE_ROWS_TO_RETURN,
        )

        if not self.params.cidr_data_str or not self.params.cidr_data_str.strip():
            raise GoogleChronicleValidationError(
                'Parameter "CIDR" is mandatory and cannot be empty.'
            )
        self.params.cidrs_to_search = string_to_multi_value(
            string_value=self.params.cidr_data_str,
        )
        if not self.params.cidrs_to_search:
            raise GoogleChronicleValidationError(
                'Parameter "CIDR" is mandatory and cannot be empty.'
            )

        for cidr in self.params.cidrs_to_search:
            try:
                ipaddress.ip_network(cidr, strict=False)
            except ValueError as exc:
                raise GoogleChronicleValidationError(
                    f'"{cidr}" is not a valid CIDR in the "CIDR" parameter.'
                ) from exc

        if self.params.column_data_str and self.params.column_data_str.strip():
            self.params.columns_to_search = string_to_multi_value(
                string_value=self.params.column_data_str,
            )

    def _init_api_clients(self) -> GoogleChronicleManagerV2:
        return GoogleChronicleManagerV2.create_manager_instance(
            user_service_account=self.params.user_service_account,
            chronicle_soar=self.soar_action,
            api_root=self.params.api_root,
            verify_ssl=self.params.verify_ssl,
            workload_identity_email=self.params.workload_identity_email,
        )

    def _perform_action(self, _: Never) -> None:
        validate_api_root_for_backstory(self.params.api_root)

        table_details: DataTableDetails = self._fetch_table_details()

        if not table_details.ordered_column_names:
            raise GoogleChronicleManagerError(
                f"Data table “{self.params.data_table_name}” has no columns."
            )

        (
            columns_to_search,
            column_indices_to_search,
        ) = self._get_columns_to_search(table_details)
        self.soar_action.LOGGER.info(
            f"Will search for CIDRs in columns: {', '.join(columns_to_search)}"
        )

        self.soar_action.LOGGER.info(
            "Fetching all rows from data table to perform client-side filtering."
        )
        all_rows: list[AddedDataTableRow] = list(self._paginated_list_rows())
        self.soar_action.LOGGER.info(
            f"Fetched {len(all_rows)} rows from the data table."
        )

        self.json_results = self._process_searches(
            all_rows=all_rows,
            all_table_columns=table_details.ordered_column_names,
            column_indices_to_search=column_indices_to_search,
        )
        self.output_message = (
            "Successfully searched provided CIDR values in the data table "
            f"{self.params.data_table_name} in Google SecOps."
        )

    def _fetch_table_details(self) -> DataTableDetails:
        self.soar_action.LOGGER.info(
            f"Fetching details for data table: {self.params.data_table_name}"
        )
        try:
            return self.api_client.data_table_details(
                data_table_identifier=self.params.data_table_name
            )
        except GoogleChronicleManagerError as exc:
            raise GoogleChronicleManagerError(
                f"Failed to fetch details for data table "
                f"“{self.params.data_table_name}”. The table might not exist "
                f"or an API error occurred."
            ) from exc

    def _get_columns_to_search(
        self,
        table_details: DataTableDetails,
    ) -> tuple[list[str], list[int]]:
        all_table_columns: list[str] = table_details.ordered_column_names
        column_name_to_type: dict[str, str]
        column_name_to_type = self._get_column_name_to_type_mapping(table_details)

        columns_to_search: list[str]
        if self.params.columns_to_search:
            columns_to_search = self._get_user_specified_search_columns(
                all_table_columns, column_name_to_type
            )
        else:
            columns_to_search = self._get_all_cidr_search_columns(
                column_name_to_type,
            )

        column_indices: list[int] = [
            all_table_columns.index(col) for col in columns_to_search
        ]

        return columns_to_search, column_indices

    def _get_column_name_to_type_mapping(
        self,
        table_details: DataTableDetails,
    ) -> dict[str, str]:
        column_name_to_type: dict[str, str] = {}
        try:
            for col_info_obj in table_details.column_info:
                col_info_dict: SingleJson = col_info_obj.to_json()
                column_name_to_type[col_info_dict["originalColumn"]] = col_info_dict[
                    "columnType"
                ]
            return column_name_to_type
        except (KeyError, TypeError, AttributeError) as e:
            raise GoogleChronicleManagerError(
                "Could not determine column types. Failed to parse the 'column_info' "
                f"structure from the data table details. The underlying error was: {e}"
            ) from e

    def _get_user_specified_search_columns(
        self,
        all_table_columns: list[str],
        column_name_to_type: dict[str, str],
    ) -> list[str]:
        invalid_columns: set[str] = set(self.params.columns_to_search) - set(
            all_table_columns
        )
        if invalid_columns:
            raise GoogleChronicleManagerError(
                f"The following columns were not found in the "
                f"'{self.params.data_table_name}': "
                f"{', '.join(invalid_columns)}. Please check the spelling."
            )

        for col_name in self.params.columns_to_search:
            if column_name_to_type.get(col_name) != consts.CIDR_COLUMN_TYPE:
                raise GoogleChronicleValidationError(
                    f"Column '{col_name}' in data table '{self.params.data_table_name}'"
                    " is not of type 'CIDR'. Only 'CIDR' type columns can be searched."
                )

        return self.params.columns_to_search

    def _get_all_cidr_search_columns(
        self,
        column_name_to_type: dict[str, str],
    ) -> list[str]:
        columns_to_search: list[str] = [
            name
            for name, col_type in column_name_to_type.items()
            if col_type == consts.CIDR_COLUMN_TYPE
        ]

        if not columns_to_search:
            raise GoogleChronicleValidationError(
                f"Data table '{self.params.data_table_name}' does not contain "
                "any columns of type 'CIDR'. At least one 'CIDR' type column is "
                "required to perform the search when no specific column is provided."
            )

        return columns_to_search

    def _paginated_list_rows(self) -> Iterator[AddedDataTableRow]:
        try:
            yield from self.api_client.list_all_data_table_rows(
                data_table_identifier=self.params.data_table_name,
            )
        except GoogleChronicleAPILimitError as e:
            raise GoogleChronicleAPILimitError(
                "Reached an API rate limit for the action. Try again in 1 minute."
            ) from e
        except GoogleChronicleManagerError as e:
            raise GoogleChronicleManagerError(
                f"Failed to list data table rows for table "
                f"“{self.params.data_table_name}”. API Error: {e}"
            ) from e

    def _process_searches(
        self,
        all_rows: list[AddedDataTableRow],
        all_table_columns: list[str],
        column_indices_to_search: list[int],
    ) -> list[SingleJson]:
        all_results: list[SingleJson] = []
        user_cidrs: dict[str, ipaddress.IPv4Network | ipaddress.IPv6Network] = {
            cidr_str: ipaddress.ip_network(cidr_str, strict=False)
            for cidr_str in self.params.cidrs_to_search
        }

        for cidr_str, cidr_network in user_cidrs.items():
            self.soar_action.LOGGER.info(
                f"Searching for IPs within CIDR '{cidr_str}'..."
            )
            matched_rows: list[AddedDataTableRow] = self._find_matches_for_cidr(
                cidr_network=cidr_network,
                all_rows=all_rows,
                column_indices_to_search=column_indices_to_search,
            )

            all_results.append(
                {
                    "Entity": cidr_str,
                    "EntityResult": {
                        "is_found": bool(matched_rows),
                        "matched_rows": self._build_json_rows(
                            matched_rows, all_table_columns
                        ),
                    },
                }
            )

        return all_results

    def _find_matches_for_cidr(
        self,
        cidr_network: ipaddress.IPv4Network | ipaddress.IPv6Network,
        all_rows: list[AddedDataTableRow],
        column_indices_to_search: list[int],
    ) -> list[AddedDataTableRow]:
        matched_rows: list[AddedDataTableRow] = []
        for row in all_rows:
            if self._row_matches_cidr(row, cidr_network, column_indices_to_search):
                matched_rows.append(row)
                if len(matched_rows) >= self.params.max_data_table_rows_to_return:
                    self.soar_action.LOGGER.info(
                        f"Reached max matches "
                        f"({self.params.max_data_table_rows_to_return}) "
                        f"for CIDR '{cidr_network}'."
                    )
                    break

        return matched_rows

    def _row_matches_cidr(
        self,
        row: AddedDataTableRow,
        user_cidr_network: ipaddress.IPv4Network | ipaddress.IPv6Network,
        column_indices: list[int],
    ) -> bool:
        for index in column_indices:
            if index < len(row.values):
                cell_value: Any = row.values[index]
                table_cidr_network: (
                    ipaddress.IPv4Network | ipaddress.IPv6Network | None
                ) = self._get_ip_network_from_string(cell_value)
                if table_cidr_network and table_cidr_network.overlaps(
                    user_cidr_network
                ):
                    return True

        return False

    @staticmethod
    @lru_cache(maxsize=10240)
    def _get_ip_network_from_string(
        value: Any,
    ) -> ipaddress.IPv4Network | ipaddress.IPv6Network | None:
        if not isinstance(value, str):
            return None
        try:
            return ipaddress.ip_network(value, strict=False)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def _build_json_rows(
        matched_rows: list[AddedDataTableRow],
        ordered_columns: list[str],
    ) -> list[SingleJson]:
        json_rows: list[SingleJson] = []
        for row in matched_rows:
            row_json: SingleJson = row.to_json()
            row_json["values"] = dict(zip(ordered_columns, row.values))
            json_rows.append(row_json)

        return json_rows


def main() -> None:
    action = IsCIDRInDataTableAction()
    action.run()


if __name__ == "__main__":
    main()

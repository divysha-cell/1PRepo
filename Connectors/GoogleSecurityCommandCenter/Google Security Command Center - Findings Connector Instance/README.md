# Google Security Command Center - Findings Connector Instance



Integration: GoogleSecurityCommandCenter

Integration Version: 17

Device Product Field: findingClass

Event Name Field: category
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|dummy_value|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|API Root|API root of the Google Security Command Center instance.|True|https://securitycenter.googleapis.com|
|Organization ID|ID of the organization that should be used in Google Security Command Center integration.|False|dummy_value|
|Project ID|ID of the project that should be used in Google Security Command Center integration. Takes priority over Organization ID, if both are provided.|False|dummy_value|
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the “Service Usage Consumer” IAM role to your Google Cloud service account.|False|dummy_value|
|Location ID|ID of the location that should be used in Google Security Command Center integration. Defaults to ‘global’|False|global|
|User's Service Account|Service account of the Google Security Command Center instance. A full content of the service account JSON file should be provided. This or "Workload Identity Email" must be provided.|False|*****|
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|dummy_value|
|Finding Class Filter|Finding classes that should be ingested. Possible values: Threat, Vulnerability, Misconfiguration, SCC_Error, Observation, Toxic_Combination, Chokepoint.  If nothing is provided, findings from all classes will be ingested.|False|Threat,Vulnerability,Misconfiguration,SCC_Error,Observation,Toxic_Combination,Chokepoint|
|Lowest Severity To Fetch|The lowest severity that is used to fetch findings. Possible values: Low, Medium, High, Critical. Note: If finding with undefined severity is ingested, it has the "Fallback Severity" severity, and it will not be filtered out by this parameter. If nothing is provided, findings with all types of severity are ingested.|False|dummy_value|
|Fallback Severity|Fallback severity that is used for the finding that has undefined severity. If nothing is provided, the parameter is set to "Medium". Possible values: Low, Medium, High, Critical.|False|Medium|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve findings from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Findings To Fetch|How many findings to process per one connector iteration. Default: 100. Maximum: 1000.|False|100|
|Use dynamic list as a blacklist|If enabled, dynamic lists will be used as a blacklist.|False|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft 365 Defender server is valid.|False|true|
|Proxy Server Address|The address of the proxy server to use.|False|dummy_value|
|Proxy Username|The proxy username to authenticate with.|False|dummy_value|
|Proxy Password|The proxy password to authenticate with.|False|*****|


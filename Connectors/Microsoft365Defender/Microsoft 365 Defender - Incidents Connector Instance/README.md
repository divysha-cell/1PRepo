# Microsoft 365 Defender - Incidents Connector Instance



Integration: Microsoft365Defender

Integration Version: 26

Device Product Field: event_type

Event Name Field: @odata.type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|dummy_value|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|Login API Root|Login API root of the Microsoft 365 Defender instance.|True|https://login.microsoftonline.com|
|Graph API Root|API root of the Microsoft Graph service.|True|https://graph.microsoft.com|
|Tenant ID|Microsoft 365 Defender account tenant ID.|True|dummy_value|
|Client ID|Microsoft 365 Defender account client ID.|True|dummy_value|
|Client Secret|Microsoft 365 Defender account client secret.|True|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft 365 Defender server is valid.|False|true|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch incidents. Possible values: Informational, Low, Medium, High.|False|dummy_value|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Incidents To Fetch|How many incidents  to process per one connector iteration. Maximum is 20.|False|10|
|Dynamic List Field|Field that can be used in the dynamic list for filtering. Possible values: Incident Name, Alert Name. If nothing is provided, connector will work with the incident name.|False|Incident Name|
|Incident Status Filter|A comma-separated list of incident statuses that need to be ingested. If nothing is provided, the connector will ingest incidents with status “Active” and “In Progress”. Possible values:
Active, In Progress, Resolved, Redirected.
Note: it’s not recommended to ingest redirected incidents, because in most situations they will be empty.|False|Active, In Progress|
|Alert Detection Source Filter|A comma-separated list of detection sources of alerts that need to be ingested. Note: this is a case sensitive parameter. Example of the values:
antivirus, microsoftDefenderForEndpoint|False|dummy_value|
|Alert Service Source Filter|A comma-separated list of service sources of alerts that need to be ingested. Note: this is a case sensitive parameter. Example of the values:
antivirus, microsoftDefenderForEndpoint|False|dummy_value|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|true|
|Lowest Alert Severity To Fetch|Lowest severity that will be used to fetch alerts. Possible values: Informational, Low, Medium, High.|False|dummy_value|
|Disable Alert Tracking|If enabled, the connector will stop tracking updates associated with alerts.|False|false|
|Proxy Server Address|The address of the proxy server to use.|False|dummy_value|
|Proxy Username|The proxy username to authenticate with.|False|dummy_value|
|Proxy Password|The proxy password to authenticate with.|False|*****|


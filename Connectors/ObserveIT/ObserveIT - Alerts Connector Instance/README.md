# ObserveIT - Alerts Connector Instance



Integration: ObserveIT

Integration Version: 7

Device Product Field: Product Name

Event Name Field: eventType
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration.|False|25|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Use SSL|Option to enable SSL/TLS connection|False|true|
|Proxy Server Address|The address of the proxy server to use|False|dummy_value|
|Proxy Username|The proxy username to authenticate with|False|dummy_value|
|Proxy Password|The proxy password to authenticate with|False|*****|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|dummy_value|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.
Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|API Root|API root of ObserveIT server.|True|https://x.x.x.x:x|
|Client ID|Client ID of the ObserveIT app.|True|dummy_value|
|Client Secret|Client Secret of the ObserveIT app.|True|*****|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch Alerts. Possible values: Low, Medium, High, Critical.|True|Medium|


# FireEye ETP - Email Alerts Connector Instance



Integration: FireEyeETP

Integration Version: 8

Device Product Field: Product Name

Event Name Field: alertType
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|dummy_value|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.
Default is .* to catch all and return the value unchanged.
Used to allow the user to manipulate the environment field via regex logic.
If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.
|False|.*|
|API Root|API root of the FireEye ETP instance.|True|https://etp.us.fireeye.com|
|API Key|API Key of the FireEye ETP account.|True|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the FireEye ETP server is valid.|False|False|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Timezone|Timezone of the instance. Default: UTC. Example: +1 will be UTC+1 and -1 will be UTC-1.|False|dummy_value|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|false|
|Proxy Server Address|The address of the proxy server to use|False|dummy_value|
|Proxy Username|The proxy username to authenticate with|False|dummy_value|
|Proxy Password|The proxy password to authenticate with|False|*****|


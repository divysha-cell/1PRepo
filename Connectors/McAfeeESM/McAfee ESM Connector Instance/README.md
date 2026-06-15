# McAfee ESM Connector Instance



Integration: McAfeeESM

Integration Version: 46

Device Product Field: data_type

Event Name Field: alarmName
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Use AES Encryption|If enabled, integration will authenticate using AES Encryption and will not do Base64 inside the code. Note: you need to provide Login and Password already as Base64 encoded strings.|False|false|
|Verify SSL|If enabled, verifies that the SSL certificate for the connection to the McAfee ESM server is valid.|False|false|
|Lowest Severity To Fetch|The lowest severity that needs to be used to fetch alarms. Possible values are in range from 0 to 100. If nothing is specified, the connector ingests alarms with all severities.|False|0|
|Ingest 0 Source Event Alarms|If enabled, action will ingest alarms that have 0 source events. Note: this can have an impact on the values that come from parameters “Product Field Name”, “Event Field Name”, “Rule Generator Field Name”. Connector will wait the time that is provided in the parameter “Padding Time”, if the parameter is disabled.|False|true|
|Padding Time|The number of hours that connector will use for padding. Note: this parameter describes how long the connector will wait to ingest the alarm with 0 source events, if "Ingest 0 Source Event Alarms" is disabled. Maximum: 6 hours.|False|1|
|Time Format|Time format that will be used to read the timestamp provided in McAfee ESM. If nothing is provided or invalid time format is provided, then the connector will not perform the transformation.|False|%m/%d/%Y %H:%M:%S|
|Time Zone|Time zone of the source event. This parameter is needed to transform the timestamp into the format that reflects UTC+0 time. Note: this parameter is ignored, if invalid values are provided in the "Time Format" parameter or nothing is provided there.|False|0|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alarms from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|1|
|Max Alarms To Fetch|The number of alarms to process per one connector iteration. Default: 100.|False|100|
|Use dynamic list as a blacklist|If enabled, dynamic lists will be used as a blacklist.|False|false|
|Rule Generator Field Name|Name of the field that will be used in the rule generator. Note: action will use "alarmName", if value is not available and this parameter is only applied to the values that come from source events.|False|alarmName|
|Secondary Device Product Field|Fallback product field name.|False|dummy_value|
|Disable Overflow|If enabled, the connector will disable the overflow mechanism.|False|false|
|Disable Overflow For Alarm Names|A comma-separated list of alarm names for which connector will ignore overflow. Note: requires "Disable Overflow" to be enabled.|False|dummy_value|
|Proxy Server Address|The address of the proxy server to use.|False|dummy_value|
|Proxy Username|The proxy username to authenticate with.|False|dummy_value|
|Proxy Password|The proxy password to authenticate with.|False|*****|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|srcZone|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|.*|
|API Root|API root of the McAfee ESM instance. Format: https://{ip address}/rs/|True|https://{ip address}/rs/|
|Username|Username of the McAfee ESM account.|True|dummy_value|
|Password|Password of the McAfee ESM account.|True|*****|
|Product Version|Version of Mcafee ESM. Possible values: 11.1, 11.2, 11.3, 11.4, 11.5.|True|dummy_value|


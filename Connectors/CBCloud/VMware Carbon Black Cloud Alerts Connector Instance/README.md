# VMware Carbon Black Cloud Alerts Connector Instance



Integration: CBCloud

Integration Version: 38

Device Product Field: ProductName

Event Name Field: type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is ""|False|dummy_value|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|.*|
|API Root|Vmware Carbon Black Cloud API Root URL|True|dummy_value|
|Organization Key|Vmware Carbon Black Cloud Organization Key|True|dummy_value|
|API ID|Vmware Carbon Black Cloud API ID (Custom API Key ID)|True|*****|
|API Secret Key|Vmware Carbon Black Cloud API Secret Key (Custom API Secret Key)|True|*****|
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|false|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|10|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|24|
|Minimum Severity to Fetch|Minimum severity of Carbon Black Cloud alert to be ingested to Siemplify|False|0|
|What Alert Field to use for Name field|What Carbon Black Cloud alert field should be used for the Siemplify Alert Name field. Possible values are: type, policy_name|True|type|
|What Alert Field to use for Rule Generator|What Carbon Black Cloud alert field should be used for the Siemplify Alert Rule Generator field. Possible values are: type, policy_name|True|type|
|Proxy Server Address|Proxy server to use for connection.|False|dummy_value|
|Proxy Server Username|Proxy server username|False|dummy_value|
|Proxy Server Password|Proxy server password|False|*****|


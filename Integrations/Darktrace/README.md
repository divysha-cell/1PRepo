
# Darktrace

Darktrace empowers defenders to reduce risk and minimize cyber disruption. Its Self-Learning AI technology develops a deep and evolving understanding on your bespoke organization, allowing it to prevent, detect, and respond to unpredictable cyber-attacks across the entire digital environment – from cloud and email to endpoints and OT networks.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root||True|String|https://{{api root}}|
|API Token||True|String||
|API Private Token||True|Password|*****|
|Verify SSL||False|Boolean|true|


#### Dependencies
| |
|-|
|requests-2.32.5-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|google_auth-2.43.0-py2.py3-none-any.whl|
|certifi-2025.11.12-py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|cachetools-6.2.2-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|TIPCommon-1.1.0.1-py2.py3-none-any.whl|
|urllib3-2.5.0-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Add Comment To Model Breach
Add a comment to model breach in Darktrace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Specify the comment for the model breach.|True|String||
|Model Breach ID|Specify the ID of the model breach to which you want to add a comment.|True|String||



#### Execute Custom Search
Execute custom search in Darktrace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Specify the query that needs to be executed.|True|String||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time". If "Alert Time Till Now" is selected, action will use start time of the alert as start time for the search and end time will be current time. If "30 Minutes Around Alert Time" is selected, action will search the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened. Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time"|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|



#### List Similar Devices
List similar devices to the endpoint in Darktrace. Supported entities: IP, Hostname, Mac Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Devices To Return|Specify how many devices to return per entity. Default: 50.|False|String|50|



#### Update Model Breach Status
Update model breach status in Darktrace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Status|Specify what status to set for the model breach.|True|List|Acknowledged|
|Model Breach ID|Specify the id of the model breach, for which you want to update status.|True|String||



#### Ping
Test connectivity to the Darktrace with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Enrich Entities
Enrich entities using information from Darktrace. Supported entities: IP, Hostname, MacAddress, URL. Note: action will extract the domain part out of URL entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fetch Connection Data|If enabled, action will return additional information about connections related to the internal endpoints of Darktrace.|False|Boolean|true|
|Max Hours Backwards|Specify how many hours backwards, action needs to fetch connection data. Default: 24.|False|String|24|
|Create Endpoint Insight|If enabled, action will create an insight containing information about the internal endpoints of Darktrace.|False|Boolean|true|



#### List Endpoint Events
List latest events related to the endpoint in Darktrace. Supported entities: IP, Hostname, MacAddress. Note: events will be returned in UTC timezone.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event Type|Specify a comma-separated list of event types that they want to return. Possible values: connection, unusualconnection, newconnection, notice, devicehistory, modelbreach.|True|String|connection,unusualconnection,notice|
|Time Frame|Specify a time frame for the search. If "Custom" is selected, you also need to provide "Start Time".|True|List|Last Hour|
|Start Time|Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the search. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Events To Return|Specify how many events to return per event type. Default: 50.|False|String|50|









## Connectors
#### Darktrace - AI Incident Events Connector
Pull information about AI incident events from Darktrace. Dynamic list works with "title" parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Darktrace instance.|True|String|https:/{{api root}}|
|API Token|Darktrace API token|True|String||
|API Private Token|Darktrace API private token|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Darktrace server is valid.|False|Boolean|true|
|Lowest AI Incident Score To Fetch|Lowest score that will be used to fetch AI incidents. Maximum: 100.|True|Int|0|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|1|
|Max AI Incidents To Fetch|How many model breaches to process per one connector iteration. Maximum is 100.|False|Int|10|
|Use dynamic list as a blocklist|If enabled, dynamic list will be used as a blocklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|


#### Darktrace - Model Breaches Connector
Pull information about model breaches and connections events related to them from Darktrace.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Darktrace instance.|True|String|https:/{{api root}}|
|API Token|Darktrace API token|True|String||
|API Private Token|Darktrace API private token|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Darktrace server is valid.|False|Boolean|true|
|Lowest Model Breach Score To Fetch|Lowest score that will be used to fetch model breaches. Maximum: 100.|False|Int|0|
|Lowest Priority To Fetch|Lowest priority that will be used to fetch model breaches. Provided as integer. 1, 2, 3 - Informational, 4 - Suspicious, 5 - Critical|False|Int||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve model breaches from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|1|
|Max Model Breaches To Fetch|How many model breaches to process per one connector iteration. Maximum is 1000.|False|Int|10|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|true|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Behaviour Visibility|Behavior visibility values that need to be ingested. Possible values: Critical, Suspicious, Compliance, Informational.|False|String||
|Padding Time|Amount of hours that will be used as a padding. If nothing is provided, this parameter is not going to be applied. Max 100 hours.|False|Int||





Read123!@#
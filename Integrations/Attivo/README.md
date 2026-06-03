
# Attivo

Efficiently derail attacker discovery, lateral movement, privilege escalation, & collection activities early in the attack cycle with Attivo.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root||True|String|https:/{{ip address}}|
|Username||True|String||
|Password||True|Password|*****|
|Verify SSL||False|Boolean|True|


#### Dependencies
| |
|-|
|idna-3.13-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|requests-2.32.4-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|


## Actions
#### List Vulnerability Hosts
List hosts related to the vulnerability in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vulnerabilities|Specify a comma-separated list of vulnerabilities for which action needs to return hostnames.|True|String||
|Max Hosts To Return|Specify how many hosts to return. If nothing is provided, action will return 50 hosts.|False|String|50|



#### Enrich Entities
Enrich entities using information from Attivo. Supported entities: Hostname, IP Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Include ThreatPaths|If enabled, action will return information about ThreatPaths related to the entity.|False|Boolean|true|
|Include Vulnerabilities|If enabled, action will return information about vulnerabilities related to the entity.|False|Boolean|true|
|Include Credential Info|If enabled, action will return information about credential information related to the entity.|False|Boolean|true|
|Create Insights|If enabled, action will create an insight containing all of the retrieved information about the entity.|False|Boolean|true|
|Max ThreatPaths To Return|Specify how many ThreatPaths to return per entity. Default: 50.|False|String|50|
|Max Vulnerabilities To Return|Specify how many vulnerabilities to return per entity. Default: 50.|False|String|50|
|Max Credentials To Return|Specify how many credentials to return per entity. Default: 50.|False|String|50|



#### List Service ThreatPaths
List ThreatPaths related to services in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Services|Specify a comma-separated list of services for which action needs to return ThreatPaths.|True|String||
|Max ThreatPaths To Return|Specify how many ThreatPaths to return. If nothing is provided, action will return 50 ThreatPaths.|False|String|50|



#### Update Event
Update event in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID of the event, which needs to be updated.|True|String||
|Status|Specify the status for the event.|False|List|Select One|
|Comment|Specify a comment that needs to be added to the event.|False|String||



#### List Critical ThreatPath
List available critical ThreatPaths in Attivo.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter critical paths.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|String|50|



#### Ping
Test connectivity to the Attivo with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds









## Connectors
#### Attivo - Events Connector
Pull events from Attivo into Siemplify. Note: whitelist works with attackName parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Attivo instance.|True|String|https:/{{ip address}}|
|Username|Attivo API Username.|True|String||
|Password|Attivo API Password.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Attivo server is valid.|False|Boolean|true|
|Lowest Severity To Fetch|Severity that will be used to fetch events. If nothing is specified, action will ingest all events. Possible values: System Activity, Very Low, Low, Medium, High, Very High.|False|String|Medium|
|Status Filter|Status filter for the connector. Possible values: unacknowledged, acknowledged, all.|True|String|All|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve events from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time.|False|Int|1|
|Max Events To Fetch|How many events to process per one connector iteration. Maximum is 1000. Default: 100.|False|Int|100|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





Read123!@#
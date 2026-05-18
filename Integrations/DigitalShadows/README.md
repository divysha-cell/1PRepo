
# DigitalShadows

Digital Shadows is designed to protect you from external threats, continually identifying where your assets are exposed, providing sufficient context to understand the risk, and options for remediation.


Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Key|None|True|String||
|Api Secret|None|True|Password||


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|requests-2.31.0-py3-none-any.whl|


## Actions
#### EnrichCVE
Enrich a CVE using Digital Shadows information.
Timeout - 600 Seconds



#### EnrichHash
Deprecated: Enrich a Hash using Digital Shadows information.
Timeout - 600 Seconds



#### EnrichURL
Enrich a Url using Digital Shadows information.
Timeout - 600 Seconds



#### EnrichIP
Deprecated: Enrich an Ip using Digital Shadows information.
Timeout - 600 Seconds



#### Ping
Test Connectivity
Timeout - 600 Seconds









## Connectors
#### Digital Shadows - Incident Connector
Connector ingest incidents from Digital Shadows into Siemplify.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|API Key|Digital Shadow API Key.|True|None||
|API Secret|Digital Shadow API Secret.|True|None||
|Lowest Severity To Fetch|Lowest severity that will be used to fetch findings. Possible values: VERY_HIGH, HIGH, MEDIUM, LOW, VERY_LOW, NONE|True|None|NONE|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|1|
|Incident Type Filter|Comma-separated list of incident types that should be ingested into Siemplify. By default connector pulls all of the incident types. Example: DATA_LEAKAGE,CYBER_THREAT. Possible Values: DATA_LEAKAGE, CYBER_THREAT, PHYSICAL_SECURITY, SOCIAL_MEDIA_COMPLIANCE, BRAND_PROTECTION, INFRASTRUCTURE.|False|None||
|Max Incidents To Fetch|How many incidents to process per one connector iteration.|False|None|50|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|None|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Digital Shadow server is valid.|False|None|true|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||





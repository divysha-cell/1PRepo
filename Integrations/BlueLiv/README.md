
# BlueLiv

Blueliv is Europe’s leading cyberthreat intelligence provider. It looks beyond your perimeter, scouring the open, deep and dark web to deliver fresh, automated and actionable threat intelligence to protect the enterprise and manage your digital risk.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String||
|User Name|None|True|String||
|Password|None|True|Password||
|Organization ID|None|True|String||
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|idna-3.8-py3-none-any.whl|
|filelock-3.16.0-py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|


## Actions
#### Ping
Test connectivity to the BlueLiv with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Add Comment to a Threat
The action will add a desired text comment to a specific threat. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Module Type|Specify the module type the resource belongs to|True|None||
|Module ID|Specify the module ID the resource belongs to|True|None||
|Resource ID|Specify the Resource ID to add the comment to|True|None||
|Comment Text|Provide the comment you would like to add to the resource|True|None||



#### Add Labels to Threats
The action will add the specified label name to the specified threat IDs
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Module Type|Specify the module type the resource belongs to|True|None||
|Module ID|Specify the module ID the resource belongs to|True|None||
|Resource ID|Specify the Resource IDs, as a comma separated list, to add the labels to|True|None||
|Label Names|Specify the label names you would like to apply to the specified threats, as a comma separated list. Please pay attention to lowercase and uppercase.|True|None||



#### Remove Labels From Threats
The action will remove the specified labels from the specified threat IDs.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Module Type|Specify the module type the resource belongs to.|True|None||
|Module ID|Specify the module ID the resource belongs to.|True|None||
|Resource ID|Specify a comma-separated list of  resource IDs from which you want to remove labels.|True|None||
|Label Names|Specify a comma-separated list of labels that need to be removed. Please pay attention to lowercase and uppercase.|True|None||



#### Mark Threat as a Favorite
The action will mark the specified threat as a favorite threat in BlueLiv
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Module Type|Specify the module type the resource belongs to|True|None||
|Module ID|Specify the module ID the resource belongs to|True|None||
|Resource ID|Specify the Resource ID to add the comment to|True|None||
|Favorite Status|Provide the Favorite status you would like to apply on the specified threat|True|None||



#### Enrich Entities
Enrich entities using information from Threat Context module of Blueliv. Supported entities: IP, Hash, URL, Threat Actor, Threat Campaign, Threat Signature, CVE. Note: only MD5, SHA1, SHA256 and SHA512 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insight|If enabled, action will create insights containing information about entities.|False|None||
|Lowest Score To Mark as Suspicious|Specify what should be the lowest score for the entity to be marked as suspicious. Maximum: 10.|True|None||



#### List Entity Threats
List threats related to entities in Blueliv. Supported entities: All.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Label Filter|Specify a comma-separated list of labels, that will be used to filter threats. Note: label filter works with "OR" logic.|False|None||
|Module Filter|Specify a comma-separated list of modules, that will be used to filter threats.|False|None||
|Max Threats To Return|Specify how many threats to return per entity. If nothing is specified action will return 50 threats.|False|None||









## Connectors
#### BlueLiv - Threats Connector
Pull security threats from BlueLiv. Connector fetches all of the latest threats from BlueLiv modules. Whitelist and blacklist filters work with BlueLiv module types. For example, if you want to get threats only from Hacktivism modules, you can turn on the whitelist and type in the Hacktivism type name.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|API URL|API Root of the BlueLiv instance.|True|None|https://example.blueliv.com/|
|User Name|User name for BlueLiv.|True|None||
|Password|User password for BlueLiv.|True|None||
|Organization ID|Specify the Organization ID to use in BlueLiv.|True|None||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the BlueLiv server is valid.|False|None|false|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve events from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|1|
|Max Threats To Fetch|How many threats to process per one connector iteration. Note - Maximum value here is 100.|False|None|10|
|Severity|Severity will be one from the following values Low, Medium, High, Critical. Will be assigned to Siemplify alerts created from this connector.|True|None|Medium|
|Analysis Results To Ingest|Filter the threats by the analyst analysis to this threat, only ingest threats with the chosen analysis result. Provide a comma separated list of the desired analysis results to ingest. Possible values: NOT_AVAILABLE, NOT_IMPORTANT, NOT_PROCESSABLE, POSITIVE, NEGATIVE, INFORMATIVE, IMPORTANT.|False|None||
|Labels To Filter By|Please provide a comma separated list of the label names you want to filter by. Please pay attention to uppercase and lowercase letters and write the labels exactly as they appear in BlueLiv UI.|False|None||
|Reading Status To Ingest|Filter the threats by their reading status, so that the connector will ingest according to it. If no value is provided we will fetch both. Options:  “Only Read”, “Only Unread”.|False|None||
|Should ingest only starred threats?|If checked, only starred (favorite) threats will be ingested.|False|None|false|
|Should ingest threats related to incidents?|Should connector filter the threats by checking the relationship to an incident. If no value is provided we will fetch both. Options are: Only Incidents - will ingest only threats related to incidents, Only Non Incidents - will ingest only threats that are not related to incidents.|False|None||
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||





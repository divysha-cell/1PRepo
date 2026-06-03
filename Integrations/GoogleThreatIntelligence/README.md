
# GoogleThreatIntelligence

Google Threat Intelligence (GTI) delivers comprehensive threat insights by combining Mandiant's expertise, Google's vast data resources, and VirusTotal's crowdsourced intelligence. By defending billions of users, seeing millions of phishing attacks, and spending hundreds of thousands of hours investigating incidents it has the visibility to see across the threat landscape to keep the most important organizations protected.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|The API root of the Google Threat Intelligence instance.|True|String|https://www.virustotal.com|
|API Key|The Google Threat Intelligence API key.|True|Password|*****|
|ASM Project Name|The Attack Surface Management (ASM) project name to use in the Google Threat Intelligence integration. This parameter is required to execute the ASM actions.|False|String||
|Verify SSL|If selected, the integration verifies that the SSL certificate for connecting to the Google Threat Intelligence server is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|proto_plus-1.25.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|cryptography-43.0.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|httpcore-1.0.5-py3-none-any.whl|
|google_api_core-2.22.0-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|urllib3-2.2.3-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|pycryptodome-3.20.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl|
|anyio-4.4.0-py3-none-any.whl|
|pycryptodomex-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.10-py3-none-any.whl|
|paramiko-3.5.0-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|pyzipper-0.3.6-py2.py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|google_auth-2.35.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.65.0-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|google_api_python_client-2.151.0-py2.py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|bcrypt-4.2.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cachetools-5.5.0-py3-none-any.whl|
|TIPCommon-2.2.2-py2.py3-none-any.whl|


## Actions
#### Download File
Use the Download File action to download a file from Google Threat Intelligence. This action runs on the Google SecOps Hash entity. This action supports the MD5, SHA-1, and SHA-256 hashes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Download Folder Path|The path to a folder to store the downloaded files, such as "/tmp/".|True|String||
|Overwrite|If selected, the action overwrites the file with the same name.|False|Boolean|true|



#### Execute IOC Search
Use the Execute IOC Search action to run the IOC search in Google Threat Intelligence.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search Query|A search query to execute, such as "crowdsourced_yara_rule:*apt* and p:3+ and fs:2d+".|True|String||
|Max Results To Return|The maximum number of results to return for every action run. The default value is 50. The maximum value is 200.|False|String|50|



#### Get Graph Details
Use the Get Graph Details action to obtain detailed information about graphs in Google Threat Intelligence. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Graph ID|A comma-separated list of graph IDs for which to retrieve information.|True|String||
|Max Links To Return|The maximum number of links to return. The default value is 50.|True|String|50|



#### Get Related IOCs
Use the Get Related IOCs action to obtain information about IOCs that are related to Google SecOps entities using information from Google Threat Intelligence. This action runs on the following Google SecOps entities: IP address, URL, Hostname, Domain, Hash, Threat Actor. This action only supports the MD5, SHA-1, and SHA-256.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IOC Types|A comma-separated list of IOCs to extract. The possible values are as follows: IP, Hash, URL, Domain, Threat Actors, Malware, Campaigns.|True|String|IP, Hash, URL, Domain|
|Max IOCs To Return|The maximum number of IOCs to return for selected IOC types  for every entity. The default value is 40.|True|String|40|



#### Private Submit URL
Use the Private Submit URL action to submit a URL for private scan in Google Threat Intelligence. For regular scan and enrichment use the action “Enrich Entities”. Supported Entities: URL.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URL|Comma-separated list of URLs that need to be scanned. Values from this parameter and entities will be processed together.|False|String||
|Check Existing Submissions First|If enabled, action will first check if there is any available information about the URL in public or private submissions. If it’s available, it will return the information without the submission flow.|False|Boolean|false|
|Resubmit After (Days)|The number of days that must elapse from the last public analysis for the URL to be eligible for resubmission.To use this parameter, “Check Existing Submissions First” must be enabled.|False|String|30|



#### Search ASM Entities
Use the Search ASM Entities action to search for Attack Surface Management (ASM) entities in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project Name|The name of the ASM project. If you don’t set a value, the action uses the value that you configured for the "ASM Project Name" integration parameter.|False|String||
|Entity Name|A comma-separated list of entity names for which to find related entities. The action treats entity names that contain forward slashes (/) as invalid names.|False|String||
|Minimum Vulnerabilities Count|The minimum number of vulnerabilities that the entity has for the action to return the entity.|False|String||
|Minimum Issues Count|The minimum number of issues that are related to the entity for the action to return the entity.|False|String||
|Tags|A comma-separated list of tag names to use when searching for entities.|False|String||
|Max Entities To Return|The maximum number of entities to return for every action run. The default value is 50. The maximum value is 200.|True|String|50|
|Critical or High Issue|If selected, the action only returns issues with High and Critical severity.|False|Boolean|false|



#### Search ASM Issues
Use the Search ASM Issues action to search for Attack Surface Management (ASM) issues in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project Name|The name of the ASM project. If you don’t set a value, the action uses the value that you configured for the "ASM Project Name" integration parameter.|False|String||
|Issue ID|A comma-separated list of issue IDs for which to obtain details.|False|String||
|Entity ID|A comma-separated list of entity IDs for which to find related issues.|False|String||
|Entity Name|A comma-separated list of entity names for which to find related issues. The action treats entity names that contain forward slashes (/) as invalid names.|False|String||
|Time Parameter|The time parameter to filter the results.|False|List|First Seen|
|Time Frame|A period to search for issues. If you select the "Custom" value, set the "Start Time" parameter. The default value is Last Hour.|False|List|Last Hour|
|Start Time|The start time to search for results. If you select "Custom" for the "Time Frame" parameter,  this parameter is required. To configure this parameter, set the start time in the ISO 8601 format.|False|String||
|End Time|The end time to search for results. If you don’t set a value and select "Custom" for the "Time Frame" parameter, this parameter uses the current time as end time value. To configure this parameter, set the end time in the ISO 8601 format.|False|String||
|Lowest Severity To Return|The lowest severity of the issues to return. The default value is Select One. If you use the default parameter value, this filter doesn’t apply to search.|False|List|Select One|
|Status|The status of the issues to return. The default value is Select One. If you use the default parameter value, this filter doesn’t apply to search.|False|List|Select One|
|Tags|A comma-separated list of tag names to use when searching for issues.|False|String||
|Max Issues To Return|The maximum number of issues to return for every action run. The default value is 50. The maximum value is 200.|True|String|50|



#### Search Graphs
Use the Search Graphs action to search for graphs that are based on custom filters in Google Threat Intelligence.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|A query filter for the graph. For example, to search for graphs in the selected period, format the query as follows: "creation_date:2018-11-1+creation_date:2018-11-12"|True|String||
|Sort Field|The value to sort the results. By default, the action sorts the results by last modified date.|False|List|Last Modified Date|
|Max Graphs To Return|The maximum number of graphs to return for a specified query. The default value is 10.|True|String|10|



#### Submit File
Use the Submit File action to submit a file and return results from Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|External URLs|A comma-separated list of public URLs for the files to submit. If both “External URL” and “File Paths” are provided, action will collect files from both inputs.|False|String||
|File Paths|A comma-separated list of absolute file paths. If you configure the “Linux Server Address” parameter, the action attempts to retrieve the file from a remote server. If both “External URL” and “File Paths” are provided, action will collect files from both inputs.|False|String||
|Check Hash First|If enabled, action will first calculate the hashes for the files and search, if there is any available information for it. If it’s available, it will return the information without the submission flow.|False|Boolean|false|
|GTI Score|GTI Score that is used to set is_risky property in JSON result to true. This condition is validated together with GTI verdict information. If nothing is provided, action will ignore the GTI score values.|False|String|60|
|Engine Threshold|The count of how many engines should mark the file as malicious or suspicious, for is_risky property in JSON result to be set to true. If “Engine Allowlist” contains values, action will only count results from those engines. This condition is validated together with GTI verdict information. If nothing is provided, action will ignore the Engines calculations.|False|String|None|
|Engine Percentage Threshold|The percentage of engines should mark the entity as malicious or suspicious, for is_risky property in JSON result to be set to true. If “Engine Allowlist” contains values, action will only count the percentage from those engines. If both “Engine Threshold” and “Engine Percentage Threshold” are provided, “Engine Threshold” will be used. Maximum value: 100. Minimum: 0. If nothing is provided, action will ignore the Engines calculations.|False|String|None|
|Engine Allowlist|Comma-separated list of engines that should be used to retrieve information, whether a file is malicious or not. Example: AlienVault,Kaspersky.If nothing is specified in this parameter, action will take results from every available engine. If the engine didn’t return any information about the file it’s not going to be counted for the parameters “Engine Threshold” and “Engine Percentage Threshold”.|False|String||
|Resubmit After (Days)|The number of days for the action to wait before resubmitting the file even if the hash is available for the file in the GTI database. To use this parameter, enable the “Check Hash First” parameter. The default value is 30 days.|False|String|30|
|Fetch MITRE Details|If selected, the action returns the information about the related MITRE techniques and tactics. This parameter only supports the Hash entity. Not selected by default.|False|Boolean|false|
|Lowest MITRE Technique Severity|The lowest MITRE technique severity to return. The action treats the "Unknown" severity as “Info”. This parameter only supports the Hash entity. The default value is Medium.|False|List|Medium|
|Private Submission|If selected, the action submits the file in a private mode.|False|Boolean|false|
|Retrieve Comments|If selected, the action retrieves comments about the entity. This parameter supports the following entities: URL, Domain, Hostname, Hash, and IP Address.|False|Boolean|true|
|Max Comments To Return|The maximum number of comments to return in every action run. The default value is 10.|False|String|10|
|Linux Server Address|Specify the IP address of the remote linux server, where the file is located.|False|String||
|Linux Username|Specify the username of the remote linux server, where the file is located.|False|String||
|Linux Password|Specify the password of the remote linux server, where the file is located.|False|Password|*****|
|ZIP Password|A password for the zipped folder that contains the files to submit.|False|Password|*****|



#### Update ASM Issue
Use the Update ASM Issue to update an Attack Surface Management (ASM) issue in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue ID|The ID of the issue to update.|True|String||
|Status|The new status to set for the issue. The default value is Select One. If you use the default value, the action fails.|True|List|Select One|



#### Add Comment To Entity
Use the Add Comment To Entity action to add comments to the Google SecOps entities in Google Threat Intelligence. This action runs on the following Google SecOps entities: File Hash, URL, Hostname, Domain, IP Address. This action supports the MD5, SHA-1, and SHA-256 hashes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|A comment to add to all supported entities.|True|String||



#### Update DTM Alert
Use the Update DTM Alert to update a Digital Threat Monitoring (DTM) alert in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|The ID of the alert to update.|True|String||
|Status|The new status to set for the alert. The default value is Select One. If you use the default value, the action fails.|False|List|Select One|



#### Add Tag To DTM Alert
Use the “Add Tag To DTM” to add tags to a Digital Threat Monitoring (DTM) alert in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|The ID of the alert to update.|True|String||
|Mode|Mode for the action execution. If “Append” is selected, action will add a new tag to the alert. If “Set” is selected, action will overwrite existing tags with the provided one in “Tags” parameter.|True|List|Append|
|Tags|Comma-separated list of tags that should be added to Alert.|True|String||



#### Add ASM Issue Note
Use the Add ASM Issue Note action to add a note for the Attack Surface Management (ASM) issue in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|The ID of the alert to update.|True|String||
|Text|Text of the analysis.|True|String||



#### Enrich IOCs
Use the Enrich IOCs action to enrich IOCs with information from Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IOC Type|The type of the IOC to enrich.|False|List|Filehash|
|IOCs|A comma-separated list of IOCs for which to ingest data.|True|String||
|Widget Theme|The theme of the augmented widget.|False|List|Chronicle|



#### Get Related Associations
Use the Get Related Associations action to get information about associations (reports, campaigns, IOC collections, malware families, software toolkits, vulnerabilities, threat actors) related to the provided entities in Google Threat Intelligence. Supported entities: IP, URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Association Types|A comma-separated list of associations to return. Possible values: Report, Campaign, Collections, Malware Family, Vulnerability, Threat Actor. If no value is provided, the action returns all associations. Note: Reports are processed after all other associations are complete.|False|String|Report, Campaign, Collection, Malware Family, Vulnerability, Threat Actor|
|Create Entity|If selected, the action creates an entity for related Threat Actors, CVEs and Campaigns, linking it to the original entity. Note: Only CVE, Threat Actor and Campaign entities are created.|False|Boolean|false|
|Max Associations To Return|The maximum number of IOCs to return for every entity. Max: 1000.|False|String|50|



#### Get ASM Entity Details
Use the Get ASM Entity Details action to obtain information about an Attack Surface Management (ASM) entity in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Entity ID|A comma-separated list of entity IDs for which to obtain details.|True|String||



#### Ping
Use the Ping action to test the connectivity to Google Threat Intelligence. This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds



#### Search Entity Graphs
Use the Search Entity Graphs action to search graphs that are based on Google SecOps entities in Google Threat Intelligence. This action runs on the following Google SecOps entities: IP, URL, Filehash, Hostname, Domain, Threat Actor, User. This action only supports the MD5, SHA-1, and SHA-256 hashes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sort Field|The value to sort the results. By default, the action sorts the results by owner.|False|List|Owner|
|Max Graphs To Return|The maximum number of graphs to return for a specified query. The default value is 10.|True|String|10|



#### Add Vote To Entity
Use the Add Vote To Entity action to add votes to the Google SecOps entities in Google Threat Intelligence. This action supports the following Google SecOps entities: File Hash, URL, Hostname, Domain, IP Address. This action supports the MD5, SHA-1, and SHA-256 hashes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vote|A vote to add to all supported entities.|True|List|Malicious|



#### Enrich Entities
Use the Enrich Entities action to enrich the Google SecOps entities using information from Google Threat Intelligence. This action runs on the following Google Secops entities: IP address, URL, Hostname, Domain, Hash, Threat Actor, CVE. This action supports only MD5, SHA-1, and SHA-256 hashes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|GTI Score|GTI Score that is used to set Google SecOps entities as suspicious. This condition is validated together with GTI verdict information. If nothing is provided, action will ignore the GTI score values. This parameter only supports IP address, URL, Hostname, Domain, Hash entities.|False|String|60|
|Engine Threshold|The count of how many engines should mark the entity as malicious or suspicious, for Google SecOps to label it as suspicious. If “Engine Allowlist” contains values, action will only count results from those engines. This condition is validated together with GTI verdict information. If nothing is provided, action will ignore the Engines calculations. This parameter only supports IP address, URL, Hostname, Domain, Hash entities.|False|String|None|
|Engine Percentage Threshold|The percentage of engines should mark the entity as malicious or suspicious, for Google SecOps to label it as suspicious. If “Engine Allowlist” contains values, action will only count the percentage from those engines. If both “Engine Threshold” and “Engine Percentage Threshold” are provided, “Engine Threshold” will be used. Maximum value: 100. Minimum: 0. If nothing is provided, action will ignore the Engines calculations. This parameter only supports IP address, URL, Hostname, Domain, Hash entities.|False|String|None|
|Engine Allowlist|Comma-separated list of engines that should be used to retrieve information, whether an entity is malicious or not. Example: AlienVault,Kaspersky.If nothing is specified in this parameter, action will take results from every available engine. If the engine didn’t return any information about the entity it’s not going to be counted for the parameters “Engine Threshold” and “Engine Percentage Threshold”.|False|String||
|Resubmit Entity|If selected, the action resubmits entities for analysis instead of using the information from the previous action run. This parameter only supports the URL and Hash entities. Not selected by default.|False|Boolean|false|
|Resubmit After (Days)|The number of days for the action to wait before resubmitting the entity. To use this parameter, enable the "Resubmit Entity" parameter. The default value is 30 days. This parameter only supports the URL and Hash entities.|False|String|30|
|Sandbox|A comma-separated list of sandbox names to analyze, such as VirusTotal Jujubox, VirusTotal ZenBox, Microsoft Sysinternals, Tencent HABO. This parameter only supports the Hash entity.If you don’t set this parameter, the action uses the default sandbox, VirusTotal Jujubox.|False|String|VirusTotal Jujubox|
|Retrieve Sandbox Analysis|If selected, the action retrieves the sandbox analysis for the entity and creates a separate section for every sandbox in the JSON result. The action returns data for sandboxes that you configured in the "Sandbox" parameter. This parameter only supports the Hash entity. Not selected by default.|False|Boolean|false|
|Fetch MITRE Details|If selected, the action returns the information about the related MITRE techniques and tactics. This parameter only supports the Hash entity. Not selected by default.|False|Boolean|false|
|Lowest MITRE Technique Severity|The lowest MITRE technique severity to return. The action treats the "Unknown" severity as “Info”. This parameter only supports the Hash entity. The default value is Medium.|False|List|Medium|
|Retrieve Comments|If selected, the action retrieves comments about the entity. This parameter supports the following entities: URL, Domain, Hostname, Hash, and IP Address.|False|Boolean|true|
|Max Comments To Return|The maximum number of comments to return in every action run. The default value is 10.|False|String|10|
|Widget Theme|The theme of the augmented widget.|False|List|Chronicle|



#### Set DTM Alert Analysis
Use the Set DTM Alert Analysis action to set an analysis for a Digital Threat Monitoring (DTM) alert in Google Threat Intelligence. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|The ID of the alert to update.|True|String||
|Text|Text of the analysis.|True|String||
|Attachment File Paths|Comma-separated list of attachment file paths. Note: only 10 files can be attached to the alert.|False|String||









## Connectors
#### Google Threat Intelligence - DTM Alerts Connector
Use the Google Threat Intelligence - DTM Alerts Connector to retrieve alerts from Google Threat Intelligence. The dynamic listworks with the "alert_type" parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|The name of the field where the environment name is stored. If the environment field isn't found, the environment is set to the default environment. The default value is "".|False|String||
|Environment Regex Pattern|A regular expression pattern to run on the value found in the "Environment Field Name" field. This parameter lets you manipulate the environment field using the regular expression logic.Use the default value ".*" to retrieve the|False|String|.*|
|API Root|The API root of the Google Threat Intelligence instance.|True|String|https://www.virustotal.com|
|API Key|The Google Threat Intelligence API key.|True|Password|*****|
|Verify SSL|If selected, the connector verifies that the SSL certificate for connecting to Google Threat Intelligence is valid.|False|Boolean|true|
|Lowest Severity To Fetch|The lowest severity of the alerts to fetch. If you don’t set a value, the connector ingests alerts with all severity levels. The possible values are as follows: Low, Medium, High.|False|String||
|Monitor ID Filter|A comma-separated list of monitor IDs from which to retrieve alerts. This parameter is applied alongside side Monitor Name values as OR filter.|False|String||
|Monitor Name Filter|A comma-separated list of monitor names from which to retrieve alerts. Note: if there are several monitors with the same name, connector will ingest from all of them. This parameter is applied alongside side Monitor ID values as OR filter.|False|String||
|Event Type Filter|A comma-separated list of event types that needs to be returned. If input is provided in format “!event_type”, then action will return all events except for the provided one. If nothing is provided, the connector will process all event types. Input is case sensitive.|False|String||
|Disable Overflow|If selected, the connector ignores the Google SecOps overflow mechanism during alert creation. Selected by default.|False|Boolean|true|
|Max Hours Backwards|The number of hours before the first connector iteration to retrieve responses from. This parameter applies either to the initial connector iteration after you enable the connector for the first time or the fallback value for an expired connector timestamp. The default value is 1 hour.|True|Int|1|
|Max Alerts To Fetch|The maximum number of alerts to process for every connector iteration. The default value is 25. The maximum value is 25.|True|Int|25|
|Use dynamic list as a blocklist|If selected, the connector uses th dynamic list as a blocklist. Not selected by default.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|


#### Google Threat Intelligence - ASM Issues Connector
Use the Google Threat Intelligence - ASM Issues Connector to retrieve information about the Attack Surface Management (ASM) issues from Google Threat Intelligence. The dynamic list filter works with the "category" parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Proxy Username|The proxy username to authenticate with.|False|String||
|Environment Field Name|The name of the field where the environment name is stored. If the environment field isn't found, the environment is set to the default environment. The default value is "".|False|String||
|Environment Regex Pattern|A regular expression pattern to run on the value found in the "Environment Field Name" field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value ".*" to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|The API root of the Google Threat Intelligence instance.|True|String|https://www.virustotal.com|
|API Key|The Google Threat Intelligence API key.|True|Password|*****|
|Project Name|The name of the ASM project.|False|String||
|Verify SSL|If selected, the connector verifies that the SSL certificate for connecting to Google Threat Intelligence is valid.|False|Boolean|true|
|Lowest Severity To Fetch|The lowest severity of the alerts to fetch. If you don’t set a value, the connector ingests alerts with all severity levels. The possible values are as follows: Informational, Low, Medium, High, Critical.|False|String||
|Disable Overflow|If selected, the connector ignores the Google SecOps overflow mechanism during alert creation. Selected by default.|False|Boolean|true|
|Issue Name Filter|Comma-separated list of names of issues that need to be ingested. If the input is provided as “!issue_name”, connector will ingest everything except for the provided issue. If nothing is provided, the connector will not apply this filter. Input is case sensitive.|False|String||
|Status Filter|Comma-separated list of issue statuses that need to be ingested. If nothing is provided, the connector will process only opened issues. Possible Values: Open, Closed.|False|String|Open|
|Max Hours Backwards|The number of hours before the first connector iteration to retrieve issues from. This parameter applies either to the initial connector iteration after you enable the connector for the first time or the fallback value for an expired connector timestamp. The default value is 1 hour.|True|Int|1|
|Max Issues To Fetch|The maximum number of issues to process for every connector iteration. The default value is 10. The maximum value is 100.|True|Int|10|
|Use dynamic list as a blocklist|If selected, the connector uses th dynamic list as a blocklist. Not selected by default.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|


#### Google Threat Intelligence - Livehunt Connector
Use the Google Threat Intelligence - Livehunt Connector to retrieve information about the Livehunt notifications and their related files from Google Threat Intelligence. The dynamic list works with the "rule_name" parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|The name of the field where the environment name is stored. If the environment field isn't found, the environment is set to the default environment. The default value is "".|False|String||
|Environment Regex Pattern|A regular expression pattern to run on the value found in the "Environment Field Name" field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value ".*" to retrieve the required raw Environment Field Name value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|The API root of the Google Threat Intelligence instance.|True|String|https://www.virustotal.com|
|API Key|The Google Threat Intelligence API key.|True|Password|*****|
|Verify SSL|If selected, the connector verifies that the SSL certificate for connecting to Google Threat Intelligence is valid.|False|Boolean|true|
|Max Hours Backwards|The number of hours before the first connector iteration to retrieve notifications from. This parameter applies either to the initial connector iteration after you enable the connector for the first time or the fallback value for an expired connector timestamp. The default value is 1 hour.|False|Int|1|
|Max Notifications To Fetch|The maximum number of notifications to process for every connector iteration. The default value is 40.|False|Int|40|
|Disable Overflow|If selected, the connector ignores the Google SecOps overflow mechanism during alert creation. Selected by default.|False|Boolean|true|
|Use dynamic list as a blocklist|If selected, the connector uses th dynamic list as a blocklist. Not selected by default.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





Read123!@#
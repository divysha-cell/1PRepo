
# Anomali

Anomali ThreatStream operationalizes threat intelligence, automating collection and integration, and enabling security teams to analyze and respond to threats.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|URL|https://api.threatstream.com/api|
|Username|None|True|String|user@domain.com|
|Api Key|None|True|Password|*****|


#### Dependencies
| |
|-|
|idna-3.8-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|


## Actions
#### Ping
Test connectivity to Anomali ThreatStream
Timeout - 600 Seconds



#### GetThreatInfo
Enrich entities using information from Anomali ThreatStream. Supported entities: IP, URL, Hash, Email Addresses (User entities that match email regex).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Limit|Specify how many records to return per entity.|True|String|10|
|Severity Threshold|Specify what should be the severity threshold for the entity, in order to mark it as suspicious. If multiple records are found for the same entity, action will take the highest severity out of all available records.|False|List|Medium|
|Confidence Threshold|Specify what should be the confidence threshold for the entity, in order to mark it as suspicious. Note: Maximum is 100. If multiple records are found for the entity, action will take the average. Active records have priority. Default: 50.|False|String|50|
|Ignore False Positive Status|If enabled, action will ignore the false positive status and mark the entity as suspicious based on the "Severity Threshold" and "Confidence Threshold". If disabled, action will never label false positive entities as suspicious, regardless, if they pass the "Severity Threshold" and "Confidence Threshold" conditions or not.|False|Boolean|false|



#### Get Related Associations
Retrieve entity related associations from Anomali ThreatStream.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Return Campaigns|If enabled, action will fetch related campaigns and details about them.|False|Boolean|true|
|Return Threat Bulletins|If enabled, action will fetch related threat bulletins and details about them.|False|Boolean|true|
|Return Actors|If enabled, action will fetch related actors and details about them.|False|Boolean|true|
|Return Attack Patterns|If enabled, action will fetch related attack patterns and details about them.|False|Boolean|true|
|Return Courses Of Action|If enabled, action will fetch related courses of action and details about them.|False|Boolean|true|
|Return Identities|If enabled, action will fetch related identities and details about them.|False|Boolean|true|
|Return Incidents|If enabled, action will fetch related incidents and details about them.|False|Boolean|true|
|Return Infrastructure|If enabled, action will fetch related infrastructure and details about them.|False|Boolean|true|
|Return Intrusion Sets|If enabled, action will fetch related intrusion sets and details about them.|False|Boolean|true|
|Return Malware|If enabled, action will fetch related malware and details about them.|False|Boolean|true|
|Return Signatures|If enabled, action will fetch related signatures and details about them.|False|Boolean|true|
|Return Tools|If enabled, action will fetch related tools and details about them.|False|Boolean|true|
|Return TTPs|If enabled, action will fetch related TTPs and details about them.|False|Boolean|true|
|Return Vulnerabilities|If enabled, action will fetch related vulnerabilities and details about them.|False|Boolean|true|
|Create Campaign Entity|If enabled, action will create an entity out of available "Campaign" associations.|False|Boolean|false|
|Create Actors Entity|If enabled, action will create an entity out of available "Actor" associations.|False|Boolean|false|
|Create Signature Entity|If enabled, action will create an entity out of available "Signature" associations.|False|Boolean|false|
|Create Vulnerability Entity|If enabled, action will create an entity out of available "Vulnerability" associations.|False|Boolean|false|
|Max Associations To Return|Specify how many associations to return per type. Default: 5|False|String|5|










Read123!@#

# Netskope

The Netskope Security Cloud helps the world’s largest organizations take full advantage of the cloud and web without sacrificing security.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://{IP}|
|V1 Api Key|None|False|Password|*****|
|V2 Api Key|None|False|Password|*****|
|Client ID|None|False|String|None|
|Client Secret|None|False|Password|*****|
|Verify SSL|None|False|Boolean|False|


#### Dependencies
| |
|-|
|idna-3.7-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|netskopesdk-0.0.41-py3-none-any.whl|


## Actions
#### Add Entities to URL List
Use the “Add Entities To URL List” action to append new URLs, domains, or IP addresses to an existing Netskope URL list. Supported Entities: URL, Domain, IP Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URL List Name|The name of the existing Netskope URL list to update (such as Allowed URLs).|True|String||
|Entries|A comma-separated list of URLs, domains, or IP addresses to add to the list. The action also automatically processes URL, Domain, and IP Address entities attached to the case.|False|String||
|Deploy URL List Changes|If selected, the action deploys all pending changes to all URL lists. Note: All changes across all URL lists are deployed.|False|Boolean|false|



#### List Alerts
List alerts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|This acts as a filter for all the cloud app events in the alerts database.|False|String||
|Type|The type of the alert to filter by. Valid values: anomaly | 'Compromised Credential' | policy | 'Legal Hold' | malsite | Malware | DLP | watchlist | quarantine | Remediation.|False|String||
|Time Period|Time period to search alerts at (milliseconds backwards). Valid Values: 3600 | 86400 | 604800 | 2592000.|False|String||
|Start Time|Restrict alerts to those that have timestamps greater than this (unixtime). Needed only if time period is not passed.|False|String||
|End Time|Restrict alerts to those that have timestamps less than this (unixtime). Needed only if time period is not passed.|False|String||
|Is Acknowledged|Whether to get only acknowledged alerts.|False|Boolean||
|Limit|Number of results to return. Default: 100.|False|String||



#### Download File
Download a quarantined file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File ID|ID of a file, needed to identify a file.|True|String||
|Quarantine Profile ID|ID of a quarantine profile. This parameter is mandatory for V1 API.|False|String||
|Use V2 API|If enabled, the action will use the V2 API endpoint (requires credentials).|False|Boolean|false|



#### Block File
Block a quarantined file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File ID|ID of a file, needed to identify a file.|True|String||
|Quarantine Profile ID|ID of a quarantine profile. This parameter is mandatory for V1 API.|False|String||
|Use V2 API|If enabled, the action will use the V2 API endpoint (requires credentials).|False|Boolean|false|



#### List Clients
List clients.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|This acts as a filter on all the entries in the database.|False|String||
|Limit|Number of results to return. Default: 25.|False|String||
|Use V2 API|If enabled, the action will use the V2 API endpoint (requires credentials).|False|Boolean|false|



#### Ping
Test connectivity to Netskope.
Timeout - 600 Seconds



#### List Quarantined Files
List quarantined files.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Start Time|Restrict events to those that have timestamps greater than this (unixtime). Needed only if time period is not passed.|False|String||
|End Time|Restrict events to those that have timestamps less than this (unixtime). Needed only if time period is not passed.|False|String||
|Max Items To Return|Maximum number of items to retrieve. If unspecified, the maximum (100) is used.|False|String||
|Use V2 API|If enabled, the action will use the V2 API endpoint (requires credentials).|False|Boolean|false|



#### List Events
List events.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|This acts as a filter for all the cloud app events in the events database.|False|String||
|Type|The type of the alert to filter by. Valid values: page | application | audit | infrastructure.|False|String||
|Time Period|Time period to search events at (milliseconds backwards). Valid Values: 3600 | 86400 | 604800 | 2592000.|False|String||
|Start Time|Restrict events to those that have timestamps greater than this (unixtime). Needed only if time period is not passed.|False|String||
|End Time|Restrict events to those that have timestamps less than this (unixtime). Needed only if time period is not passed.|False|String||
|Limit|Number of results to return. Default: 100.|False|String||



#### Allow File
Allow a quarantined file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File ID|ID of a file, needed to identify a file.|True|String||
|Quarantine Profile ID|ID of a quarantine profile. This parameter is mandatory for V1 API.|False|String||
|Use V2 API|If enabled, the action will use the V2 API endpoint (requires credentials).|False|Boolean|false|



#### Deploy URL List Changes
Use the “Deploy URL List Changes” action to push pending configurations to the active policy engine, ensuring that any staged updates are applied and enforced for URL Lists.
Timeout - 600 Seconds










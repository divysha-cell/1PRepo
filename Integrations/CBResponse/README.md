
# CBResponse

Highly scalable, real-time EDR with unparalleled visibility for top security operations centers and incident response teams

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|IP_OR_HOST||
|Api Key|None|True|Password||
|Version|None|True|String||
|CA Certificate File|CA certificate file to use with the verify_ssl option. Certificate file should be specified as a Base64-encoded string.|False|String||
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|types_python_dateutil-2.9.0.20240316-py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|zipp-3.18.1-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|requests-2.31.0-py3-none-any.whl|


## Actions
#### Binary Free Query
List binaries by free query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|e.g. md5:* AND original_filename:<file-name>|True|None||



#### Create Watchlist
Create a watchlist for processes (type = events) or for binaries (type = modules)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Watchlist Name|Name of this watchlist|True|None||
|Query|The raw Carbon Black query that this watchlist matches|True|None||
|Watchlist Type|The type of watchlist. e.g. modules|True|None||



#### Enrich Process
Enrich process entity with data from CB Response
Timeout - 600 Seconds



#### Get FileMod Data For Process
Get filemod data for a process by its id
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Process ID|process unique id|True|None||
|Segment Id|e.g. 1|True|None||



#### Block Hash
Block a hash
Timeout - 600 Seconds



#### Enrich Binary
Enrich hash with binary info from CB Response.
Timeout - 600 Seconds



#### Isolate Host
Isolate an endpoint from the network
Timeout - 600 Seconds



#### List Processes
List processes that are related to given entities
Timeout - 600 Seconds



#### Get System Info
Get  system information for a sensor from CB Response and enrich  entity
Timeout - 600 Seconds



#### Get Process Tree Data
Get process tree data for process by id (JSON)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Process ID|process unique id|True|None||
|Segment Id|e.g. 1|True|None||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Download Binary
Download a binary
Timeout - 600 Seconds



#### Unblock Hash
Unblock a hash
Timeout - 600 Seconds



#### Unisolate Host
Rejoin an endpoint to the network
Timeout - 600 Seconds



#### Kill Process
Kill a process on a particular host
Timeout - 600 Seconds



#### Resolve Alert
Resolve an alert. Note: Carbon Black Response REST-API returns a successful answer even if the alert that you tried to resolve doesn’t exist.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|The id of the alert to resolve|True|None||



#### Get License
Get the current license from CB Response
Timeout - 600 Seconds



#### Hosts By Process
Get hosts that are related to a particular process
Timeout - 600 Seconds



#### Process Free Query
List processes by free query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|e.g. process_name:python.exe|True|None||









## Connectors
#### Carbon Black Response Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|https://x.x.x.x|True|None||
|Api Key|Api Key|True|None||
|Version|CB server version, default 6.3 will be used|True|None|6.3|
|Alerts Count Limit|Limit the number of alerts in every cycle. e.g. 20.|True|None|20|
|Max Days Backwards|Number of days before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|None|3|
|Environment Field Name|The name of the environment's field.|False|None||
|List Type|Can be whitelist or blacklist.|False|None||
|List Operator|Can be 'exact', 'start with', 'ends with' or 'contains'.|False|None||
|List Fields|List of fields, comma separated.|False|None||
|CA Certificate File|CA certificate file to use with the verify_ssl option. Certificate file should be specified as a Base64-encoded string.|False|None||
|Verify SSL|Whether to verify ssl certificate on connection or not|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||






# AlienVaultAppliance

USM Appliance includes the essential security capabilities and continuously delivered threat intelligence needed to quickly and easily identify and respond to threats in your physical and virtual infrastructure.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|IP_OR_HOST|https://<instance>.alienvault.com|
|Username|None|True|String||
|Password|None|True|Password|*****|


#### Dependencies
| |
|-|
|pytz-2024.1-py2.py3-none-any.whl|
|dateparser-1.2.0-py2.py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|simplejson-3.19.2-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|six-1.16.0-py2.py3-none-any.whl|
|tzlocal-5.2-py3-none-any.whl|
|regex-2024.4.16-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|soupsieve-2.5-py3-none-any.whl|


## Actions
#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Get Vulnerability Reports
Get environment vulnerability report files
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Number Of Files To Fetch|e.g. 10|True|String||



#### Enrich Vulnerabilities
Retrieve information about vulnerabilities from AlienVault USM Appliance
Timeout - 600 Seconds



#### Fetch Last PCAP Files
Fetch last PCAP files from AlienVault
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Number Of Files To Fetch|e.g. 10|True|String||



#### Enrich Assets
Retrieve information about assets from AlienVault USM Appliance
Timeout - 600 Seconds



#### Get PCAP Files For Events
Get PCAP files for events in an alert
Timeout - 600 Seconds









## Connectors
#### AlienVault USM Appliance Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|e.g. https://<instance>.alienvault.com|True|String||
|Username|Username|True|String||
|Password|Password|True|Password|*****|
|Max Events Per Alert|Limit the number of events per alert. e.g. 10|True|Int|10|
|Max Days Backwards|This field is used in the connector first running cycle and determine the connector start time. e.g. 3|True|Int|1|
|Max Alerts Per Cycle|Limit the number of alerts in every cycle. e.g. 10|True|Int|10|
|Server Timezone|The timezone configured in the AlienVault's, ex. UTC, Asia/Jerusalem etc.|True|String|UTC|
|Environment Field Name|The name of the environment's field. e.g. AlienVault Sensor|False|String||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





Read123!@#
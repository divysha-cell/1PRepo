
# Cuckoo

Cuckoo Sandbox is an advanced, extremely modular, and 100% open source automated malware analysis system with infinite application opportunities. Cuckoo provides you all the requirements to easily integrate the sandbox into your existing framework and backend in the way you want, with the format you want, and all of that without licensing requirements.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root||True|IP_OR_HOST|http://x.x.x.x:8090|
|Web Interface Address||True|IP_OR_HOST|http://x.x.x.x:8000|
|Warning Threshold||True|Int|5.0|
|CA Certificate File||False|String||
|API Token||False|Password|*****|
|Verify SSL||False|Boolean|False|


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|requests-2.32.4-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|


## Actions
#### Detonate Url
Send a URL for analysis and get a report (async)
Timeout - 600 Seconds



#### Detonate File
Submit a file for analysis and get a report (async)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Paths|The path of the file to submit|True|String||



#### Get Report
Get report of a particular task by id (async)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Task ID|The task's id. e.g. 10|True|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds










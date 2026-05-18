
# McAfeeTIEDXL

McAfee Threat Intelligence Exchange optimizes threat detection and response by closing the gap from malware encounter to containment from days, weeks, and months down to milliseconds.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server Address|None|True|IP_OR_HOST||
|Broker CA Bundle Path|None|True|String||
|Client Cert File Path|None|True|String||
|Client Key File Path|None|True|String||


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|oscrypto-1.3.0-py2.py3-none-any.whl|
|certifi-2024.6.2-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|asn1crypto-1.5.1-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|msgpack-1.0.8-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|dxlclient-5.6.0.0-py2.py3-none-any.whl|
|dxlbootstrap-0.2.2-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|types_python_dateutil-2.9.0.20240316-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|configobj-5.0.8-py2.py3-none-any.whl|
|dxltieclient-0.3.0-py2.py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|PySocks-1.7.1-py3-none-any.whl|


## Actions
#### Get File Reputation
Get file reputation
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enrich with all services|If checked, enrich with all results from all returned services. Else, store only the worst reputation as enrichment.|False|None||



#### Ping
Test connectivity
Timeout - 600 Seconds



#### Get File References
Get references for a file (the agent on which the file was used)
Timeout - 600 Seconds



#### Set File Reputation
Set a file's enterprise reputation
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Trust Level|The trust level to set to the file's reputation|True|None||
|File Name|The name of the file|False|None||
|Comment|The comment to add to the file's reputation|False|None||










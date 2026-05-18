
# CheckPointSandBlast

Protect your organization from zero-day cyber attacks with SandBlast Network, the marketâ€™s leading advanced network threat prevention solution. Increase productivity while creating a secure environment with innovative technologies like threat emulation, threat extraction and artificial intelligence.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String||
|API Key|None|True|Password||
|Verify SSL|None|False|Boolean||


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


## Actions
#### Ping
Test connectivity to the Check Point SandBlast with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Upload File
Upload files for analysis
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Path|The full path of the file to upload. For multiple, use comma separated values.|True|None||
|Enable Threat Emulation feature|If enabled, threat emulation feature will be enabled for the upload. By default, if no features are selected, threat emulation will be used.|False|None||
|Enable AntiVirus feature|If enabled, antivirus feature will be enabled for the upload. By default, if no features are selected, threat emulation will be used.|False|None||
|Enable Threat Extraction feature|If enabled, threat extraction feature will be enabled for the upload. By default, if no features are selected, threat emulation will be used.|False|None||



#### Query
Get threat reputation information about FILEHASH entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threshold|Mark entity as suspicious if severity is equal or above the given threshold.|True|None||










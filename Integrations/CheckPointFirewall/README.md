
# CheckPointFirewall

VPN-1 is a firewall and VPN product developed by Check Point Software Technologies Ltd. VPN-1 is a stateful firewall which also filters traffic by inspecting the application layer.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server Address|None|True|IP||
|Username|None|True|String||
|Domain|None|False|String||
|Password|None|True|Password||
|Policy Name|None|True|String||
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|idna-3.7-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|charset_normalizer-3.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|chardet-5.2.0-py3-none-any.whl|


## Actions
#### Add Ip To Group
Add IP to the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Blacklist Group Name|Specify the name of the group to which you want to add IP address.|True|None||



#### Download Log Attachment
Download log attachments from CheckPoint FireWall.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Log IDs|Specify the comma-separated list of log IDs from which you want to download attachments.|True|None||
|Download Folder Path|Specify the absolute path for the folder where the action should store the attachments.|True|None||
|Create Case Wall Attachment|If enabled, action will create a case wall attachment for each successfully downloaded file. Note: that attachment will only be created if it’s size is less than 3 MB.|False|None||



#### List Policies On Site
Retrieve all existing policies
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Policies To Return|Specify how many policies to return in the response. Default: 50.|False|None||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Remove SAM Rule
Remove a SAM (suspicious activity monitoring) rule from Checkpoint Firewall. Note: you need to match the current rule in order to remove it. Please refer to the Checkpoint fw_sam command criteria section documentation for available ip, netmask, port and protocol combinations - https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_CLI_ReferenceGuide/Topics-CLIG/MDSG/fw-sam.htm
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Security Gateway|Specify the name of Security Gateway from where to remove SAM Rule|True|None||
|Source IP|Specify the source IP to be added to the rule.|False|None||
|Source Netmask|Specify the source netmask to be added to the rule.|False|None||
|Destination IP|Specify the destination IP to be added to the rule.|False|None||
|Destination Netmask|Specify the destination netmask to be added to the rule.|False|None||
|Port|Specify the port number to be added to the rule for example, 5005|False|None||
|Protocol|Specify the protocol name to be added to the rule for example, TCP|False|None||
|Action for the Matching Connections|Specify the action that should be executed for the matching connections.|True|None||
|How to Track Matching Connections|Specify how to track matching connections.|True|None||
|Close Connections|Specify if the existing matching connections should be closed.|False|None||



#### Remove Url From Group
Remove URL from the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URLs Group Name|Specify the name of the group from which you want to remove URL.|True|None||



#### Add Url To Group
Add Url to the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URLs Group Name|Specify the name of the group to which you want to add URL.|True|None||



#### Show Logs
Retrieve logs from CheckPoint FireWall based on the filter.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query Filter|Specify the query filter that will be used to return logs.|False|None||
|Time Frame|Specify what time frame should be used for log retrieval.|True|None||
|Log Type|Specify what type of logs should be returned.|True|None||
|Max Logs To Return|Specify how many logs to return. Maximum is 100. This is Checkpoint FireWall limitation.|False|None||



#### List Layers On Site
Retrieve all of the available Access Control and Threat Prevention layers
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Layers To Return|Specify how many layers to return in the response. Default: 50.|False|None||



#### Remove IP From Group
Remove IP from the Checkpoint FireWall Group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Blacklist Group Name|Specify the name of the group from which you want to remove IP address.|True|None||



#### Add a SAM Rule
Add a SAM (suspicious activity monitoring) rule for Checkpoint Firewall. Please refer to the Checkpoint fw_sam command criteria section documentation for available ip, netmask, port and protocol combinations - https://sc1.checkpoint.com/documents/R80.40/WebAdminGuides/EN/CP_R80.40_CLI_ReferenceGuide/Content/Topics-CLIG/MDSG/fw-sam.htm
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Security Gateway to Create SAM Rule on|Specify the name of Security Gateway to create a rule for.|True|None||
|Source IP|Specify the source IP to be added to the rule.|False|None||
|Source Netmask|Specify the source netmask to be added to the rule.|False|None||
|Destination IP|Specify the destination IP to be added to the rule.|False|None||
|Destination Netmask|Specify the destination netmask to be added to the rule.|False|None||
|Port|Specify the port number to be added to the rule for example, 5005|False|None||
|Protocol|Specify the protocol name to be added to the rule for example, TCP|False|None||
|Expiration|Specify how long in seconds the newly added SAM rule should be active for example, 4. If nothing is specified - then the rule never expires.|False|None||
|Action for the Matching Connections|Specify the action that should be executed for the matching connections.|True|None||
|How to Track Matching Connections|Specify how to track matching connections.|True|None||
|Close Connections|Specify if the existing matching connections should be closed.|False|None||



#### Run Script
Run arbitrary script with CheckPoint run-script API call. Note: action is not using Siemplify entities to operate.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Script text|Script to execute. For example, fw sam command: fw sam -t 600 -I src 8.9.10.12|True|None||
|Target|Specify CheckPoint device to execute script on, for example: gaia80.10. Parameter accepts multiple values as a comma separated list.|True|None||










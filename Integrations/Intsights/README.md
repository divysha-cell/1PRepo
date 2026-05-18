
# Intsights

The only all-in-one external threat protection platform designed to neutralize cyberattacks outside the wire.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String||
|Account ID|None|True|String||
|Api Key|None|True|Password||
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|idna-3.8-py3-none-any.whl|
|TIPCommon-1.0.12-py2.py3-none-any.whl|
|types_python_dateutil-2.9.0.20240906-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|


## Actions
#### Download Alert CSV
Download CSV file containing information related to alert in IntSights.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert for which you want to download CSV.|True|None||
|Download Folder Path|Specify the path to the folder, where you want to store the CSV file.|True|None||
|Overwrite|If enabled, action will overwrite the file with the same name.|False|None||



#### Search IOCs
Search IOCs
Timeout - 600 Seconds



#### Ping
Check connectivity
Timeout - 600 Seconds



#### Close Alert
Close alert in IntSights.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert which you want to close.|True|None||
|Additional Info|Specify additional information explaining why the alert should be closed.|False|None||
|Rate|Specify the rating of the alert. Maximum is 5.|False|None||
|Reason|Specify the reason why the alert needs to be closed.|True|None||



#### Assign Alert
Assign alert to an analyst in IntSights.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert on which you want to change the assignment.|True|None||
|Assignee ID|Specify the ID of the analyst that should be assigned to the alert. Note: If both Assignee ID and Assignee Email Address are specified, action will prioritize Assignee ID.|False|None||
|Assignee Email Address|Specify the email address of the analyst that should be assigned to the alert. Note: If both Assignee ID and Assignee Email Address are specified, action will prioritize Assignee ID.|False|None||



#### Ask An Analyst
Ask an analyst regarding the alert in IntSights.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert where you want to ask the analyst.|True|None||
|Comment|Specify the comment for the analyst.|True|None||



#### Get Alert Image
Retrieve information about alert images in IntSights.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Image IDs|Specify the comma-separated list of alert image IDs. Example: id1,id2.|True|None||



#### Reopen Alert
Reopen alert in IntSights.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert which you want to reopen.|True|None||



#### Add Note
Add a note to the alert in IntSights.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert to which you want to add a note.|True|None||
|Note|Specify the note for the alert.|True|None||









## Connectors
#### Intsights Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|The api root of the Intsights server|True|None|https://api.intsights.com|
|Account ID|The account ID to login with|True|None||
|Api Key|The API key to login with.|True|None||
|Verify SSL|Whether to verify the SSL certificate of the server|False|None|FALSE|
|Max Days Backwards|Number of days before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|None|3|
|Max Alerts Per Cycle|Max number of alerts to fetch per single connector cycle|True|None|10|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||





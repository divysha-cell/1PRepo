
# ConnectWise

Seamlessly transition projects and tasks to keep your communication flowing without ever worrying about accountability and visibility.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|URL||
|Company Name|None|True|String||
|Public Key|None|True|String||
|Private Key|None|True|Password||
|Client Id|None|True|String||


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|requests-2.31.0-py3-none-any.whl|


## Actions
#### Get Ticket
Get ConnectWise ticket by ID and attach ticket JSON as a file
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|Fetch ticket by ID|True|None||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Close Ticket
Close ConnectWise ticket
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|ConnectWise ticket id. e.g. 608718|True|None||
|Custom Close Status|If the specific system use a custom closed status (e.g. Completed)|False|None||



#### Delete Ticket
Delete ConnectWise ticket by ID
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|Ticket ID to be deleted. e.g. 607167|True|None||



#### Add Comment To Ticket
Add new comment to a ticket in ConnectWise
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|ConnectWise ticket id. e.g. 608718|True|None||
|Comment|Comment content to attach to a ticket|True|None||
|Internal|If checked, put comment in internal section|False|None||



#### Create Ticket
Create a ConnectWise ticket
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Company|Company identifier|True|None||
|Owner Name|ConnectWise member name to assign this ticket to, e.g. connectwise_user_1.|False|None||
|Board|Board name|True|None||
|Summary|Specify the summary for the new ticket. Note: if the summary is more than 100 characters, it will be truncated.|True|None||
|Status|e.g. Unassigned|True|None||
|Priority|e.g. Priority 3 - Normal Response|True|None||
|Email Note CC|Specify a comma-separated list of email addresses that should receive all of the notes via email.|False|None||



#### Create Alerts Ticket
Create a ConnectWise ticket for each new Siemplify alert
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Company|Company identifier|True|None||
|Owner Name|ConnectWise member name to assign this ticket to, e.g. connectwise_user_1.|False|None||
|Board|Board name|True|None||
|Status|e.g. Unassigned|True|None||
|Priority|e.g. Priority 3 - Normal Response|True|None||
|Initial Description|Initial Description|True|None||



#### Update Ticket
Update ticket details in ConnectWIse
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Ticket Id|Ticket ID to be updated. e.g. 609620|True|None||
|Summary|Specify the summary for the updated ticket. Note: if the summary is more than 100 characters, it will be truncated.|False|None||
|Type Name|e.g. Application|False|None||
|SubType Name|e.g. Adobe|False|None||
|Item Name|e.g. Development|False|None||
|Owner Name|ConnectWise member name to assign this ticket to, e.g. connectwise_user_1.|False|None||
|Board|Board name.|False|None||
|Priority|e.g. Priority 3 - Normal Response.|False|None||
|Status|New ticket status, e.g. In Progress (plan of action)|False|None||
|Email Note CC|Specify a comma-separated list of email addresses that should receive all of the notes via email.|False|None||



#### Add Attachment To Ticket
Add an attachment to the ticket in ConnectWise.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Allow Only Owner Update|If enabled, action will only allow the owner to update the attachment.|False|None||
|Display In Customer Portal|If enabled, attachment will be shown in the customer portal.|False|None||
|Filename|Specify the filename behind the attachment. This value will be also used as a title. Note: action needs to provide the correct extension for the file.|True|None||
|Base64 Encoded File|Specify the base64 encoded file that needs to be added as an attachment.|True|None||
|Ticket ID|Specify the ID of the ticket to which the document would need to be added.|True|None||










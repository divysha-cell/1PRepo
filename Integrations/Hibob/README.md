
# Hibob

Hibob integration facilitates the centralized management and synchronization of the company's employees information stored in the HR system called Hibob.
Bob is a cloud-based human resources (HR) management and benefits administration platform for HR teams, CEOs, and accountants.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Token|API Token|True|Password||


#### Dependencies
| |
|-|
|certifi-2025.6.15-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|urllib3-2.5.0-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Get User Image
Get the image base64 and URL for a specific employee
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Employee's Email|The employee's email you want to upload a photo.|True|None||



#### Enrich Entities
Enrich entities with Hibob properties
Timeout - 600 Seconds



#### Search User
Search if a specific user exists in Hibob
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Employee's Email|The employee's email to check if it exists|True|None||



#### Revoke Access
Disabling a given employee in Hibob based on his email address
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Employee's Email|The email of the employee you want to disable the access to Hibob|True|None||



#### Send Invitation
Sending an invitation to a new employee in order to invite them to log in the Hibob system for the first time or reinvite the user after he was disabled
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Employee's Email|The email of the employee that you want to send the invitation in order to start using Hibob system.|True|None||
|Welcome Wizard Name|The wizard name found in Hibob (Setting-> Flows), for example: "Welcome!". Please note: this is case sensitive!|True|None||



#### Upload User Image
Uploading an image (URL image) to a specific employee
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Employee's Email|The email of the employee that you want to upload an image to.|True|None||
|Url Image|The employee URL image|True|None||



#### Ping
Testing the connectivity with Hibob 
Timeout - 600 Seconds










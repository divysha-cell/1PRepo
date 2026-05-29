
# ActiveDirectory

Microsoft Active Directory integration facilitates the centralized management and synchronization of Windows user accounts with Security Center's administrator and cardholder accounts.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server|None|True|String|x.x.x.x|
|Username|None|True|String|user@domain.com|
|Domain|None|True|String|domain.com|
|Password|None|True|Password|*****|
|Custom Query Fields|None|False|String||
|CA Certificate File - parsed into Base64 String|None|False|String||
|Use SSL|None|False|Boolean|False|


#### Dependencies
| |
|-|
|idna-3.8-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|types_python_dateutil-2.9.0.20240821-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|ldap3-2.9.1-py2.py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|


## Actions
#### Disable account
Disable the user account 
Timeout - 600 Seconds



#### Is User In Group
Check whether a user is a member of a specific group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|GroupName|Group name to be checked. e.g. Administrators. Please make sure group name is spelled correctly, and exists in Active Directory.|True|String||



#### Add User To Group
Add user to groups.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|Specify a comma-separated list of groups to which action should add users.|True|String|None|



#### Remove User From Group
Remove user from groups.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|Specify a comma-separated list of groups from which action should remove users.|True|String|None|



#### Change User OU
Change a user's Organizational Unit (OU)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|OU Name|The name of the new user's OU|True|String|None|



#### Update attributes of an AD User
Update attributes of an existing Active Directory users.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|The name of the attribute to update. Default: Description.|True|String|Description|
|Attribute Value|The attribute value to update.|True|String|None|



#### Get Group Members
Get the members list of the provided group name in Active Directory
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|Specify whether the name of the group of which you would like to list down the group members.|True|String||
|Members Type|Specify the member type of the group.|True|List|User|
|Perform Nested Search|Specify whether the action should fetch additional details regarding groups found in the main group.|False|Boolean|false|
|Limit|Specify the maximum number of listings to fetch from Active Directory|True|String|100|



#### Enable account
Enable the user account
Timeout - 600 Seconds



#### Get Manager Contact Details
Get manager's contact details from active directory
Timeout - 600 Seconds



#### Search Active Directory
Search Active Directory with Siemplify, using your personal query.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query String|Specify the query string you would like to perform in AD.|True|String||
|Limit|Specify the maximum number of listings to fetch from Active Directory.|False|String||



#### Set User Password
Set a user's password
Note - For this action, please make sure to have a verified SSL connection and a strong password that will match the password rules in your organization
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|New Password|New Password|True|Password|*****|



#### Enable computer
Enable a computer account
Timeout - 600 Seconds



#### Enrich entities
Enrich Hostname or Username entities with Active Directory properties
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mark entities as internal|Specify whether successfully enriched entities should be automatically marked as “Internal Entity”|False|Boolean|false|
|Specific Attribute Names To Enrich With|Provide a comma separated list of attribute names to enrich the entities with. If nothing is provided - action will enrich with all available attributes. If an attribute contains a few values - it will be enriched with all of the available values. Parameter is case sensitive.|False|String||
|Should Case Wall Table be filtered by the specified Attributes?|If checked, the Case Wall Table for this action will only present the specified attributes, found in the “Specific Attribute Names To Enrich With” parameter.|False|Boolean|false|
|Should JSON result be filtered by the specified Attributes?|If checked, the JSON result for this action will only return the specified attributes, found in the “Specific Attribute Names To Enrich With” parameter.|False|Boolean|false|



#### Change Host OU
Change a Host's Organizational Unit (OU)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|OU Name|The name of the new user's OU|True|String|None|



#### Force password update
Force user password update on the next logon
Timeout - 600 Seconds



#### List User Groups
Get list of all users groups in Active Directory
Timeout - 600 Seconds



#### Release Locked Account
Release locked account
Timeout - 600 Seconds



#### Disable computer
Disable a computer account
Timeout - 600 Seconds



#### Ping
Test Active Directory connectivity
Timeout - 600 Seconds



#### Update attributes of an AD Host
Update attributes of an existing Active Directory hosts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|The name of the attribute to update. Default: Description.|True|String|Description|
|Attribute Value|The attribute value to update.|True|String|None|










Read123!@#

# GSuite

G Suite is a brand of cloud computing, productivity and collaboration tools, software and products developed by Google.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Verify SSL|If enabled, the server-side certificate used for connection is validated.|False|Boolean||
|Service Account JSON|For the service account based authentication, specify the Service Account JSON. Parameter accepts two ways to provide the service account: First (recommended), the full JSON content of the service account can be provided. The second way (legacy, will be deprecated) is to provide the path to the stored service account JSON file on the CSOAR server.|False|Password||
|Workload Identity Email|For the service account based authentication, specify the Workload Identity email.|False|String||
|Delegated Email|Specify the email that integration should use.|False|String||


#### Dependencies
| |
|-|
|proto_plus-1.25.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|anyio-4.6.2.post1-py3-none-any.whl|
|google_api_core-2.22.0-py3-none-any.whl|
|urllib3-2.2.3-py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|TIPCommon-2.0.1-py2.py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|httpcore-1.0.6-py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|google_auth-2.35.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.65.0-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|google_api_python_client-2.151.0-py2.py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|


## Actions
#### Delete Group
Delete a Google Workspace Directory Group.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Email Address|Email of the group to delete.|True|None||



#### Delete Extension
Preview. Use the Delete Extension action to delete a specified Chrome extension from an organizational unit blocklist. 
Note: A Chrome Enterprise license is required to use this action.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Organization Unit Name|The name of the organizational unit from which to delete the extension.|True|None||
|Extension ID|The ID of the extension to delete.|True|None||



#### List Group Privileges
List roles and privileges related to the group using Google Workspace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Email Addresses|A comma-separated list of groups that you want to examine|True|None||
|Check Roles|Specify a comma-separated list of roles that you want to check in relation to the group.|False|None||
|Check Privileges|Specify a comma-separated list of permission that you want to check in relation to the group. Note: "Expand Privileges" needs to be enabled for this parameter to work. If there are values inside the "Check Roles" parameter, action will check the privileges only among those roles.|False|None||
|Expand Privileges|If enabled, action will return information about all of the unique privileges related to the group.|False|None||
|Max Roles To Return|Specify how many roles related to the group to return.|True|None||
|Max Privileges To Return|Specify how many privileges related to the group to return.|True|None||



#### Get Group Details
Retrieve information about a group using Google Workspace.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Email Addresses|A comma-separated list of group emails that you want to examine.|True|None||



#### List OU Of Account
List the organizational units of an account
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|The unique ID for the customer's G Suite account, 'my_customer' alias can also be used to represent your account's customerId.|True|None||
|Organization Unit Path|The path of the organizational unit that needs to be returned.|False|None||
|Max Organization Units|Number of organizational units to return. Maximum is 100.|True|None||



#### List User Privileges
List roles and privileges related to the user using Google Workspace. Supported entities: User.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Email Addresses|A comma-separated list of users that you want to remove from the group. Note: values from this parameter will be executed alongside User Entities.|False|None||
|Check Roles|Specify a comma-separated list of roles that you want to check in relation to the user.|False|None||
|Check Privileges|Specify a comma-separated list of permission that you want to check in relation to the user. Note: "Expand Privileges" needs to be enabled for this parameter to work. If there are values inside the "Check Roles" parameter, action will check the privileges only among those roles.|False|None||
|Include Inherited Roles|If enabled, action will additionally return user roles that were inherited from groups.|False|None||
|Expand Privileges|If enabled, action will return information about all of the unique privileges related to the user.|False|None||
|Max Roles To Return|Specify how many roles related to the user to return.|True|None||
|Max Privileges To Return|Specify how many privileges related to the user to return.|True|None||



#### Ping
Test connectivity to Google Workspace
Timeout - 600 Seconds



#### Remove Members From Group
Remove members from a group. Action runs on Google SecOps User entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Email Address|Email of the group to remove the members from.|True|None||
|User Email Addresses|A comma-separated list of users that you want to remove from the group. Note: values from this parameter will be executed alongside User Entities.|False|None||



#### Update OU
Update an organizational unit.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|The unique ID for the customer's G Suite account, 'my_customer' alias can also be used to represent your account's customerId.|True|None||
|Name|Display name of the OU.|False|None||
|Description|Description of the OU.|False|None||
|OU Path|The full path to the organizational unit. If organizational unit is located under root (/) path, provide just organizational unit name, without path.|True|None||



#### Delete User
Delete a user.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Email Address|The email address of the user to delete.|True|None||



#### List Group Members
List the members of a group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Email Address|Email address of the group.|True|None||
|Include Derived Membership|Whether to list indirect memberships.|False|None||



#### Add Members To Group
Add members to a group. Action runs on Google SecOps User entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Email Address|Email of the group to add the members to.|True|None||
|User Email Addresses|A comma-separated list of users that you want to remove from the group. Note: values from this parameter will be executed alongside User Entities.|False|None||



#### List Users
List users present in account.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|The unique ID for the customer's G Suite account, 'my_customer' alias can also be used to represent your account's customerId.|False|None||
|Domain|Specify a domain to search for users in.|False|None||
|Manager Email|The email address of a user's direct manager|False|None||
|Return only Admin Accounts?|Specify whether to return only admin accounts.|False|None||
|Return only Delegated Admin Accounts?|Specify whether to return only delegated admin accounts.|False|None||
|Return only Suspended Users?|Specify whether to return only suspended accounts.|False|None||
|Org Unit Path|The full path of an org unit to retrieve users from. This matches all org unit chains under the target.|False|None||
|Department|The department within the organization to retrieve users from.|False|None||
|Record Limit|Specify how many records can be returned by the action.|False|None||
|Custom Query Parameter|Optional. Specify custom query parameter you want to add to the list users search call. For example, orgName='Human Resources' For reference on which fields can be used see https://developers.google.com/admin-sdk/directory/v1/guides/search-users#fields. Note: when providing the 'Custom Query Parameter', make sure that you are not providing 'email' field alongside 'Email Addresses' parameter as the generated query will not work.|False|None||
|Return only users without 2fa?|If enabled, action will only return users that don't have 2fa enabled.|False|None||
|Email Addresses|Specify a comma-separated list of email addresses that need to be searched for. Note: if 'Email Addresses' parameter is used, then 'Record Limit' parameter is ignored.|False|None||



#### Delete OU
Delete an organizational unit.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|The unique ID for the customer's G Suite account, 'my_customer' alias can also be used to represent your account's customerId.|True|None||
|OU Path|The full path to the organizational unit. If organizational unit is located under root (/) path, provide just organizational unit name, without path.|True|None||



#### Enrich Entities
Enrich Google SecOps User entities with information from Google Workspace.
Timeout - 600 Seconds



#### Create Group
Create a new group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Email Address|Email address of the new group.|True|None||
|Name|Display name of the new group.|False|None||
|Description|Description of the new group.|False|None||



#### Get Extension Details
Use the Get Extension Details action to retrieve information about a specified Chrome Extension. 
Note: A Chrome Enterprise license is required to use this action.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Extension ID|A comma-separated list of extension IDs to enrich.|True|None||
|Max Requesting Users To Return|The maximum number of users to return who requested the extension installation.The maximum value is `1000`.|True|None||
|Max Requesting Devices To Return|The maximum number of devices to return where the extension installation was requested.The maximum value is `1000`.|True|None||



#### Create User
Create a new user.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Given Name|The user's first name|True|None||
|Family Name|The user's last name|True|None||
|Password|The password of the new user.|True|None||
|Email Address|The user's primary email address|True|None||
|Phone|The phone number of the user.|False|None||
|Gender|The gender of the user. Valid values: female, male, other, unknown.|False|None||
|Department|The name of the department of the user.|False|None||
|Organization|The name of the organization of the user.|False|None||
|Change Password At Next Login|Whether to force the user to change his password on next login.|False|None||



#### Remove Extension
Use the Remove Extension action to remove a specified Chrome extension from an organizational unit registered Chrome browsers.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Organization Unit Name|The name of the organizational unit from which to remove the extension.|True|None||
|Extension ID|The ID of the extension to remove.|True|None||



#### Get Host Browser Details
Use the Get Host Browser Details action to retrieve information about browsers associated with a specified Google SecOps Hostname entity.
Note: This action requires a Chrome Enterprise license.
Timeout - 600 Seconds



#### Create OU
Create a new organizational unit.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|The unique ID for the customer's G Suite account, 'my_customer' alias can also be used to represent your account's customerId.|True|None||
|Name|Display name of the new OU.|False|None||
|Description|Description of the new OU.|False|None||
|Parent OU Path|The full path to the organizational unit's parent OU.|True|None||



#### Revoke User Session
Use the Revoke User Sessions action to revoke the user web and device sessions and reset their sign-in cookies using Google Workspace. This action runs on the Google SecOps User entity.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Email Addresses|A comma-separated list of users to sign out. The action runs the values from this parameter with User entities.|False|None||



#### Block Extension
Use the Block Extension action to block a specified Chrome extension in an organizational unit.
Note: A Chrome Enterprise license is required to use this action.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Organization Unit Name|The name of the organizational unit in which to block the extension.|True|None||
|Extension ID|The ID of the extension to block.|True|None||



#### Search User Activity Events
Use the User Activity Events action to retrieve activity events from an application for a specified Google SecOps User entity.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Email Addresses|A comma-separated list of additional user email addresses to process.The action processes all users in this list in addition to a User entity (if one is provided).|False|None||
|Application Names|A list of applications to query for activity events.For a full list of supported applications, see the [ApplicationName documentation](https://developers.google.com/workspace/admin/reports/reference/rest/v1/activities/list#applicationname).|True|None||
|Event Type Filter|A comma-separated list of event types to retrieve.|False|None||
|Time Frame|The time frame for the activity search. If Custom is selected, the Start Time parameter is required.The possible values are as follows:     • Last Hour    • Last 6 Hours    • Last 24 Hours    • Last Week    • Last Month    • Custom|False|None||
|Start Time|The start of the time range for the activity search.This parameter is required if Custom is selected for the Time Frame parameter.Configure the value in ISO 8601 format.|False|None||
|End Time|The end of the time range for the activity search.This parameter is optional when Custom is selected for the Time Frame parameter and defaults to the current time if not provided.Configure the value in ISO 8601 format.|False|None||
|Max Events To Return|The maximum number of events to return per user. The default value is 200.The maximum value is 1000.The action processes a maximum of 1000 events per user, per application.|False|None||



#### Update User
Update a Google Workspace Directory user. Note: action is not working on Google SecOps entities
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Email Address|A comma-separated list of primary email addresses that will be used to identify users that need to be updated.|True|None||
|Given Name|The user's first name|False|None||
|Family Name|The user's last name|False|None||
|Password|The password of the user.|False|None||
|Phone|The phone number of the user.|False|None||
|Gender|The gender of the user. Valid values: female, male, other, unknown.|False|None||
|Department|The name of the department of the user.|False|None||
|Organization|The name of the organization of the user.|False|None||
|Change Password At Next Login|Whether to force the user to change his password on next login.|False|None||
|User Status|Specify if user status should be updated to blocked or unblocked. By default action is no changing the user status.|False|None||











# Okta

The Okta Identity Cloud provides secure identity management with Single Sign-On, Multi-factor Authentication, Lifecycle Management (Provisioning), and more.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|The base URL of the Okta instance.|True|String||
|Api Token|The API token (SSWS) used for authentication with the Okta instance. This parameter is mandatory if Use Oauth Authentication is disabled.|False|Password||
|Use Oauth Authentication|If enabled, the integration uses OAuth 2.0 for authentication instead of an API token.|False|Boolean||
|Client ID|The unique identifier for the Okta OAuth application. This parameter is mandatory if Use Oauth Authentication is enabled. Leave this field blank if authenticating using an API token.|False|String||
|Key ID|The ID of the public key associated with the private key used for OAuth authentication. This parameter is mandatory if Use Oauth Authentication is enabled.|False|String||
|Private Key|The private key in PEM format used for OAuth authentication. This parameter is mandatory if Use Oauth Authentication is enabled. Leave this field blank if authenticating using an API Token.|False|Password||
|Verify SSL|If enabled, the integration validates the SSL certificate when connecting to the Okta server.|False|Boolean||


#### Dependencies
| |
|-|
|proto_plus-1.25.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|cryptography-43.0.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|httpcore-1.0.5-py3-none-any.whl|
|google_api_core-2.22.0-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|urllib3-2.2.3-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|pycryptodome-3.20.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl|
|anyio-4.4.0-py3-none-any.whl|
|pycryptodomex-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.10-py3-none-any.whl|
|paramiko-3.5.0-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|pyzipper-0.3.6-py2.py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|python2_secrets-1.0.5-py2.py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|google_auth-2.35.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.65.0-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|google_api_python_client-2.151.0-py2.py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|bcrypt-4.2.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cachetools-5.5.0-py3-none-any.whl|
|TIPCommon-2.2.2-py2.py3-none-any.whl|


## Actions
#### Add Group
Add a group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Name|The name of the group in Okta|True|None||
|Group Description|The description for the group|False|None||



#### Assign Role
Assign a role to a user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs|Ids of users in Okta|False|None||
|Role Types|The type of role to assign to the users|True|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### List Roles
Lists all roles assigned to a user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs|Ids of users in Okta|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### Disable User
Disables the specified user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs Or Logins|Ids of users in Okta|False|None||
|Is Deactivate|Whether to dactivate or only suspend the user|False|None||
|Send Email If Deactivate|Whether to send an email after deactivating or not|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### Unassign Role
Unassign a role from a user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs|Ids of users in Okta|False|None||
|Role IDs Or Names|Ids or names of roles in Okta|True|None||
|Is Id|Whether the values are ids or names|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### Ping
Test Connection With Okta
Timeout - 600 Seconds



#### Clear Okta User Session
Use the Clear Okta Session for User action to terminate all active Okta sessions for specified users.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs Or Logins|A comma-separated list of Okta user IDs or login identifiers.|False|None||
|Also Run On Scope|If selected, the action revokes active Identity Provider (IdP) sessions for all users identified in the entity scope, in addition to those explicitly listed in User IDs Or Logins.|False|None||



#### Get User
Get information about a user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Ids Or Logins|Ids or logins (email or short email name) of a user in Okta, e.g. test@gmail.com or simply 'test'|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### List Users
Get the list of users
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Search for a match in the firstname, lastname or in the email|False|None||
|Filter|Custom search query for a subset of properties|False|None||
|Search|Custom search query for most properties|False|None||
|Limit|Max amount of results to return|False|None||



#### Get Group
Get information about a group
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Group Ids Or Names|Ids or names of groups in Okta|True|None||
|Is Id|Whether the value is an id or a name|False|None||



#### Send ITP Signal To Okta
Send ITP Signal To Okta
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Key ID|The ID of the public key, used to verify the private key’s signature.|True|None||
|Private Key|Private key used to sign the signal. Provided in a string format (including the “BEGIN” and “END” statements).|True|None||
|User Email|Email address of the affected user.|True|None||
|Timestamp|Timestamp of the signal occurrence. Timestamp format is ISO 8601.|True|None||
|Reason|Reason for the signal creation.|True|None||
|Severity|Severity of the signal.|True|None||
|Issuer URL|Creation source of the signal.|True|None||



#### List Providers
List identity providers (IdPs) in your organization
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Search the name property for a match|False|None||
|Type|Filter by type|False|None||
|Limit|Max amount of results to return|False|None||



#### List User Groups
Get the groups that the user is a member of
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs Or Logins|Ids or logins of users in Okta|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### Reset Password
Generate a one-time token that can be used to reset a user's password
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs Or Logins|Ids or logins of users in Okta|False|None||
|Send Email|Whether to send an email for the password reset or return the token for every user|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### Set Password
Set the password of a user without validating existing credentials
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs Or Logins|Ids or logins of users in Okta|False|None||
|New Password|The new password|True|None||
|Add 10 Random Chars|Whether to add extra characters to every user password or not|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||



#### Enable User
Enables the specified user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User IDs Or Logins|Ids or logins of users in Okta|False|None||
|Is Activate|Whether to activate the user or just unsuspend|False|None||
|Send Email If Activate|Whether to send an email after activating or not|False|None||
|Also Run On Scope|Whether to run on entities as well as the input|False|None||










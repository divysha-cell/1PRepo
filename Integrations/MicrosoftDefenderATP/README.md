
# MicrosoftDefenderATP

Microsoft Defender Advanced Threat Protection (Microsoft Defender ATP) is a unified platform for preventative protection, post-breach detection, automated investigation, and response. Microsoft Defender ATP protects endpoints from cyber threats, detects advanced attacks and data breaches, automates security incidents and improves security posture. Google SecOps integration for Microsoft Defender ATP provides a list of actions to pull the data stored in Microsoft Defender ATP and use it in Google SecOps playbooks and manual actions, as well as a series of active response actions, such as isolate specific host or restrict app execution on host. In addition, integration provides a connector to ingest Microsoft Defender ATP alerts as Google SecOps Cases.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Login API Root|None|True|String|https://login.microsoftonline.com|
|Api Root|None|True|String|https://api.securitycenter.windows.com|
|Graph API Root|The base URL for the Microsoft Graph API (e.g., https://graph.microsoft.com). If provided, V2 API endpoints will be used.|False|String||
|Client ID|None|True|String||
|Client Secret|None|True|Password|*****|
|Azure Active Directory ID|None|True|String||
|Verify SSL|None|False|Boolean|True|


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
|pyOpenSSL-24.2.1-py3-none-any.whl|
|anyio-4.6.2.post1-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|TIPCommon-2.0.4-py2.py3-none-any.whl|
|google_auth-2.36.0-py2.py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|googleapis_common_protos-1.66.0-py2.py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|httpcore-1.0.6-py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|google_api_core-2.23.0-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|google_api_python_client-2.152.0-py2.py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|


## Actions
#### Get Current Task Status
Get Current Task Status
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Task IDs|Task IDs list. Comma-separated string|True|String||



#### Create Isolate Machine Task
Create Isolate Machine Task
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Isolation Type|Isolation type|True|List|Full|
|Comment|Comment why the machine needs to be isolated|True|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Run Advanced Hunting Query
Run Advanced Hunting Query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Advanced hunting query to execute|True|String||



#### Submit Entity Indicators
Submit entities as indicators in Microsoft Defender ATP. Supported entities: Filehash, URL, IP Address. Note: only MD5, SHA1 and SHA256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Action|Specify the action that needs to be applied to the entities. Note: "Block And Remediate" is supported only for filehash entities.|True|List|Block|
|Severity|Specify the severity for the found entities.|True|List|High|
|Application|Specify an application that is related to the entities.|False|String||
|Indicator Alert Title|Specify what should be the title for the alert, if they are identified in the environment.|True|String||
|Description|Specify the description for the entities.|True|String|Siemplify Remediation|
|Recommended Action|Specify what should be the recommended actions for the handling of the entities.|False|String||



#### Update Alert
Update Alerts
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Microsoft Defender ATP Alert ID to update.|True|String||
|Status|Status of the alert|False|List|New|
|Assigned To|User who is assigned to this alert|False|String||
|Classification|Classification to update alert with|False|List|Unknown|
|Determination|Determination to update alert with|False|List|NotAvailable|



#### Get File Related Alerts
Deprecated. Get File Related Alerts. Note: For this action only SHA1 is supported
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Status|Statuses of the alert to look for. Comma-separated string|False|String|Unknown, New, InProgress, Resolved|
|Severity|Severities of the alert to look for. Comma-separated string.|False|String|UnSpecified, Informational, Low, Medium, High|
|Category|Categories of the alert to look for. Comma-separated string.|False|String||
|Incident ID|Microsoft Defender Incident ID for which you want to find related alerts.|False|String||



#### Create Stop And Quarantine File Specific Machine Task
Create Stop and Quarantine a File on Specific Machine Task
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SHA1 File Hash to Quarantine|SHA1 File Hash to Quarantine|True|String||
|Comment|Comment to associate with the action|True|String||



#### Create Run Antivirus Scan Task
Create Run AV Scan Task
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Antivirus Scan Type|Antivirus Scan Type|True|List|Full|
|Comment|Comment why an antivirus scan needs to be executed on the machine|True|String||



#### Get File Related Machines
Get File Related Machines. Note: For this action only SHA1 is supported
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Machine Name|Full Machine Name to look for|False|String||
|Machine IP Address|Machine IP Address to look for|False|String||
|Machine Risk Score|Machine risk score to look for. Comma-separated string.|False|String|None, Low, Medium, High|
|Machine Health Status|Machine health status to look for. Comma-separated string|False|String|Active, Inactive, ImpairedCommunication, NoSensorData, NoSensorDataImpairedCommunication|
|Machine OS Platform|Machine OS platform to look for.|False|String||
|RBAC Group ID|RBAC Group ID to look for.|False|String||



#### Enrich Entities
This action allows a user to enrich Microsoft Defender ATP hosts, ips and file hashes. Note: File hash can be in sha1 or sha256 format.
Timeout - 600 Seconds



#### Get Machine Logon Users
Get Machine Log on users
Timeout - 600 Seconds



#### Get Machine Recommendations
Use the Get Machine Recommendations action to retrieve a list of security recommendations for specific machines in Microsoft Defender for Endpoint.Supported Entities: IP Address, Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Recommendations To Return|The maximum number of recommendations to return for each entity. Maximum: 100.|True|String|100|



#### Get User Related Alerts
Use the Get User Related Alerts action to list alerts associated with specific users in Microsoft Defender for Endpoint. Supported Entities: User.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Alerts To Return|The maximum number of alerts to retrieve for each user. Maximum: 100.|True|String|100|



#### Execute Live Response Command
Use "Execute Live Response Command" action to execute a live response command in Microsoft Defender for Endpoint. Supported Entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Command|JSON object that represents the command that needs to be executed. More information is available on this page: https://learn.microsoft.com/en-us/defender-endpoint/api/run-live-response|True|String|{
     "type": "Command",
     "params": [
          {
               "key": "string",
               "value": "string"
          }
     ]
}|
|Comment|Comment that describes the executed command.|False|String||



#### Get Machine Related Alerts
Deprecated. Get Machine Related Alerts
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Status|Statuses of the alert to look for. Comma-separated string|False|String|Unknown, New, InProgress, Resolved|
|Severity|Severities of the alert to look for. Comma-separated string.|False|String|UnSpecified, Informational, Low, Medium, High|
|Category|Categories of the alert to look for. Comma-separated string.|False|String||
|Incident ID|Microsoft Defender Incident ID for which you want to find related alerts.|False|String||



#### Get Machine Vulnerabilities
Use the Get Machine Vulnerabilities action to list vulnerabilities associated with specific machines in Microsoft Defender for Endpoint. Supported Entities: IP Address, Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Severity Filter|The severity levels used to filter the returned vulnerabilities.|False|MultipleChoiceParameter|Critical|
|Threat Filter|The threat intelligence criteria used to filter the returned vulnerabilities.|False|MultipleChoiceParameter||
|Sort By|The field used to sort the returned vulnerabilities.|False|List|Severity|
|Sort Order|The order in which the sorted results are displayed.|False|List|ASC|
|Max Vulnerabilities To Return|The maximum number of vulnerabilities to return for each entity. Maximum: 100.|True|String|100|



#### Delete Entity Indicators
Delete entity indicators in Microsoft Defender ATP. Supported entities: Filehash, URL, IP Address. Note: only MD5, SHA1 and SHA256 hashes are supported.
Timeout - 600 Seconds



#### Create Unisolate Machine Task
Create Unisolate Machine Task
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Comment why the machine needs to be isolated|True|String||



#### List Alerts
Get Alerts
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Time frame in hours for which to fetch Alerts|False|String|3|
|Status|Statuses of the alert to look for. Comma-separated string|False|String|Unknown, New, InProgress, Resolved|
|Severity|Severities of the alert to look for. Comma-separated string.|False|String||
|Category|Categories of the alert to look for. Comma-separated string.|False|String||
|Incident ID|Microsoft Defender Incident ID for which you want to find related alerts.|False|String||



#### List Indicators
List indicators in Microsoft Defender ATP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Indicators|Specify a comma-separated list of indicators that you would like to retrieve.|False|String||
|Indicator Types|Specify a comma-separated list of indicator types that you want to retrieve. Possible values: FileSha1, FileSha256, FileMd5, CertificateThumbprint, IpAddress, DomainName, Url.|False|String|FileSha1,FileSha256,FileMd5,CertificateThumbprint,IpAddress,DomainName,Url|
|Actions|Specify a comma-separated list of indicator actions that you want to use for filtering. Possible values: Warn,Block,Audit,Alert,AlertAndBlock,BlockAndRemediate,Allowed.|False|String|Warn,Block,Audit,Alert,AlertAndBlock,BlockAndRemediate,Allowed|
|Severity|Specify a comma-separated list of severities that you want to use for filtering. Possible values: Informational,Low,Medium,High.|False|String|Informational,Low,Medium,High|
|Max Results To Return|Specify how many indicators to return. Default: 50.|False|String|50|



#### List Machines
Get Machines
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Last Seen Time Frame|Time frame in hours for which to fetch Machines|False|String||
|Machine Name|Full Machine Name to look for|False|String||
|Machine IP Address|Machine IP Address to look for|False|String||
|Machine Risk Score|Machine risk score to look for. Comma-separated string.|False|String|None, Low, Medium, High|
|Machine Health Status|Machine health status to look for. Comma-separated string|False|String|Active, Inactive, ImpairedCommunication, NoSensorData, NoSensorDataImpairedCommunication|
|Machine OS Platform|Machine OS platform to look for.|False|String||
|RBAC Group ID|RBAC Group ID to look for.|False|String||



#### Wait Task Status
Wait for Task Status
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Task IDs|Task IDs list. Comma-separated string|True|String||









## Connectors
#### Microsoft Defender ATP Connector V2
Connector can be used to fetch Defender ATP alerts with events information from 365 Defender, as Defender ATP SIEM API used in v1 connector for events is deprecated starting March 1st 2022. Connector whitelist can be used to ingest only specific types of alerts based on alert's "detectionSource" attribute value. SourceGroupIdentifier of the connector can be used to group Siemplify alerts based on Defender ATP incident id.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is "".|False|Int|.*|
|Login API Root|Login API root of the Microsoft 365 Defender instance.|True|String|https://login.microsoftonline.com|
|Defender ATP API Root|Api root url to use with integration. For better performance, you can use server closer to your geo location: api-us.securitycenter.windows.com api-eu.securitycenter.windows.com api-uk.securitycenter.windows.com|True|String|https://api.securitycenter.windows.com|
|365 Defender API Root|API root of the Microsoft 365 Defender instance used to get Siemplify events data.|True|String|https://api.security.microsoft.com|
|Graph API Root|The base URL for the Microsoft Graph API (e.g., https://graph.microsoft.com). If provided, V2 API endpoints will be used.|False|String||
|Azure Active Directory ID|Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|String||
|Integration Client ID|Client (Application) ID that was added for app registration in Azure Active Directory for the integration.|True|String||
|Integration Client Secret|Secret that was entered for Azure AD app registration for the integration.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft 365 Defender server is valid.|False|Boolean|true|
|Offset Time In Hours|Fetch alerts from X hours backwards.|True|Int|24|
|Max Alerts per Cycle|How many alerts should be processed during one connector run.|True|Int|10|
|Alert Statuses to Fetch|Specify the statuses of the Defender ATP alerts that should be fetched by the Siemplify server. Parameter can take multiple values as a comma separated string.|True|String|Unknown, New, InProgress, Resolved|
|Alert Severities to Fetch|Specify the severities of the Defender ATP alerts that should be fetched by the Siemplify server. Parameter can take multiple values as a comma separated string.|True|String|UnSpecified, Informational, Low, Medium, High|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|Boolean|false|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|Proxy server to use for connection.|False|IP||
|Proxy Server Username|Proxy server username|False|String||
|Proxy Server Password|Proxy server password|False|Password|*****|


#### Microsoft Defender ATP Connector
Fetch alerts and events from MS Defender ATP

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored.|False|String||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "environment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|Int||
|Login API Root|Login API root of the Microsoft 365 Defender instance.|True|String|https://login.microsoftonline.com|
|API Root|The API Root of Microsoft Defender ATP|True|String|https://api.securitycenter.windows.com|
|Azure Active Directory ID|Azure Active Directory Tenant ID, can be viewed in Active Directory > App Registration > <Application you configured for your integration> > Directory (tenant) ID.|True|String||
|Integration Client ID|Client (Application) ID that was added for the app registration in Azure Active Directory for this integration.|True|String||
|Integration Client Secret|Secret that was entered for Azure AD app registration|True|Password|*****|
|SIEM Client ID|Client (Application) ID for the enabled SIEM integration in Microsoft Defender ATP|True|String||
|SIEM Client Secret|Secret that for the enabled SIEM integration in Microsoft Defender ATP|True|Password|*****|
|Max Alerts per Cycle|How many alerts should be processed during one connector run|True|Int|100|
|Offset Time In Hours|Fetch alerts from X hours backwards. Default value: 24 hours.|True|Int|24|
|Alert Statuses to Fetch|Specify the statuses of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|String|Unknown, New, InProgress, Resolved|
|Alert Severities to Fetch|Specify the severities of the incidents that should be fetched by the Siemplify server. Comma-separated string.|True|String|UnSpecified, Informational, Low, Medium, High|
|Proxy Server Address|Proxy server to use for connection.|False|IP||
|Proxy Server Username|Proxy server username|False|String||
|Proxy Server Password|Proxy server password|False|Password|*****|





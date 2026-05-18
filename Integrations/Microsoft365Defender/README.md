
# Microsoft365Defender

Microsoft 365 Defender is a unified pre- and post-breach enterprise defense suite that natively coordinates detection, prevention, investigation, and response across endpoints, identities, email, and applications to provide integrated protection against sophisticated attacks.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Login API Root|None|True|String||
|Graph API Root|None|True|String||
|API Root|None|True|String||
|Tenant ID|None|True|String||
|Client ID|None|True|String||
|Client Secret|None|True|Password||
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|requests-2.32.5-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|TIPCommon-2.3.4-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|cachetools-6.2.4-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|certifi-2026.2.25-py3-none-any.whl|
|charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|httpx-0.28.1-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.11-py3-none-any.whl|
|googleapis_common_protos-1.73.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|sniffio-1.3.1-py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Add Comment To Incident
Add comment to incident in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Specify the comment that needs to be added to the incident.|True|None||
|Incident ID|Specify the id of the incident that needs to be updated.|True|None||



#### Execute Entity Query
Execute a hunting query based on entities in Microsoft 365 Defender. Note: this action prepares a where filter based on entities. Please refer to the documentation for more details. Supported entities: IP, Host, User, Hash, URL.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Names|Specify what tables should be queried.|True|None||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|None||
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|None||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|None||
|Fields To Return|Specify what fields to return.|False|None||
|Sort Field|Specify what parameter should be used for sorting.|False|None||
|Sort Order|Specify the order of sorting.|False|None||
|Max Results To Return|Specify how many results to return. Default: 50.|False|None||
|IP Entity Key|Specify what key should be used with IP entities. Please refer to the action documentation for details.|False|None||
|Hostname Entity Key|Specify what key should be used with Hostname entities. Please refer to the action documentation for details.|False|None||
|File Hash Entity Key|Specify what key should be used with File Hash entities. Please refer to the action documentation for details.|False|None||
|User Entity Key|Specify what key should be used with User entities. Please refer to the action documentation for details.|False|None||
|URL Entity Key|Specify what key should be used with URL entities. Please refer to the action documentation for details.|False|None||
|Email Address Entity Key|Specify what key should be used with Email Address (User entity with email regex) entities. Please refer to the action documentation for details.|False|None||
|Stop If Not Enough Entities|If enabled, action will not start execution, unless all of the entity types are available for the specified “.. Entity Keys”. Example: if “IP Entity Key” and “File Hash Entity Key” are specified, but in the scope there are no file hashes then if this parameter is enabled, action will not execute the query.|False|None||
|Cross Entity Operator|Specify what should be the logical operator used between different entity types.|True|None||



#### Update Incident
Update incident in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|Specify the id of the incident that needs to be updated.|True|None||
|Status|Specify what status to set for the incident.|False|None||
|Classification|Specify what classification to set for the incident..|False|None||
|Determination|Specify what determination to set for the incident. Note: determination can only be set, when classification is true positive.|False|None||
|Assign To|Specify to whom to assign this incident.|False|None||



#### Ping
Test connectivity to the Microsoft 365 Defender with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Execute Custom Query
Execute a custom hunting query in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|Specify the query that needs to be executed. Use this parameter to provide |where clauses. Note: Note: you don't need to provide a limiting ("top" keyword).|True|None||
|Max Results To Return|Specify how many results to return. Default: 50.|False|None||



#### Execute Query
Execute hunting query in Microsoft 365 Defender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Names|Specify what tables should be queried.|True|None||
|Query|Specify the query that needs to be executed. Use this parameter to provide |where clauses. Note: you don’t need to provide time filter, limiting and sorting.|False|None||
|Time Frame|Specify a time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|None||
|Start Time|Specify the start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|None||
|End Time|Specify the end time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|None||
|Fields To Return|Specify what fields to return.|False|None||
|Sort Field|Specify what parameter should be used for sorting.|False|None||
|Sort Order|Specify the order of sorting.|False|None||
|Max Results To Return|Specify how many results to return. Default: 50.|False|None||






## Jobs

#### Sync Alerts
This job synchronizes Google SecOps Alerts and Microsoft Defender XDR Alerts. It ensures that comments and status are synchronized bi-directionally between both systems. Note: Assignee synchronization occurs exclusively from Microsoft Defender to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the "Microsoft Defender XDR Alert" tag. If the alert didn’t originate from "Microsoft 365 Defender - Incidents Connector",  you will need to add an "Alert_ID" context value to the alert for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|None|Default Environment|
|Login API Root|True|None|https://login.microsoftonline.com|
|Graph API Root|True|None|https://graph.microsoft.com|
|API Root|True|None|https://api.security.microsoft.com|
|Tenant ID|True|None||
|Client ID|True|None||
|Client Secret|True|None||
|Max Hours Backwards|True|None|24|
|Sync Assignee|False|None|false|
|Verify SSL|False|None|true|



## Connectors
#### Microsoft 365 Defender - Incidents Connector
Pull information about incidents and related alerts from Microsoft 365 Defender. Note: whitelist works with an incident name.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|None|.*|
|Login API Root|Login API root of the Microsoft 365 Defender instance.|True|None|https://login.microsoftonline.com|
|Graph API Root|API root of the Microsoft Graph service.|True|None|https://graph.microsoft.com|
|Tenant ID|Microsoft 365 Defender account tenant ID.|True|None||
|Client ID|Microsoft 365 Defender account client ID.|True|None||
|Client Secret|Microsoft 365 Defender account client secret.|True|None||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft 365 Defender server is valid.|False|None|true|
|Lowest Severity To Fetch|Lowest severity that will be used to fetch incidents. Possible values: Informational, Low, Medium, High.|False|None||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|None|1|
|Max Incidents To Fetch|How many incidents  to process per one connector iteration. Maximum is 20.|False|None|10|
|Dynamic List Field|Field that can be used in the dynamic list for filtering. Possible values: Incident Name, Alert Name. If nothing is provided, connector will work with the incident name.|False|None|Incident Name|
|Incident Status Filter|A comma-separated list of incident statuses that need to be ingested. If nothing is provided, the connector will ingest incidents with status “Active” and “In Progress”. Possible values:Active, In Progress, Resolved, Redirected.Note: it’s not recommended to ingest redirected incidents, because in most situations they will be empty.|False|None|Active, In Progress|
|Alert Detection Source Filter|A comma-separated list of detection sources of alerts that need to be ingested. Note: this is a case sensitive parameter. Example of the values:antivirus, microsoftDefenderForEndpoint|False|None||
|Alert Service Source Filter|A comma-separated list of service sources of alerts that need to be ingested. Note: this is a case sensitive parameter. Example of the values:antivirus, microsoftDefenderForEndpoint|False|None||
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|None|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|None|true|
|Lowest Alert Severity To Fetch|Lowest severity that will be used to fetch alerts. Possible values: Informational, Low, Medium, High.|False|None||
|Disable Alert Tracking|If enabled, the connector will stop tracking updates associated with alerts.|False|None|false|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||





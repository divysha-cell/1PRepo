
# CrowdStrikeFalcon

CrowdStrike Falcon is the leader in next-generation endpoint protection, threat intelligence and incident response through cloud-based endpoint protection.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|False|String|https://api.crowdstrike.com|
|Client API ID|None|True|String||
|Client API Secret|None|True|Password|*****|
|Verify SSL|None|False|Boolean|False|
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|String||


#### Dependencies
| |
|-|
|requests-2.32.5-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|anyio-4.13.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|TIPCommon-2.3.4-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
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
|requests_file-2.1.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|sniffio-1.3.1-py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Add Alert Comment
Add a comment to alert in Crowdstrike. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert that needs to be updated.|True|String||
|Comment|Specify the comment for the alert.|True|String||



#### Contain Endpoint
Contain endpoint in Crowdstrike Falcon. Supported entities: Hostname and IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Fail If Timeout|If enabled, action will be failed, if not all of the endpoints were contained.|False|Boolean|true|





#### Get Process Name By IOC
DEPRECATED. Retrieve processes related to the IOCs and provided devices in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported. IP address entities are treated as IOCs.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Devices Names|Specify a comma-separated list of devices for which you want to retrieve processes related to entities.|True|String||





#### Add Identity Protection Detection Comment
Add a comment to identity protection detection in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the ID of the detection that needs to be updated.|True|String||
|Comment|Specify the comment for the detection.|True|String||



#### Submit File
Submit files to a sandbox in Crowdstrike. Note: This action requires a Falcon Sandbox license. For the list of supported file formats, refer to the documentation portal.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Paths|Specify the file paths to the files that need to be submitted. Refer to the documentation portal for a list of the supported file formats.|True|String||
|Sandbox Environment|Specify the sandbox environment for the analysis.|False|List|Windows 10, 64-bit|
|Network Environment|Specify the network environment for the analysis.|False|List|Default|
|Archive Password|Specify the password that would need to be used, when working with archive files.|False|Password|*****|
|Document Password|Specify the password that would need to be used, when working with Adobe or Office files. Maximum: 32 characters.|False|Password|*****|
|Check Duplicate|If enabled, the action checks if the file was already submitted previously and returns the available report. Note: during the validation “Network Environment” and “Sandbox Environment” are not taken into consideration.|False|Boolean|true|
|Comment|Specify the comment for the submission.|False|String||
|Confidential Submission|If enabled, the file is only shown to users within your customer account.|False|Boolean|false|





#### Delete IOC
Delete custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds



#### Add Comment to Detection
Deprecated. Add a comment to the detection in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the id of the detection to which you want to add a comment.|True|String||
|Comment|Specify the comment that needs to be added to the detection.|True|String||



#### Execute Command
Execute commands on the hosts in Crowdstrike Falcon. Supported entities: IP Address and Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Command|Specify what command to execute on the hosts.|True|String||
|Admin Command|If enabled, action will execute commands with the admin level permissions. This is necessary for certain commands like "put".|False|Boolean|false|
|Hostname|Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.|False|String||
|Queue Offline|If enabled, commands targeting offline hosts are queued and executed once the host reconnects to the network.|False|Boolean|false|





#### Add Incident Comment
Deprecated. Add comment to incident in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident ID|Specify the ID of the incident that needs to be updated.|True|String||
|Comment|Specify the comment for the incident.|True|String||





#### Get Event Offset
Action will retrieve the event offset that is used by the Event Streaming Connector. Note: action starts processing events from 30 days ago.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Events To Process|Specify how many events the action needs to process starting from the offset from 30 days ago.|True|String|10000|





#### Get Hosts by IOC
DEPRECATED. List hosts related to the IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds





#### Get Host Information
Retrieve information about the hostname from Crowdstrike Falcon. Supported entities: Hostname, IP Address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Create Insight|If enabled, action will create insights containing information regarding entities.|False|Boolean|true|





#### Close Detection
Deprecated. Close a Crowdstrike Falcon detection. Note: Action "Update Detection" is the best practice for this use case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the id of the detection that needs to be closed.|True|String||
|Hide Detection|If enabled, action will hide the detection in the UI.|False|Boolean|true|



#### Lift Contained Endpoint
Lift endpoint containment in Crowdstrike Falcon. Supported entities: Hostname and IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Fail If Timeout|If enabled, action will be failed, if containment was not lifted on all endpoints.|False|Boolean|true|





#### Hide Hosts
Use the Hide Hosts action to hide one or more hosts from the CrowdStrike Falcon console. Supported entities: IP Address, Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hostname|A comma-separated list of hostnames to hide in CrowdStrike Falcon. The action processes both the input values provided in this parameter and the Hostname and IP Address entities attached to the case.|False|String||
|Customer ID|The unique CrowdStrike Customer ID (CID) used to target a specific tenant. This parameter is required in Falcon Flight Control or multi-tenant environments to perform the action on a specific child CID.|False|String||





#### Get Alert Details
Get details of an alert in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert.|True|String||





#### List Host Vulnerabilities
List vulnerabilities found on the host in Crowdstrike Falcon. Supported entities: IP Address and Hostname. Note: requires Falcon Spotlight license and permissions. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Severity Filter|Specify the comma-separated list of severities for vulnerabilities.If nothing is provided, action will ingest all related vulnerabilities. Possible values: Critical, High, Medium, Low, Unknown.|False|String||
|Create Insight|If enabled, action will create an insight per entity containing statistical information about related vulnerabilities.|False|Boolean|true|
|Max Vulnerabilities To Return|Specify how many vulnerabilities to return per host. If nothing is provided action will process all of the related vulnerabilities.|False|String|100|





#### List Hosts
List available hosts in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Filter Logic|Specify what logic should be used, when searching for hosts.|False|List|Equal|
|Filter Value|Specify the value that should be used to filter hosts.|False|String||
|Max Hosts To Return|Specify how many hosts to return. Default: 50. Maximum: 1000.|False|String|50|





#### List Uploaded IOCs
List available custom IOCs in CrowdStrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IOC Type Filter|Specify a comma-separated list of IOC types that should be returned. If nothing is provided, action will return IOCs from all types. Possible values: ipv4,ipv6,md5,sha256,domain.|False|String|ipv4,ipv6,md5,sha256,domain|
|Value Filter Logic|Specify the value filter logic. If "Equal" is selected, action will try to find the exact match among IOCs and if "Contains" is selected, action will try to find IOCs that contain that substring.|False|List|Equal|
|Value Filter String|Specify the string that should be searched among IOCs.|False|String||
|Max IOCs To Return|Specify how many IOCs to return. Default: 50. Maximum: 500.|False|String|50|





#### On-Demand Scan
Scan the endpoint on demand in Crowdstrike. Note: only Windows hosts are supported. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Chronicle SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|File Paths To Scan|Comma-separated list of paths to scan.|True|String|C:\Windows|
|File Paths To Exclude From Scan|Comma-separated list of paths to exclude from scanning.|False|String||
|Host Group Name|Comma-separated list of host group names to initiate scanning for. Note: Separate scanning process is created for each host group.|False|String||
|Scan Description|Description for the scan. If no value is provided, the action sets the description to the following: "Scan initialized by Chronicle SecOps."|False|String||
|CPU Priority|The amount of CPU to  use for the underlying host during scanning.|False|List|Up to 25% CPU utilization|
|Sensor Anti-malware Detection Level|Specify the sensor anti-malware detection level. Note: Detection level must be equal to or higher than the Prevention level.|False|List|Moderate|
|Sensor Anti-malware Prevention Level|Specify the sensor anti-malware prevention level. Note: Detection level must be equal to or higher than the Prevention level.|False|List|Moderate|
|Cloud Anti-malware Detection Level|Specify the cloud anti-malware detection level. Note: Detection level must be equal to or higher than the Prevention level.|False|List|Moderate|
|Cloud Anti-malware Prevention Level|Specify the cloud anti-malware prevention level. Note: Detection level must be equal to or higher than the Prevention level.|False|List|Moderate|
|Quarantine Hosts|If enabled, underlying hosts are quarantined as part of scanning.|False|Boolean|false|
|Create Endpoint Notification|If enabled, the scanning process creates an endpoint notification.|False|Boolean|true|
|Max Scan Duration|Number of hours for a scan to run. If no value is provided, the scan runs continuously.|False|String|1|
|Hostname|Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.|False|String||





#### Update Incident
Deprecated. Update incident in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Incident ID|Specify the ID of the incident that needs to be updated.|True|String||
|Status|Specify the status for the incident.|False|List|Select One|
|Assign to|Specify the name or email of the analyst to whom the incident needs to be assigned. If "Unassign" is provided, action will remove assignment from the incident. Note: for name you need to provide first and last name of the analyst in the following format "{first name} {last name}"|False|String||





#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Upload IOCs
Add custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Platform|Specify a comma-separated list of the platforms related to the IOC. Possible values: Windows, Linux, Mac.|True|String|Windows,Linux,Mac|
|Severity|Specify the severity for the IOC.|True|List|Medium|
|Comment|Specify a comment with more context related to IOC.|False|String||
|Host Group Name|Specify the name of the host group.|False|String||
|Action|Specify the action for the uploaded IOCs. Note: "Block" action can only be applied to hashes. Action will always apply "Detect" policy to all other IOC types.|False|List|Detect|
|Days To Expire|The number of days before the IOC expires.|False|String||



#### Run Script
Execute a powershell script on the endpoints in Crowdstrike. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for the action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Script Name|The name of the script file that needs to be executed. Note: either “Script Name” or “Raw Script” should be provided. If both “Script Name” and “Raw Script” are provided, then “Raw Script” will have the priority.|False|String||
|Raw Script|Raw powershell script payload that needs to be executed on the endpoints. Note: either “Script Name” or “Raw Script” should be provided. If both “Script Name” and “Raw Script” are provided, then “Raw Script” will have the priority.|False|String||
|Hostname|Comma-separated list of hostnames on which you want to execute the action. Note: action will run the action on both entities + this parameter values.|False|String||
|Queue Offline|If enabled, commands targeting offline hosts are queued and executed once the host reconnects to the network.|False|Boolean|false|





#### Submit URL
Submit urls to a sandbox in Crowdstrike. Note: This action requires a Falcon Sandbox license.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URLs|Specify the URLs that need to be submitted.|True|String||
|Sandbox Environment|Specify the sandbox environment for the analysis.|False|List|Windows 10, 64-bit|
|Network Environment|Specify the network environment for the analysis.|False|List|Default|
|Check Duplicate|If enabled, the action checks if the file was already submitted previously and returns an available report. Note: during the validation “Network Environment” and “Sandbox Environment” are not taken into consideration.|False|Boolean|true|





#### Update Alert
Update an alert in Crowdstrike.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert that needs to be updated.|True|String||
|Status|Specify the status for the alert.|False|List|Select One|
|Verdict|Specify the verdict for the alert.|False|List|Select One|
|Assign To|Specify the name of the analyst to whom the alert needs to be assigned. If "Unassign" is provided, action will remove assignment from the alert. Note: API will accept any value that is provided, even if the underlying user doesn’t exist.|False|String||





#### Update IOC Information
Update information about custom IOCs in Crowdstrike Falcon. Supported entities: Hostname, URL, IP address and Hash. Note: Hostname entities are treated as domain IOCs and action will extract domain part out of URLs. Only MD5 and SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Description|Specify a new description for custom IOCs.|False|Content||
|Source|Specify the source for custom IOCs.|False|Content||
|Expiration days|Specify the amount of days till expiration.|False|String||
|Detect policy|If enabled, IOCs that have been identifed, will send a notification. In other case, no action will be taken|False|Boolean|true|





#### Update Identity Protection Detection
Update an identity protection detection in Crowdstrike. Note: this action requires an Identity Protection license.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the ID of the detection that needs to be updated.|True|String||
|Status|Specify the status for the detection.|False|List|Select One|
|Assign To|Specify the name of the analyst to whom the detection needs to be assigned. If "Unassign" is provided, action will remove assignment from the detection. Note: API will accept any value that is provided, even if the underlying user doesn't exist.|False|String||





#### Update Detection
Deprecated. Update detection in Crowdstrike Falcon.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Detection ID|Specify the ID of the detection that needs to be updated.|True|String||
|Status|Specify the new status for the detection.|True|List|Select One|
|Assign Detection to|Specify the email address of the Crowdstrike Falcon user, who needs to be assigned to this detection|False|String||



#### Download File
Download files from the hosts in Crowdstrike Falcon. Supported entities: File Name, IP Address and Hostname. Note: action requires both File Name and IP Address/Hostname entity to be in the scope of the Siemplify alert. The downloaded file will be in password-protected zip. Password is "infected".
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Customer ID|Specify the ID of the customer for which you want to execute the action.|False|String||
|Download Folder Path|Specify the path to the folder, where you want to store the threat file.|True|String||
|Overwrite|If enabled, action will overwrite the file with the same name.|False|Boolean|false|





#### Search Events
Search events in Crowdstrike. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Repository|Repository that should be searched.|True|List|All|
|Query|Query that needs to be executed in Crowdstrike. Note: don't provide "head" as part of the query. Action will provide it automatically based on the value provided in the "Max Results To Return" parameter.|True|String||
|Time Frame|Time frame for the results. If "Custom" is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.|False|String||
|End Time|End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|How many results to return for the query. Action will append "head" to the provided query. Default: 50. Maximum: 1000.|False|String|50|








## Jobs

#### Sync Alerts
This job will synchronize Google SecOps Alerts and Crowdstrike alerts. The job synchronizes comments and status. Requires “Crowdstrike Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” or “Identity Protections Detection Connector” you will need to add an “Alert_ID” context value for the job to be able to find the correct information.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|String|Default Environment|
|API Root|True|String|https://api.crowdstrike.com|
|Client ID|True|String||
|Client Secret|True|Password|*****|
|Max Hours Backwards|False|Int|24|
|Verify SSL|False|Boolean|true|



## Connectors
#### Crowdstrike - Alerts Connector
Pull alerts from Crowdstrike. Dynamic List works with the "display_name" parameter. Note: To fetch identity protection detections use "Identity Protection Detections Connector".

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.|False|String||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Int|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration. Default: 10.|True|Int|10|
|Include Hidden Alerts|If enabled, connector will also fetch alerts that are labeled as "hidden" by Crowdstrike.|False|Boolean|true|
|Fallback Severity|Fallback severity for the SecOps alert that should be applied to the Crowdstrike alerts, which are missing severity information. Possible values: Informational, Low, Medium, High, Critical. If nothing is provided, connector will use "Informational" severity.|False|String|Informational|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|Boolean|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|String||


#### Crowdstrike - Detections Connector
Deprecated. Pull detections from Crowdstrike. Whitelist works with filters that are supported by the API of Crowdstrike. For the details, please refer to the documentation portal.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical.|False|String|50|
|Lowest Confidence Score To Fetch|Lowest confidence score of the detections to fetch. If nothing is provided, the connector won't apply this filter. Maximum is 100.|False|Int|0|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|1|
|Max Detections To Fetch|How many detections to process per one connector iteration. Default: 10.|False|Int|10|
|Padding Period|The number of hours that connector will use for padding. Maximum: 6.|False|Int|1|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|String||


#### Crowdstrike - Identity Protection Detections Connector
Pull Identity Protection detections from Crowdstrike. Note: this connector requires an Identity Protection license. Dynamic List works with the “display_name” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Lowest Severity Score To Fetch|Lowest severity score of the identity protection detections to fetch. If nothing is provided, the connector will ingest detections with all severities. Maximum is 100. Note: action also supports the following values: Informational, Low, Medium, High, Critical.|False|String||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve detections from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|1|
|Max Detections To Fetch|How many identity protection detections to process per one connector iteration. Default: 10.|False|Int|10|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|Boolean|true|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Google Secops Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Google Secops Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Google Secops Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|String||


#### Crowdstrike Falcon Streaming Events Connector
Crowdstrike Falcon Streaming Events Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If environment field isn't found, environment is ""|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.|False|String||
|API Root|API root of the Crowdstrike instance|False|String|https://api.crowdstrike.com|
|Client ID|Client ID for Crowdstrike API|True|String||
|Client Secret|Client Secret for Crowdstrike API|True|Password|*****|
|Event types|Specify a comma-separated list of event types. Examples of the event types: DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent. For more information visit documentation portal.|False|String|DetectionSummaryEvent, IncidentSummaryEvent, UserActivityAuditEvent, RemoteResponseSessionStartEvent, RemoteResponseSessionEndEvent, EppDetectionSummaryEvent|
|Max Events per Cycle|Max events to process per connector run.|True|Int|100|
|Max Day Backwards|Number of days before the first connector iteration to retrieve events from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|3|
|Min Severity|Specify the events that should be ingested based on the events severity (detections events). The value ranges from 0-5. If other event types besides detections are ingested by the connector, connector sets a severity for them as -1 and this filter is not applied to those types of events|False|Int|0|
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Rule Generator Template|	If provided, the connector will use this value for Siemplify Rule Generator. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use the first Siemplify event for placeholders. Only keys that have string value will be handled. If nothing is provided or the user provides an invalid template, the connector will use the default rule generator.|False|String||
|Proxy Server Address|Proxy server address.|False|String||
|Proxy Username|Proxy username.|False|String||
|Proxy Password|Proxy password.|False|Password|*****|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|Boolean|false|
|Verify SSL|Indicate whether to use SSL in the session or not|False|Boolean|false|
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|String||


#### Crowdstrike - Incidents Connector
Deprecated. Pull incident and related behaviors from Crowdstrike. Dynamic List works with the “incident_type” parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Crowdstrike instance.|True|String|https://api.crowdstrike.com|
|Client ID|Client ID  of the Crowdstrike account.|True|String||
|Client Secret|Client Secret of the Crowdstrike account.|True|Password|*****|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default: 1|False|String|1|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Lowest Severity Score To Fetch|Lowest severity score of the incidents to fetch. If nothing is provided, the connector will ingest incidents with all severities. Maximum is 100. Note: action also supports the following values: Low, Medium, High, Critical. In the Crowdstrike UI the same value is presented as divided by 10.|False|String||
|Max Incidents To Fetch|How many incidents to process per one connector iteration. Default: 10. Max: 100.|False|String|10|
|Use dynamic list as a blocklist|If enabled, the dynamic list will be used as a blocklist.|False|Boolean|false|
|Disable Overflow|If enabled, connector will ignore the overflow mechanism.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Crowdstrike server is valid.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Customer ID|The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.|False|String||





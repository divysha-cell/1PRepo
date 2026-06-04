
# SCCEnterprise

SCC Enterprise integration to set up the SCC Enterprise env

Python Version - V3_11


#### Dependencies
| |
|-|
|proto_plus-1.27.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|keyring-25.5.0-py3-none-any.whl|
|Jinja2-3.1.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|defusedxml-0.7.1-py2.py3-none-any.whl|
|importlib_metadata-8.5.0-py3-none-any.whl|
|jeepney-0.8.0-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|Markdown-3.7-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|anyio-4.12.0-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|httplib2-0.31.0-py3-none-any.whl|
|certifi-2025.11.12-py3-none-any.whl|
|cachetools-6.2.4-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|backports.tarfile-1.2.0-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|jaraco.functools-4.1.0-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|requests_oauthlib-2.0.0-py2.py3-none-any.whl|
|jira-3.2.0-py3-none-any.whl|
|pyparsing-3.3.1-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|oauthlib-3.2.2-py3-none-any.whl|
|pillow-11.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_core-2.28.1-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_python_client-2.187.0-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|jaraco.classes-3.4.0-py3-none-any.whl|
|packaging-24.2-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl|
|urllib3-2.6.2-py3-none-any.whl|
|zipp-3.21.0-py3-none-any.whl|
|google_auth-2.45.0-py2.py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|TIPCommon-2.2.20-py2.py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|jaraco.context-6.0.1-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|more_itertools-10.5.0-py3-none-any.whl|
|protobuf-6.33.2-cp39-abi3-manylinux2014_x86_64.whl|
|pycparser-2.23-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|SecretStorage-3.3.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Create SCC Enterprise Cloud Posture Ticket Type SNOW
This action will create a new ticket type called "SCC Enterprise Cloud Posture Ticket" in ServiceNow. It’s a mandatory requirement for the "Sync SCC-ServiceNow Tickets" job and "Posture Findings with SNOW" playbook to work.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the ServiceNow instance.|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|Username of the ServiceNow account.|True|String|None|
|Password|Password of the ServiceNow account.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ServiceNow is valid.|False|Boolean|None|
|Table Role|Specify the role that should be set to access the newly created table. If nothing is provided, action will create a new role "u_scc_enterprise_cloud_posture_ticket_user".|False|String|None|



#### Lock Playbook
This action will enforce only one playbook being executed for given Posture case.
Timeout - 600 Seconds



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Set SCC-FINDINGS-STATE Context Value
Set "SCC-FINDINGS-STATE" context value that is used by the "Sync SCC Data" job, action "Prepare Description" and ITSM jobs.
Timeout - 600 Seconds



#### Add SCCE Tags
Add all of the SCCE metadata tags to the case.
Timeout - 600 Seconds



#### CloudEntityParser
Parse GCP related Entities from am existing alert's events data, and adds them to the alert.
Timeout - 600 Seconds



#### Create SCC Enterprise Cloud Posture Ticket Type Jira
This action will create a new ticket type called SCC Enterprise Cloud Posture Ticket” in Jira. It’s a mandatory requirement for the “Sync SCC-Jira Tickets” job and “Posture Findings with Jira” playbook to work. Note: as a part of the process, action will create a new project SCC Enterprise Project” dedicated to SCC Enterprise.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Jira instance.|True|String||
|Username|Username of the Jira account.|True|String||
|API Token|Password of the Jira account.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to Jira is valid.|False|Boolean|true|



#### Prepare Description
Prepare description for ITSM ticket.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Output|Output|False|List|HTML|






## Jobs

#### Sync SCC Data
This job will synchronize Google Security Command Center based cases created by the "Urgent Posture Findings Connector".

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|String|Default Environment|
|API Root|True|String|https://securitycenter.googleapis.com|
|Organization ID|True|String||
|Location ID|False|String|global|
|PubSub Project ID|False|String||
|Quota Project ID|False|String||
|User Service Account|False|Password|*****|
|Workload Identity Email|False|String||
|Max Hours Backwards|True|Int|24|
|Verify SSL|False|Boolean|true|

#### Sync SCC-Jira Tickets
This job will synchronize tickets in the Jira and Chronicle SOAR case. As a part of synchronization the job will work with comments and status of Chronicle SOAR cases.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|API Root|True|String|https://{jira_address}|
|Username|True|String||
|API Token|True|Password|*****|
|Max Hours Backwards|True|Int|24|
|Verify SSL|False|Boolean|true|

#### Sync SCC-ServiceNow Tickets
This job will synchronize tickets in the ServiceNow and Chronicle SOAR case. As a part of synchronization the job will work with comments and status of Chronicle SOAR cases.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|Time Format|True|String|%Y-%m-%d %H:%M:%S|
|API Root|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|True|String||
|Password|True|Password|*****|
|Max Hours Backwards|True|String|24|
|Verify SSL|False|Boolean|true|



## Connectors
#### SCC Enterprise - Urgent Posture Findings Connector
Pull information about urgent posture findings in Google Security Command Center.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic.If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Google Security Command Center instance.|True|String|https://securitycenter.googleapis.com|
|Organization ID|ID of the organization that should be used in Google Security Command Center integration.|True|String||
|Location ID|ID of the location that should be used in Google Security Command Center integration. Defaults to ‘global’|False|String|global|
|PubSub Project ID|ID of the project that will be used in the integration to host the Pub/Sub Topic and Subscription connection.|False|String||
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the “Service Usage Consumer” IAM role to your Google Cloud service account.|False|String||
|User Service Account|Service Account that is used for authentication. If both this and "Workload Identity Email" not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password|*****|
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account. If both this and "User's Service Account" not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|String||
|Owner Tag Name|Name of the tag that contains information about the owner of the finding.|False|String|Owner Name|
|Fallback Owner|Email address of the owner of the alerts created by this connector.|True|String||
|Group By GCP Project|If enabled, the connector will group findings by project.|False|Boolean|true|
|Group By AWS Account|If enabled, the connector will group findings by AWS account.|False|Boolean|true|
|Group By Azure Subscription|If enabled, the connector will group findings by Azure subscription.|False|Boolean|true|
|Group By Severity|If enabled, the connector will group findings by severity.|False|Boolean|true|
|Group By Asset Type|If enabled, the connector will group findings by asset type.|False|Boolean|true|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Security Command Center server is valid.|False|Boolean|true|
|Disable Overflow|If enabled, the connector will disable the overflow mechanism.|False|Boolean|true|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





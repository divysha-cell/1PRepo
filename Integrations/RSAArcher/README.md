
# RSAArcher

The RSA Archer Platform provides a centralized, flexible foundation that you can use to automate, integrate, manage and report on your organization's risk.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|IP_OR_HOST|http://x.x.x.x/rsaarcher|
|Instance Name|None|True|String||
|Username|None|True|String||
|Password|None|True|Password|*****|
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|xmltodict-0.13.0-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|requests-2.31.0-py3-none-any.whl|


## Actions
#### Get Incident Details
Retrieve information about the incident from RSA Archer.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Content ID|Specify ID of the content for which you want to retrieve details.|True|String||
|Application Name|Specify an application name for the incident. Default: Incidents.|False|String|Incidents|



#### Create Incident
Create a new incident
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Summary|The summary of the new incident.|False|String||
|Application Name|Specify an application name for the incident. Default: Incidents.|False|String|Incidents|
|Incident Details|The details (description) of the new incident.|False|String||
|Incident Owner|The owner of the new incident.|False|String||
|Incident Status|The status of the new incident.|False|String||
|Priority|The priority of the new incident.|False|String||
|Category|The category of the new incident.|False|String||
|Custom Fields|Specify a JSON object of fields that need to be used, when creating an incident . Example: {“Category”:“Malware”}.|False|String||
|Custom Mapping File|Specify an absolute path to the file that contains all of the required mapping. If “Remote File“ is enabled, then provide a URL that contains the mapping file. Please refer to action documentation for the additional information.|False|String||
|Remote File|If enabled, action will treat value provided in “Custom Mapping File“ as a URL and try to fetch a file from it.|False|Boolean|false|



#### Add Incident Journal Entry
Add a journal entry to the Security Incident in RSA Archer.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Destination Content ID|Specify a content id of the security incident to which you want to add journal entry.|True|String||
|Text|Specify the text for the journal entry.|True|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Update Incident
Update an incident
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Content ID|Content Id of the incident to update.|True|String||
|Application Name|Specify an application name for the incident. Default: Incidents.|False|String|Incidents|
|Incident Summary|The new summary of the incident.|False|String||
|Incident Details|The new details (decsription) of the incident.|False|String||
|Incident Owner|The new owner of the incident.|False|String||
|Incident Status|The new status of the incident.|False|String||
|Priority|The new priority of the incident.|False|String||
|Category|The new category of the incident.|False|String||
|Custom Fields|Specify a JSON object of fields that need to be updated. Example: {“Category”:“Malware”}.|False|String||
|Custom Mapping File|Specify an absolute path to the file that contains all of the required mapping. If “Remote File“ is enabled, then provide a URL that contains the mapping file. Please refer to action documentation for the additional information.|False|String||
|Remote File|If enabled, action will treat value provided in “Custom Mapping File“ as a URL and try to fetch a file from it.|False|Boolean|false|






## Jobs

#### Sync Security Incidents
This job will synchronize security incidents in RSA Archer and Siemplify.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|http://x.x.x.x/RSAarcher|
|Instance Name|True|String||
|Username|True|String||
|Password|True|Password|*****|
|Sync Fields|True|String||
|Verify SSL|False|Boolean|true|



## Connectors
#### RSA Archer - Security Incidents Connector
Pull Security Incidents from RSA Archer.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API Root of the RSA Archer instance.|True|String|http://x.x.x.x/RSAarcher|
|Instance Name|Name of the RSA Archer instance.|True|String||
|Username|Username of the RSA Archer account. |True|String||
|Password|Password of the RSA Archer account.|True|Password|*****|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve security incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|1|
|Max Security Incidents To Fetch|How many security incidents to process per one connector iteration.|False|Int|50|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Process Security Alerts|If enabled, connector will process Security Alerts related to the Security Incident.|False|Boolean|true|
|Process Incident Journal|If enabled, connector will process Incident Journal related to the Security Incident.|False|Boolean|true|
|Time Format|Specify, what should be the time format for the searching of Security Incidents.|True|String|%Y-%m-%d %H:%M:%S|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the RSA Archer server is valid.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





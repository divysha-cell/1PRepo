
# GoogleCloudAssetInventory

Cloud Asset Inventory is a fully-managed service that helps you discover, monitor, and analyze your Google Cloud and Anthos assets across projects and services. Cloud Asset Inventory provides a comprehensive view of your assets, including their configuration, relationships, and usage. This information can be used to improve your security posture, optimize your costs, and make better decisions about your cloud resources.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Google Cloud Asset Inventory instance.|True|String|https://cloudasset.googleapis.com|
|Organization ID|ID of the organization that should be used in Google Cloud Asset Inventory integration.|False|String||
|Project ID|ID of the Project that should be used in Google Cloud Asset Inventory integration. Takes precedence over "Organization ID".|False|String||
|User Service Account|Service account of the Google Cloud Asset Inventory instance. A full content of the service account JSON file should be provided. This or "Workload Identity Email" must be provided.|False|Password|*****|
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the "Service Usage Consumer" IAM role to your Google Cloud service account.|False|String||
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Cloud Asset Inventory server is valid.|False|Boolean|true|
|API Root|API root of the Google Cloud Asset Inventory instance.|True|String|https://cloudasset.googleapis.com|
|Organization ID|ID of the organization that should be used in Google Cloud Asset Inventory integration.|False|String||
|Project ID|ID of the Project that should be used in Google Cloud Asset Inventory integration. Takes precedence over "Organization ID".|False|String||
|User Service Account|Service account of the Google Cloud Asset Inventory instance. A full content of the service account JSON file should be provided. This or "Workload Identity Email" must be provided.|False|Password|*****|
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the "Service Usage Consumer" IAM role to your Google Cloud service account.|False|String||
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Cloud Asset Inventory server is valid.|False|Boolean|true|


#### Dependencies
| |
|-|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|proto_plus-1.24.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|TIPCommon-1.1.6.1-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|protobuf-5.27.3-cp38-abi3-manylinux2014_x86_64.whl|
|certifi-2024.7.4-py3-none-any.whl|
|google_api_core-2.19.1-py3-none-any.whl|
|pyparsing-3.1.4-py3-none-any.whl|
|google_api_python_client-2.142.0-py2.py3-none-any.whl|
|google_auth-2.34.0-py2.py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.63.2-py2.py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|regex-2024.7.24-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cachetools-5.5.0-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|


## Actions
#### Enrich Resource
Enrich information about a Google Cloud resource using Google Cloud Asset Inventory.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Names|Specify a comma-separated list of resources for which you want to fetch details.|True|String||
|Fields To Return|Specify a comma-separated list of fields to return. Example of values:assetType,project,folders,organization,displayName,description,location,labels,networkTags,kmsKeys,createTime,updateTime,state,additionalAttributes, parentFullResourceName, parentAssetType. Note: name will always be returned. There is also an option to provide more advanced filters. For example, if you want to return a specific key from the "additionalAttributes" you can provide "additionalAttributes.{key}". Also, if you want to exclude a specific key from "additionalAttributes",then you can provide "-additionalAttributes.{key}".|False|String|*|



#### Get Resource Snapshot
Get information about the resource using Google Cloud Asset Inventory.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Resource Names|Specify a comma-separated list of resources for which you want to fetch details.|True|String||
|Fields To Return|Specify a comma-separated list of fields to return. Note: every field should be in format with "assets.{field}" Example of values:assets.asset.name, assets.asset.assetType,assets.asset.resource.data.Note: assets.asset.name will always be returned.|False|String|*|



#### List Service Account Roles
List roles related to the Google Cloud service account using Google Cloud Asset Inventory.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Service Accounts|Specify a comma-separated list of service accounts for which you want to fetch details.|True|String||
|Check Roles|Specify a comma-separated list of roles that you want to check in relation to the service account. Example: roles/cloudasset.owner|False|String||
|Check Permissions|Specify a comma-separated list of permission that you want to check in relation to the service account. Example: cloudasset.assets.listResource.|False|String||
|Expand Permissions|If enabled, action will return information about all of the unique permissions related to the resource.|False|Boolean|false|
|Max Roles To Return|Specify how many roles related to the service account to return.|True|String|100|
|Max Permissions To Return|Specify how many permissions related to the service account to return.|True|String|100|



#### Ping
Test connectivity to the Google Cloud Asset Inventory with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds











# GoogleCloudRecommender

Google Cloud Recommender is a service that provides recommendations and insights for using resources on Google Cloud. These recommendations and insights are per-product or per-service, and are generated based on heuristic methods, machine learning, and current resource usage. Currently integration supports insights only from google.iam.policy.Recommender recommender.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Google Recommender service.|True|String||
|Resource Manager API Root|API root of the Google Cloud Resource Manager service.|True|String||
|Organization ID|ID of the organization that can be used with the Cloud Recommender integration.|False|String||
|Project ID|ID of the project that should be used in the integration. Takes priority over Organization ID, if both are provided.|False|String||
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the “Service Usage Consumer” IAM role to your Google Cloud service account.|False|String||
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account.|False|String||
|User Service Account|Service account of the Google Recommender service. A full content of the service account JSON file should be provided. This or "Workload Identity Email" must be provided.|False|Password||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Recommender service is valid.|False|Boolean||


#### Dependencies
| |
|-|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|proto_plus-1.24.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|TIPCommon-1.1.6.1-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|protobuf-5.27.3-cp38-abi3-manylinux2014_x86_64.whl|
|certifi-2024.7.4-py3-none-any.whl|
|google_api_core-2.19.1-py3-none-any.whl|
|pyparsing-3.1.4-py3-none-any.whl|
|google_api_python_client-2.142.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|google_auth-2.34.0-py2.py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.63.2-py2.py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|


## Actions
#### Apply IAM Recommendations
Apply IAM Recommendations based on provided input. Action works only with google.iam.policy.Recommender recommendations.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IAM Recommendations JSON|Specify the JSON of the recommendation to apply to. JSON can be provided as a placeholder from “List Recommendations” or “Get Recommendation” actions.|True|None||



#### Ping
Test connectivity to the Google Recommender service with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Update Recommendation
Update recommendation in the Google Cloud Recommender service. Note 1: This action doesn’t run on Chronicle SOAR entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recommendation Name|Specify the recommendation name to update. Action accepts multiple values as a comma separated string. Example of expected input: projects/projectname/locations/global/recommenders/google.iam.policy.Recommender/recommendations/0f262740-bf4a-4c3d-9573-0da3345cf3f7|True|None||
|Recommendation State|Specify the state for the recommendation to change to.|False|None||
|Recommendation Result|Specify the result for the recommendation to change to.|False|None||



#### List Recommendations
List available recommendations in the Google Cloud Recommender service. Note 1: This action doesn’t run on Chronicle SOAR entities. Note 2: Currently action returns insights only from google.iam.policy.Recommender recommender.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recommendation Filter|Specify the filter to fetch the recommendations for. Parameter expects a string of a format "<projects or organizations>/<project or organization name or id>" or "//cloudresourcemanager.googleapis.com/<projects or organizations>/<project or organization name or id>" for which to fetch the recommendations for. If nothing is provided - action will take the project id from the service account configured.|False|None||
|Recommendation Location|Specify the GCP location to fetch recommendations for.|True|None||
|Recommendation State|Specify the recommendation state to return.|False|None||
|Recommendation Priority|Specify the recommender priority to return, multiple values can be specified as a comma separated string.|False|None||
|Recommender Subtype|Specify the recommender subtype to return.|False|None||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|None||



#### Get Recommendation
Get specific recommendation from the Google Cloud Recommender service. Note 1: This action doesn’t run on Chronicle SOAR entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recommendation Name|Specify the recommendation name to return. Action accepts multiple values as a comma separated string. Example of expected input: projects/projectname/locations/global/recommenders/google.iam.policy.Recommender/recommendations/0f262740-bf4a-4c3d-9573-0da3345cf3f7|True|None||










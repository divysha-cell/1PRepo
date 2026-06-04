
# Silverfort

Silverfort identity security platform integration for Google SecOps.

In case of any queries, please reach out to support@silverfort.com.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|Base URL for Silverfort API (e.g., https://your-instance.silverfort.io)|True|String|https://your-silverfort-instance.com|
|External API Key|External API Key from Silverfort Admin Console (X-Console-API-Key header)|True|Password|*****|
|Risk App User ID|App User ID for Risk API credentials|False|String||
|Risk App User Secret|App User Secret for Risk API credentials|False|Password|*****|
|Service Accounts App User ID|App User ID for Service Accounts API credentials|False|String||
|Service Accounts App User Secret|App User Secret for Service Accounts API credentials|False|Password|*****|
|Policies App User ID|App User ID for Policies API credentials|False|String||
|Policies App User Secret|App User Secret for Policies API credentials|False|Password|*****|
|Verify SSL|If selected, the integration validates the SSL certificate when connecting to Silverfort API|False|Boolean|true|


#### Dependencies
| |
|-|
|proto_plus-1.27.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|PyJWT-2.10.1-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|certifi-2026.1.4-py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|google_api_core-2.29.0-py3-none-any.whl|
|httplib2-0.31.0-py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|protobuf-6.33.4-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|TIPCommon-2.2.10-py2.py3-none-any.whl|
|pyparsing-3.3.1-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_python_client-2.187.0-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Ping
Use the Ping action to test connectivity to Silverfort API. This action validates that the External API Key is working and tests connectivity for each configured API (Risk, Service Accounts, Policies) using their respective credentials.
Timeout - 600 Seconds



#### Get Entity Risk
Get risk information for a user or resource from Silverfort. Returns the current risk score, severity, and risk factors. You must provide either the User Principal Name (for users) or Resource Name (for resources).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Principal Name|The user principal name (e.g., user@domain.com). Either this or Resource Name must be provided.|False|String||
|Resource Name|The resource name for non-user entities. Either this or User Principal Name must be provided.|False|String||



#### Change Policy State
Enable or disable an authentication policy in Silverfort. This is a quick way to toggle a policy's active state without modifying its configuration.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy ID|The ID of the policy to enable or disable.|True|String||
|Enable Policy|Set to true to enable the policy, false to disable it.|False|Boolean|true|



#### Update Entity Risk
Update risk information for a user in Silverfort. This allows you to set a specific risk level for a user based on external threat intelligence or security events.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Principal Name|The user principal name (e.g., user@domain.com) to update risk for.|True|String||
|Risk Type|The type of risk to update.|True|List|activity_risk|
|Severity|The severity level of the risk.|True|List|medium|
|Valid For Hours|How long (in hours) the risk indicator should be valid.|True|String|24|
|Description|Description of the risk indicator.|True|String||



#### Update SA Policy
Update the protection policy for a service account in Silverfort. Allows configuring blocking, SIEM logging, risk level thresholds, protocols, and allowed sources/destinations.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Service Account GUID|The GUID of the service account whose policy to update.|True|String||
|Enabled|Enable or disable the policy.|False|Boolean||
|Block|Enable or disable blocking for policy violations.|False|Boolean||
|Send to SIEM|Enable or disable SIEM logging.|False|Boolean||
|Risk Level|Risk level threshold for the policy.|False|List||
|Allow All Sources|Allow all sources (if true, ignores specific allowed sources list).|False|Boolean||
|Allow All Destinations|Allow all destinations (if true, ignores specific allowed destinations list).|False|Boolean||
|Protocols|Comma-separated list of protocols to allow (Kerberos, ldap, ntlm).|False|String||
|Add Allowed Sources|JSON array of sources to add to the allowlist. Format: [{"key": "10.0.0.1", "key_type": "ip"}]|False|String||
|Remove Allowed Sources|JSON array of sources to remove from the allowlist. Format: [{"key": "10.0.0.1", "key_type": "ip"}]|False|String||
|Add Allowed Destinations|JSON array of destinations to add to the allowlist. Format: [{"key": "10.0.0.1", "key_type": "ip"}]|False|String||
|Remove Allowed Destinations|JSON array of destinations to remove from the allowlist. Format: [{"key": "10.0.0.1", "key_type": "ip"}]|False|String||



#### Update Policy
Update an authentication policy in Silverfort. Allows modifying the policy's enabled state and adding/removing users, groups, sources, and destinations.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy ID|The ID of the policy to update.|True|String||
|Enabled|Enable or disable the policy.|False|Boolean||
|Add Users and Groups|JSON array of users/groups to add to the policy. Format: [{"identifierType": "upn", "identifier": "user@domain.com", "displayName": "User Name", "domain": "domain.com"}]|False|String||
|Remove Users and Groups|JSON array of users/groups to remove from the policy. Format: [{"identifierType": "upn", "identifier": "user@domain.com", "displayName": "User Name", "domain": "domain.com"}]|False|String||
|Add Sources|JSON array of sources to add to the policy. Format: [{"identifierType": "ip", "identifier": "10.0.0.1", "displayName": "Server"}]|False|String||
|Remove Sources|JSON array of sources to remove from the policy. Format: [{"identifierType": "ip", "identifier": "10.0.0.1", "displayName": "Server"}]|False|String||
|Add Destinations|JSON array of destinations to add to the policy. Format: [{"identifierType": "hostname", "identifier": "server.domain.com", "displayName": "Server", "domain": "domain.com", "services": ["rdp"]}]|False|String||
|Remove Destinations|JSON array of destinations to remove from the policy. Format: [{"identifierType": "hostname", "identifier": "server.domain.com", "displayName": "Server", "domain": "domain.com", "services": ["rdp"]}]|False|String||



#### List Service Accounts
List service accounts from Silverfort with optional pagination and field filtering. Returns a list of service accounts with their attributes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Page Size|Number of results per page (1-100).|False|String|50|
|Page Number|Page number to retrieve.|False|String|1|
|Fields|Comma-separated list of fields to include in the response. Available fields: guid, display_name, sources_count, destinations_count, number_of_authentications, risk, predictability, protected, upn, dn, spn, comment, owner, type, domain, category, creation_date, highly_privileged, interactive_login, broadly_used, suspected_brute_force, repetitive_behavior. If not specified, all fields are returned.|False|String||



#### List Policies
List all authentication policies from Silverfort with optional field filtering. Returns a list of policies with their configurations.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields|Comma-separated list of fields to include in the response. Available fields: enabled, policyName, authType, protocols, policyType, allUsersAndGroups, usersAndGroups, allDevices, sources, allDestinations, destinations, action, MFAPrompt, all, bridgeType. If not specified, all fields are returned.|False|String||



#### Get Service Account
Get detailed information about a specific service account from Silverfort by its GUID. Returns the service account's attributes including risk, predictability, protection status, and more.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Service Account GUID|The GUID of the service account to retrieve.|True|String||



#### Get Policy
Get detailed information about a specific authentication policy from Silverfort by its ID. Returns the policy configuration including users, groups, sources, destinations, and action settings.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy ID|The ID of the policy to retrieve.|True|String||










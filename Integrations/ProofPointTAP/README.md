
# ProofPointTAP

Proofpoint Targeted Attack Protection™ is the industry's first comprehensive solution for combatting targeted threats using a full lifecycle approach, monitoring suspicious messages containing malicious URLs or malicious attachments, and observing user clicks as they attempt to reach out.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://tap-api-v2.proofpoint.com|
|Username|None|True|String||
|Password|None|True|Password|*****|
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|urllib3-2.3.0-py3-none-any.whl|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_auth-2.38.0-py2.py3-none-any.whl|
|google_api_core-2.24.2-py3-none-any.whl|
|TIPCommon-2.2.0-py2.py3-none-any.whl|
|cachetools-5.5.2-py3-none-any.whl|
|certifi-2025.1.31-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|googleapis_common_protos-1.69.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|pycryptodome-3.22.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.10-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|typing_extensions-4.13.0-py3-none-any.whl|
|anyio-4.9.0-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|protobuf-6.30.2-cp39-abi3-manylinux2014_x86_64.whl|
|pyparsing-3.2.3-py3-none-any.whl|
|google_api_python_client-2.166.0-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|httpcore-1.0.7-py3-none-any.whl|


## Actions
#### List Campaigns
Use the List Campaigns action to return a list of active campaigns in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Time Frame|Time frame for the results. If “Custom” is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.|False|String||
|End Time|End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|How many results to return. Default: 50. Maximum: 1000.|True|String|50|



#### GetCampaign
Return information about campaigns in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Campaign ID|Specify a comma-separated list of campaign IDs for which you want to return info.|True|String||
|Create Insight|If enabled, action will create an insight containing information about the campaign.|False|Boolean|true|
|Create Threat Campaign Entity|If enabled, action will create a threat campaign entity from the enriched campaigns.|False|Boolean|true|
|Fetch Forensics Info|If enabled, action will return forensics information about the campaigns.|False|Boolean|true|
|Forensic Evidence Type Filter|Specify a comma-separated list of evidence types that need to be returned, when fetching forensic info. Possible values: attachment, cookie, dns, dropper, file, ids, mutex, network, process, registry, screenshot, url, redirect_chain, behavior.|False|String|attachment,dns, dropper, file, network, process, registry, screenshot, url, redirect_chain|
|Max Forensics Evidence To Return|Specify how much evidence to return per campaign. Default: 50. Maximum: 1000.|False|String|50|



#### Ping
Test connectivity to the Proofpoint TAP with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Search Events
Use the Search Events action to search events in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event Type|Type of the event that needs to be returned.|False|List|All|
|Threat Status|Status of threat that needs to be returned. If "Select One" is provided, then action will return “Active” and “Cleared” threats.|False|List|Select One|
|Time Frame|Time frame for the results. If “Custom” is selected, you also need to provide "Start Time".|False|List|Last Hour|
|Start Time|Start time for the results. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601.|False|String||
|End Time|End time for the results. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Results To Return|How many results to return. Default: 50. Maximum: 1000.|True|String|50|



#### DecodeURL
Decode URLs in Proofpoint TAP. Supported entities: URL.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Encoded URLs|Specify a comma-separated list of URLs that need to be decoded. Note: URL entities in the scope of the alert will be decoded together.|False|String|None|
|Create URL Entities|If enabled, action will create URL entities that were successfully decoded.|False|Boolean|true|



#### Get Threat Forensics
Use the Get Threat Forensics action to return forensics associated with a threat in Proofpoint TAP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threat ID|Comma-separated list of threat IDs for which forensics need to be returned.|True|String||
|Include Campaign Forensics|If enabled, action will also return campaign forensics related to the provided threat.|False|Boolean|false|
|Max Results To Return|How many results to return per threat id. Default: 50. Maximum: 1000.|True|String|50|










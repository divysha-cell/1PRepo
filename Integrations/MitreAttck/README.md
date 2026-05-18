
# MitreAttck

MITRE ATT&CK™ is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|IP_OR_HOST||
|Verify SSL|None|False|Boolean||


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
|idna-3.7-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl|
|google_api_core-2.30.0-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|googleapis_common_protos-1.73.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|sniffio-1.3.1-py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|pyasn1-0.6.3-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|TIPCommon-2.3.8-py3-none-any.whl|


## Actions
#### Get Techniques Details
Retrieve detailed information about MITRE attack techniques.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Technique Identifier|Specify the identifier that will be used to find the detailed information about technique. Comma-separated values.|True|None||
|Identifier Type|Specify what identifier type to use. Possible values: Name (Example: Access Token Manipulation) ID (Example: attack-pattern--478aa214-2ca7-4ec0-9978-18798e514790) External ID (Example: T1050)|True|None||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Get Technique Details
Retrieve detailed information about MITRE attack technique
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Technique Identifier|Specify the comma-separated list of identifiers that will be used to find the detailed information about techniques. Example: identifier_1,identifier_2|True|None||
|Identifier Type|Specify what identifier type to use. Possible values: Name (Example: Access Token Manipulation) ID (Example: attack-pattern--478aa214-2ca7-4ec0-9978-18798e514790) External ID (Example: T1050)|True|None||
|Create Insights|If enabled, action will create a separate insight for every processed technique|False|None||



#### Get Mitigations
Retrieve information about mitigations that are associated with MITRE attack technique
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Technique ID|Specify the identifier that will be used to find the mitigations related to attack technique.|True|None||
|Identifier Type|Specify what identifier type to use. Possible values: Attack Name (Example: Access Token Manipulation) Attack ID (Example: attack-pattern--478aa214-2ca7-4ec0-9978-18798e514790) External Attack ID (Example: T1050)|True|None||
|Max Mitigations to Return|Specify how many mitigations to return.|False|None||



#### Get Techniques Mitigations
Retrieve information about mitigations that are associated with MITRE attack techniques.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Technique ID|Specify the identifier that will be used to find the mitigations related to attack technique. Comma-separated values.|True|None||
|Identifier Type|Specify what identifier type to use. Possible values: Attack Name (Example: Access Token Manipulation) Attack ID (Example: attack-pattern--478aa214-2ca7-4ec0-9978-18798e514790) External Attack ID (Example: T1050)|True|None||
|Max Mitigations to Return|Specify how many mitigations to return.|False|None||



#### Get Associated Intrusions
Retrieve information about intrusions that are associated with MITRE attack technique.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Technique ID|Specify the identifier that will be used to find the associated intrusions.|True|None||
|Identifier Type|Specify what identifier type to use. Possible values: Attack Name (Example: Access Token Manipulation) Attack ID (Example: attack-pattern--478aa214-2ca7-4ec0-9978-18798e514790) External Attack ID (Example: T1050)|True|None||
|Max Intrusions to Return|Specify how many intrusions to return.|False|None||










ReadmeAddon
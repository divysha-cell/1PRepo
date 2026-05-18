
# DomainTools

DomainTools turns threat data into threat intelligence. Assess risk of domains and augment malware intel with domain data. In case of any queries, please reach out to memberservices@domaintools.com

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Username||True|String||
|ApiToken||True|String||
|Verify SSL||False|Boolean||


#### Dependencies
| |
|-|
|requests-2.32.5-py3-none-any.whl|
|shellingham-1.5.4-py2.py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|certifi-2026.1.4-py3-none-any.whl|
|domaintools_api-2.7.2-py2.py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|google_api_core-2.29.0-py3-none-any.whl|
|annotated_doc-0.0.4-py3-none-any.whl|
|proto_plus-1.27.1-py3-none-any.whl|
|protobuf-6.33.5-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|click-8.3.1-py3-none-any.whl|
|rich-14.3.2-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|mdurl-0.1.2-py3-none-any.whl|
|idna-3.11-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|
|markdown_it_py-4.0.0-py3-none-any.whl|
|TIPCommon-2.3.0-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|typer-0.21.2-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|pygments-2.19.2-py3-none-any.whl|
|pycparser-2.23-py3-none-any.whl|
|EnvironmentCommon-1.0.3-py3-none-any.whl|
|pyasn1-0.6.2-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Get Domain Rdap
Enrich external domain entity with DomainTools threat Intelligence data and return CSV output
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domain|The domain to get the parsed domain RDAP result.|False|None||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Get WhoIs History
Enrich external domain entity with DomainTools threat Intelligence data and return CSV output
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domain|The domain to get the whois history result.|False|None||



#### Investigate Domain
Enrich external domain entity with DomainTools Iris Investigate and return CSV output
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domain|The domain to investigate.|False|None||











# EmailUtilities

A set of utility actions to assist with working with emails.  Includes actions to parse EMLs and analyze email headers.

Python Version - V3_11


#### Dependencies
| |
|-|
|proto_plus-1.27.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|xmltodict-1.0.2-py3-none-any.whl|
|dicttoxml-1.7.16-py3-none-any.whl|
|pycares-4.8.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|tzlocal-5.3.1-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|tldextract-5.3.1-py3-none-any.whl|
|platformdirs-4.5.1-py3-none-any.whl|
|netaddr-1.3.0-py3-none-any.whl|
|defusedxml-0.7.1-py2.py3-none-any.whl|
|dnspython-2.7.0-py3-none-any.whl|
|certifi-2026.1.4-py3-none-any.whl|
|python_magic-0.4.27-py2.py3-none-any.whl|
|red-black-tree-mod-1.20.tar.gz|
|msoffcrypto_tool-6.0.0-py3-none-any.whl|
|timeout-decorator-0.5.0.tar.gz|
|anyio-4.12.1-py3-none-any.whl|
|geocoder-1.38.1-py2.py3-none-any.whl|
|dkimpy-1.1.8.tar.gz|
|expiringdict-1.2.2-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|file_magic-0.4.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|extract_msg-0.52.0-py3-none-any.whl|
|aiodns-3.4.0-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|oletools-0.60.2-py2.py3-none-any.whl|
|rtfde-0.1.2.2-py3-none-any.whl|
|google_api_core-2.29.0-py3-none-any.whl|
|easygui-0.98.3-py2.py3-none-any.whl|
|setuptools-80.10.2-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|decorator-5.2.1-py3-none-any.whl|
|ebcdic-1.1.1-py2.py3-none-any.whl|
|urlextract-1.9.0-py3-none-any.whl|
|pyleri-1.4.3.tar.gz|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|html2text-2024.2.26.tar.gz|
|lark-1.3.1-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|ipwhois-1.3.0-py2.py3-none-any.whl|
|click-8.3.1-py3-none-any.whl|
|future-1.0.0-py3-none-any.whl|
|uritools-6.0.1-py3-none-any.whl|
|protobuf-6.33.4-py3-none-any.whl|
|soupsieve-2.8.3-py3-none-any.whl|
|filelock-3.20.3-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|eml_parser-2.0.0-py3-none-any.whl|
|tld-0.13-py2.py3-none-any.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|checkdmarc-5.7.11-py2.py3-none-any.whl|
|pcodedmp-1.2.6-py2.py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.11-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|
|olefile-0.47-py2.py3-none-any.whl|
|pem-23.1.0-py3-none-any.whl|
|pydnsbl-1.1.7-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|TIPCommon-2.3.0-py3-none-any.whl|
|compressed_rtf-1.0.6.tar.gz|
|publicsuffixlist-1.0.2.20260126-py2.py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|dnslib-0.9.25-py3-none-any.whl|
|colorclass-2.2.2-py2.py3-none-any.whl|
|ioc_fanger-4.2.1-py2.py3-none-any.whl|
|ratelim-0.1.6-py2.py3-none-any.whl|
|msg_parser-1.2.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.3-py3-none-any.whl|
|requests_file-3.0.1-py2.py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|six-1.17.0-py2.py3-none-any.whl|
|pyasn1-0.6.2-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Parse EML Base64 Blob
This action will decode a base64 string and attempt to parse it as an EML file.  It will return a list of parsed objects.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 EML Blob|A base64 encoded string of an EML file.|True|String|<base64encoded_string>|



#### Analyze EML Headers
This actions gets a base64 EML or list of headers and extracts/analyses its headers
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 EML|Base64 string of an EML file.|False|String||
|Header List|Headers list in a JSON format.|False|String||



#### Analyze Headers
Analyze Headers accepts a JSON object containing a list of Email headers.  The action will validate the SPF, DMARC, ARC, and DKIM records in the email.  It will also check to see if any of the relay servers are denylisted by querying multiple RBLs and enrich them with geo-location and IP whois information.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Headers JSON|The JSON object that contains the email headers.|True|String|{}|



#### Ping
Check connectivity
Timeout - 600 Seconds



#### Parse Case Wall Email
This action will parse an EML or MSG file that has been attached to the case wall.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Entities|When enabled, this will create User entities out of the To and From headers and a Email Subject entity out of the Subject field. |False|Boolean|true|
|Exclude Entities Regex|Observed entities that match the supplied regex will not be created.|False|String||
|Original EML Only|Extract attachments from the original EML only.|False|Boolean|true|
|Create Observed Entities|Create Entities out of the observed entities in the email body.'All' will create URL, Email, IP, and Hash entities.|False|List|All|
|Save Attachments to Case Wall|Save the extracted attachments to the case wall.|False|Boolean|true|
|Fang Entities|When enabled, entities that are defanged (example.com => example[.]com) will be converted to fanged entities.|False|Boolean|true|
|Custom Entity Regexes|A JSON object that can parse out entities from body and subject.|False|Code|{ }|



#### Parse Base64 Email
This action is an improved version of Parse EML Base64 blob.  It will parse EML and MSG files.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Stop Transport At Header|Stop processing the transport at this header field.|False|String|None|
|EML/MSG Base64 String|The base64 representation of an EML or MSG file.|True|Content|<insert base64 string>|
|Blacklisted Headers|Headers to exclude from the response.|False|String|None|
|Use Blacklist As Whitelist|To only include the listed headers.|False|Boolean|false|










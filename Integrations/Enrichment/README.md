
# Enrichment

A set of entity enrichment actions to assist in the managing of entity attributes.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Key|SOAR API Key - Required to Enrich Entities from Explorer|False|Password|*****|
|Verify SSL|Verify SSL Certificates when executing requests to Chronicle SOAR instance.|False|Boolean|false|


#### Dependencies
| |
|-|
|proto_plus-1.27.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|tldextract-5.3.1-py3-none-any.whl|
|defusedxml-0.7.1-py2.py3-none-any.whl|
|certifi-2026.1.4-py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|geocoder-1.38.1-py2.py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|jsonpath_ng-1.7.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|dnspython-2.8.0-py3-none-any.whl|
|argparse-1.4.0-py2.py3-none-any.whl|
|google_api_core-2.29.0-py3-none-any.whl|
|setuptools-80.10.2-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|decorator-5.2.1-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|ipwhois-1.3.0-py2.py3-none-any.whl|
|click-8.3.1-py3-none-any.whl|
|future-1.0.0-py3-none-any.whl|
|protobuf-6.33.4-py3-none-any.whl|
|filelock-3.20.3-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.11-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|TIPCommon-2.3.0-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|ratelim-0.1.6-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.3-py3-none-any.whl|
|requests_file-3.0.1-py2.py3-none-any.whl|
|six-1.17.0-py2.py3-none-any.whl|
|pyasn1-0.6.2-py3-none-any.whl|
|ply-3.11-py2.py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|whois_alt-2.5.0.tar.gz|


## Actions
#### Enrich Entity From Event Field
The action extracts fields from the event and adds them to the Entity fields
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields to enrich|The name of the fields in the event that will be used to enrich the entity.  Supports comma separated list.|True|String|field_name_1,field_name_2|



#### Enrich Entity With Field
The action adds enrichment fields to the entity based on a list of key values 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields to enrich|Takes a list of key/value pairs and enriches the entity with that data. Can be used to add multiple static values easily.|True|String|[   {     "entity_field_name": "Title",     "entity_field_value": "SalseManager"   },   {     "entity_field_name": "City",     "entity_field_value": "NewYork"   } ]|



#### Enrich Entity from Explorer Attributes
Enriches entities with historic enrichment data using the entity explorer.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Field Name|The field(s) from the Entity Explorer that will be used to enrich the entity. When null all fields will be enriched. Supports comma delimited string.|False|String||
|Use Field Name as Whitelist|When true, entities will be enriched with fields from 'Field Name' param.  When False, the list will be used as a denylist and all other fields added|False|Boolean|true|



#### Whois
Query WHOIS servers for domain registration information.  Supports IP Addresses, URLs, Email, Domains.  Supports creation of DOMAIN entities linked to target entity and a domain age threshold to set the entity to suspicious. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Entities|Create and link domain entities to URL and Email / User names.|False|Boolean|true|
|Domain Age Threshold|Domains who's age is less than the than the supplied days will be marked suspicious.  |False|String||



#### Enrich FileName Entity with Path
This action will parse out path, file name, and extension from an entity and enrich it with file_path, file_name, and file_extension.
Timeout - 600 Seconds



#### Mark Entity as Suspicious
This action will mark the entities in the scope as suspicious.
Timeout - 600 Seconds



#### Ping
Check connectivity
Timeout - 600 Seconds



#### Enrich Entities from List with Field
This action enriches entities supplied by a list with a field and a value.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|List of Entities|A list of entities of the same type, delimited by a field.|True|String||
|Entity Type|The type of entity.|True|String| |
|Entity Delimiter|The value of the field that is delimiting the list of entities.|True|String|,|
|Enrichment Field|The name of the field that will be added to the entity.|True|String| |
|Enrichment Value|The value of the field that will be enriched to the entity.|True|String| |



#### Enrich Source and Destinations
This action will add the source and destination links to IPs and hostnames in the alert.
Timeout - 600 Seconds



#### Enrich Entity From JSON
The action extracts fields from a json file and adds them to the entity fields
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enrichment JSON| JSON from which you would like to enrich an entity. (List of JSONs)|True|String|[   {     "EntityResult": {       "permalink": "https://www.virustotal.com/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/analysis/1549381312/",       "sha1": "3395856ce81f2b7382dee72602f798b642f14140",       "resource": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F",       "response_code": 1,       "scan_date": "2019-02-05 15:41:52",       "scan_id": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f-1549381312",       "verbose_msg": "Scan finished, information embedded",       "total": 60,       "positives": 54,       "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",       "md5": "44d88612fea8a8f36de82e1278abb02f",       "scans": {         "Bkav": {           "detected": true,           "version": "1.1.1.1",           "result": "DOS.EiracA.Trojan",           "update": "20190201"         },         "MicroWorld-eScan": {           "detected": true,           "version": "1.1.1.1",           "result": "EICAR-Test-File",           "update": "20190205"         }       }     },     "Entity": "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F"   } ]|
|Identifier KeyPath|KeyPath to the Entity Identifier in the JSON|True|String|key1.key2|
|Separator|The "Separator" for the keypath. For example, if its XXX then the example would be:key1XXXkey2|True|String|.|
|PrefixForEnrichment|What prefix to use for enrichment|False|String|None|
|Enrichment JSONPath|JSONPath expressions always refers to a JSON structure in the same way as XPath expressions are used in combination with an XML document.|False|String|None|










Read123!@#
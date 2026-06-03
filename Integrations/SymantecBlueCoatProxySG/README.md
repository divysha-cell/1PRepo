
# SymantecBlueCoatProxySG

Symantec delivers its high-performance, proxy-based, Edge Secure Web Gateway (SWG) solution where you need it: on high-performance hardware, as a virtual appliance, or in your private cloud infrastructure. Symantec's industry-leading proxy protects organizations across the web, social media, applications, and mobile networks

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SSH Root|SSH root of the Blue Coat ProxySG instance.|True|String|{ip address}:22|
|Username|Username of the Blue Coat ProxySG SSH account.|True|String||
|Password|Password of the Blue Coat ProxySG account.|True|Password|*****|


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|cryptography-43.0.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyOpenSSL-24.2.1-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|urllib3-2.2.3-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl|
|idna-3.10-py3-none-any.whl|
|paramiko-3.1.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|bcrypt-4.2.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Block Entities
Block entities using Symantec Blue Coat ProxySG. Supported entities: IP Address.
Timeout - 600 Seconds



#### Enrich Entities
Enrich entities using information from Symantec Blue Coat ProxySG. Supported entities: Hostname, IP Address, URL.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insight|If enabled, action will create an insight containing all of the retrieved information about the entity.|False|Boolean|true|



#### Ping
Test connectivity to the Symantec Blue Coat ProxySG with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds










Read123!@#
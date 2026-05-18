
# Houdin-io

Houdin.io provides automated AI cyber threat analysis, reducing the time and effort required to analyze and respond to cyber threats.

This connector allows you to connect Houdin.io with your SOAR platform, enabling automated threat analysis and response workflows.

Support Contact: support@houdin.io

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Key|Your Houdin API key. Used to launch scans, retrieve data, etc.|True|Password||
|Verify SSL|Enable or disable SSL verification.|False|Boolean||


#### Dependencies
| |
|-|
|pluggy-1.6.0-py3-none-any.whl|
|pytest-8.4.1-py3-none-any.whl|
|packaging-25.0-py3-none-any.whl|
|pygments-2.19.2-py3-none-any.whl|
|iniconfig-2.1.0-py3-none-any.whl|


## Actions
#### Enrich Entities
Scan compatible entities on Houdin.io, and add enrichment results for each one. Compatible types are: Public IPv4/IPv6, URL, Domain, MD5, SHA1, SHA256 Note: Action is running as async, adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|scanOn|(Optional) An array of scanners you want Houdin to use.|False|None||



#### Ping
Test the connectivity to the Houdin.io API.
Timeout - 600 Seconds



#### Scan Artifact
Launch a Houdin scan on a given artifact, and retrieve all results. The action returns automatically when your scan is done. Compatible types are: Public IPv4/IPv6, URL, Domain, MD5, SHA1, SHA256 Note: Action is running as async, adjust script timeout value in Google SecOps IDE for action, as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|artifact|An artifact to scan on the Houdin.io platform. Currently supported types: IPv4, IPv6, URL, Domain, MD5, SHA1, SHA256|True|None||
|scanOn|(Optional) An array of scanners you want Houdin to use.|False|None||










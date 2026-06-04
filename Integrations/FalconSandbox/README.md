
# FalconSandbox

Falcon Sandbox is a high end malware analysis framework with a very agile architecture.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root||True|String|https://<server-address>/api/v2|
|Api Key||True|Password|*****|
|Threshold||True|Int|50.0|


#### Dependencies
| |
|-|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|idna-3.13-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|chardet-7.4.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|requests-2.32.4-py3-none-any.whl|
|certifi-2026.4.22-py3-none-any.whl|


## Actions
#### Ping
Test connectivity to Falcon Sandbox
Timeout - 600 Seconds



#### Scan URL
Scan URL/domain for analysis.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Threshold|Mark entity as suspicious if number of av detection is equal or above the given threshold|True|String||
|Environment|The environment to use for the scan.|True|List|Linux (Ubuntu 16.04, 64 bit)|



#### Get Hash Scan Report
Fetch hybrid analysis reports and enrich file hash entities
Timeout - 600 Seconds



#### Submit File
Submit files for analysis
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Path|The full path of the file to analyze. For multiple, use comma separated values.|True|String||
|Environment|The environment to use for the scan.|True|List|Linux (Ubuntu 16.04, 64 bit)|



#### Wait For Job and Fetch Report
Wait for a scan job to complete and fetch the scan report.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Job ID|The job id to fetch report for. For multiple, use comma separated values.|True|String||



#### Analyze File
Submit a file for analysis and fetch report
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Path|The full path of the file to analyze|True|String||
|Environment|Environment ID. e.g. 100 (100=Windows 7 32 bit)|True|String||
|Include Report|If enabled, action will fetch report related to the attachment. Note: this feature requires a premium key.|False|Boolean|true|



#### Search
Search Falcon databases for existing scan reports and information about files, and file Urls
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Name|Filename e.g. invoice.exe|False|String||
|File Type|e.g. docx|False|String||
|File Type Description|e.g. PE32 executable|False|String||
|Verdict|e.g. 1 (1=whitelisted, 2=no verdict, 3=no specific threat, 4=suspicious, 5=malicious)|False|String||
|AV Multiscan Range|e.g. 50-70 (min 0, max 100)|False|String||
|AV Family Substring|e.g. Agent.AD, nemucod|False|String||
|Hashtag|e.g. ransomware|False|String|None|
|Port|e.g. 8080|False|String|None|
|Host|x.x.x.x|False|String|None|
|Domain|e.g. checkip.dyndns.org|False|String|None|
|HTTP Request Substring|e.g. google|False|String|None|
|Similar Samples|e.g. <sha256>|False|String|None|
|Sample Context|e.g. <sha256>|False|String|None|



#### Analyze File Url
Submit a file by URL for analysis and fetch report
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Url|The url to the file to analyze. e.g. http://tamzamaninda.net/office/Document.zip|True|String||
|Environment|Environment ID. e.g. 100 (100=Windows 7 32 bit)|True|String||










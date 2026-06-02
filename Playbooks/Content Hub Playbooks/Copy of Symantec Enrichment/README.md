# Copy of Symantec Enrichment
This block supports remediation by retrieving system information for endpoints and listing all endpoints/sensors and groups configured on a specified Symantec-managed device, providing the necessary context for follow-up actions. It receives a boolean Scan Endpoint input; when set to true, the endpoint will be scanned.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|
|Scan Endpoint|False|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|List Endpoints| List all the endpoints/sensors configured on a particular device|SEP|ListEndpoints|
|Get System Info|Get system information for endpoints|SEP|GetSystemInfo|
|ScanEndpoint|Scan an endpoint|SEP|ScanEndpoint|
|List Groups|List all the groups configured on a particular device|SEP|ListGroups|


# enrichment block
An embedded workflow that can receive inputs and return an output.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|
|ALERT|[Alert.Name]|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|VirusTotal_Ping_1|Test Connectivity|VirusTotal|Ping|
|ActiveDirectory_Enrich entities_1|Enrich entities with Active Directory properties|ActiveDirectory|Enrich entities|
|VirusTotal_Scan Hash_1|Scan Hash via VirusTotal. *Mark entity as suspicious and show insights if risk score matches a given threshold.|VirusTotal|Scan Hash|
|VirusTotal_Scan IP_1|Scan IP via VirusTotal. Returns table of reverse domains and full Json result|VirusTotal|Scan IP|


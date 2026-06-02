# Copy of Nw Playbook




**Enabled:** False

**Version:** 0

**Type:** Playbook

**Priority:** 1

**Playbook Simulator:** False



### Playbook Trigger
**Trigger Type:** All

**Conditions Operator:** And

##### Conditions
|Key|Operator|Value|
|---|--------|-----|
||Equals||



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Siemplify_Ping_1|Test Connectivity|Siemplify|Ping|
|Siemplify_Case Tag_1|Add given tag to the case the current alert is grouped to|Siemplify|Case Tag|
|CrowdStrikeFalcon_List Hosts_1|List available hosts in Crowdstrike Falcon.|CrowdStrikeFalcon|List Hosts|


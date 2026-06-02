# Copy of 1New Playbook




**Enabled:** False

**Version:** 0

**Type:** Playbook

**Priority:** 1

**Playbook Simulator:** True



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
|CrowdStrikeFalcon_Ping_1|Test Connectivity|CrowdStrikeFalcon|Ping|
|GitSync_Ping_1|Test connectivity to GitSync|GitSync|Ping|

### Involved Blocks
|Name|Description|
|----|-----------|
|Alert Priority|This block sets the alert priority using a previously defined playbook variable, ensuring consistent prioritization logic for the case workflow.|
|Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|

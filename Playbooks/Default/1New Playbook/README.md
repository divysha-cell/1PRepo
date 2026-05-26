# 1New Playbook




**Enabled:** True

**Version:** 1

**Type:** Playbook

**Priority:** 2

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
|CrowdStrikeFalcon_Ping_1|Test Connectivity|CrowdStrikeFalcon|Ping|
|GitSync_Ping_1|Test connectivity to GitSync|GitSync|Ping|

### Involved Blocks
|Name|Description|
|----|-----------|
|Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Alert Priority|This block sets the alert priority using a previously defined playbook variable, ensuring consistent prioritization logic for the case workflow.|
A paragraph is a self-contained unit of writing consisting of one or more sentences that develop a single, controlling idea. It serves as a structural building block in prose, allowing writers to break complex ideas into digestible pieces and guiding readers through different points
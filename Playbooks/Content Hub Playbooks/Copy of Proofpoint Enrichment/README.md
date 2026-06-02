# Copy of Proofpoint Enrichment
This block uses the List Campaigns action to retrieve a list of active campaigns in Proofpoint TAP, providing relevant information to support investigation and threat analysis activities.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Search Events|Use the Search Events action to search events in Proofpoint TAP.|ProofPointTAP|Search Events|
|List Campaigns|Use the List Campaigns action to return a list of active campaigns in Proofpoint TAP.|ProofPointTAP|List Campaigns|


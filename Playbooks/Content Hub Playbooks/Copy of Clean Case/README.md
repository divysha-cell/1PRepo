# Copy of Clean Case
Clean case (Tags, Alert scoring info, etc) when playbooks that are often rerun and can create duplicate evidence.  Extend this logic to meet your requirements. 



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|
|TagsToKeep|Simulated Case,Manual Case|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Remove tags|Remove tags from a case.|Siemplify|Remove Tag|
|Reset "Alert Scoring Info"|The action sets a key and value in a specific context (alert or case)|Tools|Set Context Value|
|Get Case Data for Tags|This action will get all the data from a case and return a JSON result.  The result includes comments, entity information, insights, playbooks that ran, alert information and events.|Tools|Get Case Data|
|Filter out allowed tags|Compare all Case tags to the allowed tags.  Output a list of tags to be removed.|TemplateEngine|Render Template|


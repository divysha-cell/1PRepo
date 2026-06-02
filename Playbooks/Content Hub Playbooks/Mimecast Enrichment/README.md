# Mimecast Enrichment
This block performs an investigation by searching archived emails in Mimecast based on specified parameters and returns relevant information to support analysis and response activities within the case.



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
|Mimecast Search|Search archive emails using defined parameters in Mimecast. Note: when providing time make sure to take in the account timezones. For ease of use, Siemplify instance and Mimecast instance should be in the same timezone.|Mimecast|Simple Archive Search|
|Mimecast Search: SenderEmail|Search archive emails using defined parameters in Mimecast. Note: when providing time make sure to take in the account timezones. For ease of use, Siemplify instance and Mimecast instance should be in the same timezone.|Mimecast|Simple Archive Search|


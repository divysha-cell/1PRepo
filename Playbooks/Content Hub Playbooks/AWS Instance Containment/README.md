# AWS Instance Containment
This block allows you to stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|
|Manual|True|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Count Ec2|Count the number of entities from a specific scope.|SiemplifyUtilities|Count Entities In Scope|


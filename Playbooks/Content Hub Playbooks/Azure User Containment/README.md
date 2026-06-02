# Azure User Containment
This block applies containment actions to Azure user accounts by resetting passwords or disabling accounts. A boolean input controls manual or automatic mode. In automatic mode, the Disable Account and Password Reset flags determine which actions run. It returns true if successful, false on failure, or empty if no action is taken.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|
|Manual|True|
|Disable Account|True|
|Password Reset|True|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Count Users|Count the number of entities from a specific scope.|SiemplifyUtilities|Count Entities In Scope|


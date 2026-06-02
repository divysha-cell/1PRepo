# Copy of Google Workspace User Containment
This block allows the playbook to update Google Workspace user accounts as part of containment or response actions, supporting account management and security controls. It uses a boolean input to control whether execution is manual or automatic. When running automatically, the Disable Account and Password Reset boolean inputs determine which actions are performed and which are ignored.



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
|List Users|List users present in account.|GSuite|List Users|
|Update User|Update a Google Workspace Directory user. Note: action is not working on Google SecOps entities|GSuite|Update User|


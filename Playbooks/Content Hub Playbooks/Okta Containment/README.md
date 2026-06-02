# Okta Containment
This block performs remediation on Okta users by generating a one‑time token for password resets or disabling accounts. A boolean input controls manual or automatic mode. In automatic mode, the Disable Account and Password Reset flags determine which actions run. It returns the remediation result, false on failure, or empty if no action is taken.



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
|Disable Users|Disables the specified user|Okta|Disable User|
|Reset Passwords|Generate a one-time token that can be used to reset a user's password|Okta|Reset Password|
|Get Users|Get information about a user|Okta|Get User|
|Reset Password Auto|Generate a one-time token that can be used to reset a user's password|Okta|Reset Password|
|Disable User Auto|Disables the specified user|Okta|Disable User|


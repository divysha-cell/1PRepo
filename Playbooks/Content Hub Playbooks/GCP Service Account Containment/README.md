# GCP Service Account Containment
This block disables one or more GCP service accounts as part of containment actions. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.



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
|Disable Service Account|Disable service account. Action expects IAM service account email as a Siemplify User entity.|GoogleCloudIAM|Disable Service Account|
|Auto Disable Service Account|Disable service account. Action expects IAM service account email as a Siemplify User entity.|GoogleCloudIAM|Disable Service Account|


# Carbon Black Cloud Remediation




**Enabled:** True

**Version:** 0

**Type:** Playbook

**Priority:** 1

**Playbook Simulator:** True



### Playbook Trigger
**Trigger Type:** Custom Trigger

**Conditions Operator:** And

##### Conditions
|Key|Operator|Value|
|---|--------|-----|
|[Alert.DeviceProduct] |Contains|Carbon|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|CBCloud_Disable Bypass Mode for Device_1|Create disable bypass mode task for devices on the VMware Carbon Black Cloud server based on the Siemplify IP or Host Siemplify entities.|CBCloud|Disable Bypass Mode for Device|
|AD - Get User Info|Get information about the user that violated the  policy.|AzureActiveDirectory|Enrich User|
|VirusTotal_Scan Hash_1|Scan Hash via VirusTotal. *Mark entity as suspicious and show insights if risk score matches a given threshold.|VirusTotal|Scan Hash|
|STAGE: Investigation|Change case stage to: Investigation|Siemplify|Change Case Stage|
|STAGE: Incident|Change case stage to: Incident|Siemplify|Change Case Stage|
|CBLiveResponse_Kill Process_1|Kill process on a host based on the Siemplify Host or IP entity. Note: The Process name can be provided either as a Siemplify entity (artifact) or as an action input parameter. If the Process name is passed to action both as an entity (process) and input parameter - action will be executed on the input parameter.|CBLiveResponse|Kill Process|
|CBCloud_Quarantine Device|Quarantine affected device.|CBCloud|Quarantine Device|
|CBEnterpriseEDR_Enrich Hash_1|Enrich Siemplify File hash entity based on the information from the VMware Carbon Black Enterprise EDR. Note: Action accepts file hashes only in SHA256 format!|CBEnterpriseEDR|Enrich Hash|
|CBEnterpriseEDR_Process Search_1|Search information about process activity on the host with CB sensor based on the provided search parameters. The action accepts Host Siemplify entities.|CBEnterpriseEDR|Process Search|
|Insights_Create Entity Insight From Multiple JSONs_1|The action creates HOST entity insight from multiple json files. |Insights|Create Entity Insight From Multiple JSONs|
|CBCloud_Enrich Entities|Get more information about the affected endpoint (by hostname or IP) and files/processes.|CBCloud|Enrich Entities|
|EmailV2_Send Email_1|Send email message. Requires: SMTP configuration|EmailV2|Send Email|
|SiemplifyUtilities_Count List_1|Count malicious entities after enrichment in TI|SiemplifyUtilities|Count List|
|Siemplify_Add General Insight_6|Insight about failed process kill|Siemplify|Add General Insight|
|CBCloud_Enable Bypass Mode for Device_1|Create enable bypass mode task for device on VMware Carbon Black Cloud server based on Siemplify IP or Host Siemplify entities.|CBCloud|Enable Bypass Mode for Device|
|INSIGHT - Process Kill|Inform user about process kill|Siemplify|Add General Insight|
|INSIGHT - Quarantine|Inform analyst about quarantine|Siemplify|Add General Insight|
|INSIGHT - Action Taken|Affected device moved to restricted policy.|Siemplify|Add General Insight|
|INSIGHT - Process Not Found|Add a general insight configurable message to the case|Siemplify|Add General Insight|
|Close Case (FP)|Restricted policy already applied. Close the case.|Siemplify|Close Case|
|Siemplify_Change Priority_1|Automatically change case priority to the given input|Siemplify|Change Priority|
|CBCloud_Update a Policy for Device by Policy ID|Move the affected device to a restricted policy|CBCloud|Update a Policy for Device by Policy ID|
|Close Case (Quarantined)|Closes the case|Siemplify|Close Case|
|INSIGHT - Policy Information|Provide an insight about the policy applied|Siemplify|Add General Insight|


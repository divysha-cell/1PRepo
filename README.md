# GitSync

## Playbooks
|Name|Description|
|----|-----------|
|AWS EC2 Containment|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|AWS Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|AWS Instance Containment|This block allows you to stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|AWS User Containment|This block allows you to disable access for users referenced in the case, supporting containment actions during the incident response process. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|AWS Users Containment|An embedded workflow that can receive inputs and return an output.|
|Amazon Web Services Cloud Platform Starting Playbook|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Azure User Containment|This block applies containment actions to Azure user accounts by resetting passwords or disabling accounts. A boolean input controls manual or automatic mode. In automatic mode, the Disable Account and Password Reset flags determine which actions run. It returns true if successful, false on failure, or empty if no action is taken.|
|GTI Enrichment|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|MITRE Enrichment|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|SecMon_Enrichment_and_Triage_Block|An embedded workflow that can receive inputs and return an output.|
|Nw Playbook||
|Carbon Black Cloud Remediation||
|Copy of Carbon Black Cloud Remediation - 1||


## Visual Families
|Name|Description|
|----|-----------|
|AV_THBn|newaddedmanually|


## Jobs
|Name|Description|
|----|-----------|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/158/jobInstances/76|Automated test job instance configured by script. Index: 47|
|projects/project/locations/location/instances/instance/integrations/AzureSecurityCenter/jobs/189/jobInstances/72|Automated test job instance configured by script. Index: 43|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/61/jobInstances/105|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/52|Automated test job instance configured by script. Index: 23|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/53|Automated test job instance configured by script. Index: 24|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/114|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/49|Automated test job instance configured by script. Index: 20|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/121|Automated test job instance configured by script. Index: 7|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/157/jobInstances/75|Automated test job instance configured by script. Index: 46|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/48|Automated test job instance configured by script. Index: 19|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/51|Automated test job instance configured by script. Index: 22|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/63/jobInstances/106|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/104|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/63/jobInstances/96|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/50|Automated test job instance configured by script. Index: 21|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/61/jobInstances/95|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/94|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/63/jobInstances/86|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/84|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/63/jobInstances/31|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/61/jobInstances/30|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/CaServiceDesk/jobs/191/jobInstances/55|Automated test job instance configured by script. Index: 26|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/118|Automated test job instance configured by script. Index: 4|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/122|Automated test job instance configured by script. Index: 8|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/74|Automated test job instance configured by script. Index: 45|
|projects/project/locations/location/instances/instance/integrations/NessusScanner/jobs/142/jobInstances/60|Automated test job instance configured by script. Index: 31|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/117|Automated test job instance configured by script. Index: 3|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/120|Automated test job instance configured by script. Index: 6|
|projects/project/locations/location/instances/instance/integrations/MicrosoftGraphMailDelegated/jobs/146/jobInstances/64|Automated test job instance configured by script. Index: 35|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/56|Automated test job instance configured by script. Index: 27|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/61/jobInstances/85|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/140/jobInstances/58|Automated test job instance configured by script. Index: 29|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/61/jobInstances/115|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/139/jobInstances/57|Automated test job instance configured by script. Index: 28|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/123|Automated test job instance configured by script. Index: 9|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/141/jobInstances/59|Automated test job instance configured by script. Index: 30|
|projects/project/locations/location/instances/instance/integrations/BMCRemedyITSM/jobs/193/jobInstances/79|Automated test job instance configured by script. Index: 50|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/159/jobInstances/77|Automated test job instance configured by script. Index: 48|
|projects/project/locations/location/instances/instance/integrations/CaServiceDesk/jobs/192/jobInstances/54|Automated test job instance configured by script. Index: 25|
|projects/project/locations/location/instances/instance/integrations/MicrosoftAzureSentinel/jobs/144/jobInstances/62|Automated test job instance configured by script. Index: 33|
|projects/project/locations/location/instances/instance/integrations/MicrosoftAzureSentinel/jobs/143/jobInstances/61|Automated test job instance configured by script. Index: 32|
|projects/project/locations/location/instances/instance/integrations/RSAArcher/jobs/155/jobInstances/73|Automated test job instance configured by script. Index: 44|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/164/jobInstances/82|Automated test job instance configured by script. Index: 53|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/165/jobInstances/83|Automated test job instance configured by script. Index: 54|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/160/jobInstances/78|Automated test job instance configured by script. Index: 49|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/119|Automated test job instance configured by script. Index: 5|


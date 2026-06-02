# GitSync

## Integrations
|Name|Description|
|----|-----------|
|AbuseIPDB|Leverage the AbuseIPDB threat intelligence API with this integration.|
|Active Directory|Microsoft Active Directory integration facilitates the centralized management and synchronization of Windows user accounts with Security Center's administrator and cardholder accounts.|
|AlienVault USM Appliance|USM Appliance includes the essential security capabilities and continuously delivered threat intelligence needed to quickly and easily identify and respond to threats in your physical and virtual infrastructure.|
|Connectors|A set of custom connectors created for Google SecOps Community to power up automation capabilities.|
|Exchange|Integration provides support for Microsoft Exchange 2010 - 2019 and Microsoft Office365 mail servers. Integration uses Exchange Web Services (EWS) for communication. Integration includes a series of actions to send out emails and work with received emails, along with a connector to monitor specific mailboxes and ingest emails from that mailboxes as alerts to Google SecOps for further analysis.|
|GitSync|Sync Google SecOps integrations, playbooks, and settings with a GitHub, BitBucket or GitLab instance|


## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|cdemnAlienVault USM Appliance Connector|asdfghjgfdsadfghjhgfdsdfghj|False|
|Anomali Staxx - Indicators Connector|Pull indicators from Anomali Staxx|True|
|Apache Kafka - Messages Connector|The Apache Kafka Connector retrieves messages from Apache Kafka.|False|
|Azure AD Identity Protection - Risk Detections Connector|Pull information about risk detections from Azure AD Identity Protection. Note: whitelist filter works with "riskEventType" parameter.|False|
|DRP Violations Connector|DRP Violations Connector|False|


## Playbooks
|Name|Description|
|----|-----------|
|AWS EC2 Containment|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|AWS EC2 Containment - 1|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|AWS EC2 Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|AWS Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|AWS Enrichment - 1|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|AWS Instance Containment|This block allows you to stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|AWS User Containment|This block allows you to disable access for users referenced in the case, supporting containment actions during the incident response process. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|AWS User Containment - 1|This block allows you to disable access for users referenced in the case, supporting containment actions during the incident response process. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|AWS User Containment - 2|This block allows you to disable access for users referenced in the case, supporting containment actions during the incident response process. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|AWS Users Containment|An embedded workflow that can receive inputs and return an output.|
|AWS Users Containment - 1|An embedded workflow that can receive inputs and return an output.|
|Amazon Web Services Cloud Platform Starting Playbook|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Amazon Web Services Cloud Platform Starting Playbook - 1|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Azure User Containment|This block applies containment actions to Azure user accounts by resetting passwords or disabling accounts. A boolean input controls manual or automatic mode. In automatic mode, the Disable Account and Password Reset flags determine which actions run. It returns true if successful, false on failure, or empty if no action is taken.|
|Clean Case|Clean case (Tags, Alert scoring info, etc) when playbooks that are often rerun and can create duplicate evidence.  Extend this logic to meet your requirements.|
|Copy of AWS EC2 Containment|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|Copy of AWS EC2 Containment - 1|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|Copy of AWS EC2 Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of AWS Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of AWS Enrichment - 1|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of AWS Instance Containment|This block allows you to stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|Copy of AWS User Containment|This block allows you to disable access for users referenced in the case, supporting containment actions during the incident response process. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|Copy of AWS User Containment - 1|This block allows you to disable access for users referenced in the case, supporting containment actions during the incident response process. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|Copy of AWS User Containment - 2|This block allows you to disable access for users referenced in the case, supporting containment actions during the incident response process. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|Copy of AWS Users Containment|An embedded workflow that can receive inputs and return an output.|
|Copy of AWS Users Containment - 1|An embedded workflow that can receive inputs and return an output.|
|Copy of Amazon Web Services Cloud Platform Starting Playbook|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Copy of Amazon Web Services Cloud Platform Starting Playbook - 1|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Copy of Azure User Containment|This block applies containment actions to Azure user accounts by resetting passwords or disabling accounts. A boolean input controls manual or automatic mode. In automatic mode, the Disable Account and Password Reset flags determine which actions run. It returns true if successful, false on failure, or empty if no action is taken.|
|Copy of Clean Case|Clean case (Tags, Alert scoring info, etc) when playbooks that are often rerun and can create duplicate evidence.  Extend this logic to meet your requirements.|
|Copy of GCP Service Account Containment|This block disables one or more GCP service accounts as part of containment actions. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|Copy of GTI Enrichment|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of GTI Enrichment - 1|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Google SecOps Enrichment - 1|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Google SecOps SIEM Enrichment|This block enriches entities and retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Google Workspace User Containment|This block allows the playbook to update Google Workspace user accounts as part of containment or response actions, supporting account management and security controls. It uses a boolean input to control whether execution is manual or automatic. When running automatically, the Disable Account and Password Reset boolean inputs determine which actions are performed and which are ignored.|
|Copy of High Risk Entities|This block increases the alert risk score when risky entities from a custom list are detected. It receives the Custom List Category and a Risk Score Increase value as inputs, which are used to increase the alert score if matches are found. The block returns true if successful or false on failure.|
|Copy of MITRE Enrichment|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|Copy of MITRE Enrichment - 1|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|Copy of Mimecast Enrichment|This block performs an investigation by searching archived emails in Mimecast based on specified parameters and returns relevant information to support analysis and response activities within the case.|
|Copy of Okta Containment|This block performs remediation on Okta users by generating a one‑time token for password resets or disabling accounts. A boolean input controls manual or automatic mode. In automatic mode, the Disable Account and Password Reset flags determine which actions run. It returns the remediation result, false on failure, or empty if no action is taken.|
|Copy of Out Of Hours Check|This Block will check if the Alert is processing outside of typical business hours.  Some alert responses might react different (e.g. OOH escalation) at different parts of the day.|
|Copy of Proofpoint Enrichment|This block uses the List Campaigns action to retrieve a list of active campaigns in Proofpoint TAP, providing relevant information to support investigation and threat analysis activities.|
|Copy of Symantec Enrichment|This block supports remediation by retrieving system information for endpoints and listing all endpoints/sensors and groups configured on a specified Symantec-managed device, providing the necessary context for follow-up actions. It receives a boolean Scan Endpoint input; when set to true, the endpoint will be scanned.|
|Copy of Tag Case with time span|A Block that Tags the case with the time span between Alerts.  Can be used for Case queue filters.|
|GCP Service Account Containment|This block disables one or more GCP service accounts as part of containment actions. It uses a boolean input to control manual or automatic execution and returns the containment result, false on failure, or an empty value if no action is taken.|
|GTI Enrichment|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|GTI Enrichment - 1|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Google SecOps Enrichment - 1|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Google SecOps SIEM Enrichment|This block enriches entities and retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Google Workspace User Containment|This block allows the playbook to update Google Workspace user accounts as part of containment or response actions, supporting account management and security controls. It uses a boolean input to control whether execution is manual or automatic. When running automatically, the Disable Account and Password Reset boolean inputs determine which actions are performed and which are ignored.|
|High Risk Entities|This block increases the alert risk score when risky entities from a custom list are detected. It receives the Custom List Category and a Risk Score Increase value as inputs, which are used to increase the alert score if matches are found. The block returns true if successful or false on failure.|
|MITRE Enrichment|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|MITRE Enrichment - 1|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|Mimecast Enrichment|This block performs an investigation by searching archived emails in Mimecast based on specified parameters and returns relevant information to support analysis and response activities within the case.|
|Okta Containment|This block performs remediation on Okta users by generating a one‑time token for password resets or disabling accounts. A boolean input controls manual or automatic mode. In automatic mode, the Disable Account and Password Reset flags determine which actions run. It returns the remediation result, false on failure, or empty if no action is taken.|
|Out Of Hours Check|This Block will check if the Alert is processing outside of typical business hours.  Some alert responses might react different (e.g. OOH escalation) at different parts of the day.|
|Proofpoint Enrichment|This block uses the List Campaigns action to retrieve a list of active campaigns in Proofpoint TAP, providing relevant information to support investigation and threat analysis activities.|
|Symantec Enrichment|This block supports remediation by retrieving system information for endpoints and listing all endpoints/sensors and groups configured on a specified Symantec-managed device, providing the necessary context for follow-up actions. It receives a boolean Scan Endpoint input; when set to true, the endpoint will be scanned.|
|Tag Case with time span|A Block that Tags the case with the time span between Alerts.  Can be used for Case queue filters.|
|11Copy of New Playbook2 - 2||
|1New Playbook||
|2New Playbook||
|Copy of 11Copy of New Playbook2 - 2||
|Copy of 1New Playbook||
|Copy of 1New Playbook - 2||
|Copy of 1New Playbook - 3||
|Copy of 2New Playbook||
|Copy of 2New Playbook - 2||
|Copy of Copy of 1New Playbook||
|Copy of Copy of 1New Playbook - 2||
|Copy of Copy of 2New Playbook||
|Copy of Copy of New Playbook2||
|Copy of New Playbook||
|Copy of New Playbook1||
|Copy of New Playbook2||
|Copy of New Playbook2 - 2||
|Copy of Nw Playbook||
|New Playbook||
|New Playbook1||
|New Playbook2||
|Nw Playbook||
|Carbon Black Cloud Remediation||
|Copy of Carbon Black Cloud Remediation - 1||


## Jobs
|Name|Description|
|----|-----------|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/23|This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM. Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/158/jobInstances/76|Automated test job instance configured by script. Index: 47|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/167|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/181|Automated test job instance configured by script. Index: 14|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/215|Automated test job instance configured by script. Index: 48|
|projects/project/locations/location/instances/instance/integrations/AzureSecurityCenter/jobs/254/jobInstances/72|Automated test job instance configured by script. Index: 43|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/105|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/105|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/157|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/104|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/118|Automated test job instance configured by script. Index: 4|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/141/jobInstances/177|Automated test job instance configured by script. Index: 10|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/159|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/214|Automated test job instance configured by script. Index: 47|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/153|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/52|Automated test job instance configured by script. Index: 23|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/114|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/53|Automated test job instance configured by script. Index: 24|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/171|Automated test job instance configured by script. Index: 4|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/170|Automated test job instance configured by script. Index: 3|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/161|Automated test job instance configured by script. Index: 4|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/160|Automated test job instance configured by script. Index: 3|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/156|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/120|Automated test job instance configured by script. Index: 6|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/154|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/51|Automated test job instance configured by script. Index: 22|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/114|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/49|Automated test job instance configured by script. Index: 20|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/121|Automated test job instance configured by script. Index: 7|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/217|Automated test job instance configured by script. Index: 50|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/157/jobInstances/75|Automated test job instance configured by script. Index: 46|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/48|Automated test job instance configured by script. Index: 19|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/48|Automated test job instance configured by script. Index: 19|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/51|Automated test job instance configured by script. Index: 22|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/140/jobInstances/176|Automated test job instance configured by script. Index: 9|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/106|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/BMCRemedyITSM/jobs/256/jobInstances/79|Automated test job instance configured by script. Index: 50|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/159/jobInstances/77|Automated test job instance configured by script. Index: 48|
|projects/project/locations/location/instances/instance/integrations/CaServiceDesk/jobs/252/jobInstances/54|Automated test job instance configured by script. Index: 25|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/156|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/PaloAltoCortexXDR/jobs/203/jobInstances/149|This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/104|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/216|Automated test job instance configured by script. Index: 49|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/96|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/50|Automated test job instance configured by script. Index: 21|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/95|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/94|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/173|Automated test job instance configured by script. Index: 6|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/86|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/152||
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/84|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/172|Automated test job instance configured by script. Index: 5|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/31|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/198|Automated test job instance configured by script. Index: 31|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/29|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/163|Automated test job instance configured by script. Index: 6|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/162|Automated test job instance configured by script. Index: 5|
|projects/project/locations/location/instances/instance/integrations/MicrosoftGraphMailDelegated/jobs/146/jobInstances/28|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/24|This job will synchronize Google SecOps Alerts and Crowdstrike alerts. The job synchronizes comments and status. Requires “Crowdstrike Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” or “Identity Protections Detection Connector” you will need to add an “Alert_ID” context value for the job to be able to find the correct information.|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/151|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/50|Automated test job instance configured by script. Index: 21|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/122|Automated test job instance configured by script. Index: 8|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/30|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/119|Automated test job instance configured by script. Index: 5|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/121|Automated test job instance configured by script. Index: 7|
|projects/project/locations/location/instances/instance/integrations/CaServiceDesk/jobs/253/jobInstances/207|Automated test job instance configured by script. Index: 40|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/211|Automated test job instance configured by script. Index: 44|
|projects/project/locations/location/instances/instance/integrations/Tools/jobs/227/jobInstances/203|Automated test job instance configured by script. Index: 36|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/169|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/213|Automated test job instance configured by script. Index: 46|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/150||
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/122|Automated test job instance configured by script. Index: 8|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/157/jobInstances/182|Automated test job instance configured by script. Index: 15|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/157/jobInstances/226|Automated test job instance configured by script. Index: 59|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/74|Automated test job instance configured by script. Index: 45|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/225|Automated test job instance configured by script. Index: 58|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/23|This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM. Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/168|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/212|Automated test job instance configured by script. Index: 45|
|projects/project/locations/location/instances/instance/integrations/NessusScanner/jobs/142/jobInstances/178|Automated test job instance configured by script. Index: 11|
|projects/project/locations/location/instances/instance/integrations/NessusScanner/jobs/142/jobInstances/222|Automated test job instance configured by script. Index: 55|
|projects/project/locations/location/instances/instance/integrations/NessusScanner/jobs/142/jobInstances/60|Automated test job instance configured by script. Index: 31|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/158|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/152||
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/120|Automated test job instance configured by script. Index: 6|
|projects/project/locations/location/instances/instance/integrations/MicrosoftGraphMailDelegated/jobs/146/jobInstances/179|Automated test job instance configured by script. Index: 12|
|projects/project/locations/location/instances/instance/integrations/MicrosoftGraphMailDelegated/jobs/146/jobInstances/223|Automated test job instance configured by script. Index: 56|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/56|Automated test job instance configured by script. Index: 27|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/56|Automated test job instance configured by script. Index: 27|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/85|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/164/jobInstances/82|Automated test job instance configured by script. Index: 53|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/139/jobInstances/175|Automated test job instance configured by script. Index: 8|
|projects/project/locations/location/instances/instance/integrations/MicrosoftAzureSentinel/jobs/201/jobInstances/61|Automated test job instance configured by script. Index: 32|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/140/jobInstances/166|Automated test job instance configured by script. Index: 9|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/140/jobInstances/58|Automated test job instance configured by script. Index: 29|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/140/jobInstances/58|Automated test job instance configured by script. Index: 29|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/140/jobInstances/220|Automated test job instance configured by script. Index: 53|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/197|Automated test job instance configured by script. Index: 30|
|projects/project/locations/location/instances/instance/integrations/SentinelOneV2/jobs/245/jobInstances/148|This job will synchronize Google SecOps Alerts and SentinelOne alerts. The job synchronizes status. Requires “SentinelOne Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” you will need to add an “Alert_ID” Alert Context Value for the job to be able to find the correct information.|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/139/jobInstances/57|Automated test job instance configured by script. Index: 28|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/139/jobInstances/165|Automated test job instance configured by script. Index: 8|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/139/jobInstances/57|Automated test job instance configured by script. Index: 28|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/139/jobInstances/219|Automated test job instance configured by script. Index: 52|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/123|Automated test job instance configured by script. Index: 9|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/164|Automated test job instance configured by script. Index: 7|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/123|Automated test job instance configured by script. Index: 9|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/218|Automated test job instance configured by script. Index: 51|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/141/jobInstances/59|Automated test job instance configured by script. Index: 30|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/141/jobInstances/221|Automated test job instance configured by script. Index: 54|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/167/jobInstances/190|Automated test job instance configured by script. Index: 23|
|projects/project/locations/location/instances/instance/integrations/BMCRemedyITSM/jobs/256/jobInstances/210|Automated test job instance configured by script. Index: 43|
|projects/project/locations/location/instances/instance/integrations/ServiceDeskPlusV3/jobs/168/jobInstances/191|Automated test job instance configured by script. Index: 24|
|projects/project/locations/location/instances/instance/integrations/ServiceDeskPlusV3/jobs/168/jobInstances/155|This job will synchronize ServiceDeskPlus requests that were created within Siemplify Case playbook and Siemplify cases. Note: in ServiceDeskPlus statuses "Cancelled", "Closed" and "Resolved" are treated as closed. Additionally, in order for the job to work, it’s required for the case to have 2 tags. First tag should be "ServiceDeskPlus" and the second should be with the prefix "ServiceDeskPlus Requests:{request id}".|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/159/jobInstances/184|Automated test job instance configured by script. Index: 17|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/158/jobInstances/183|Automated test job instance configured by script. Index: 16|
|projects/project/locations/location/instances/instance/integrations/MicrosoftAzureSentinel/jobs/202/jobInstances/200|Automated test job instance configured by script. Index: 33|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/166/jobInstances/189|Automated test job instance configured by script. Index: 22|
|projects/project/locations/location/instances/instance/integrations/MicrosoftAzureSentinel/jobs/201/jobInstances/199|Automated test job instance configured by script. Index: 32|
|projects/project/locations/location/instances/instance/integrations/PaloAltoCortexXDR/jobs/203/jobInstances/25|This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.|
|projects/project/locations/location/instances/instance/integrations/SCCEnterprise/jobs/173/jobInstances/196|Automated test job instance configured by script. Index: 29|
|projects/project/locations/location/instances/instance/integrations/SCCEnterprise/jobs/172/jobInstances/195|Automated test job instance configured by script. Index: 28|
|projects/project/locations/location/instances/instance/integrations/SCCEnterprise/jobs/171/jobInstances/194|Automated test job instance configured by script. Index: 27|
|projects/project/locations/location/instances/instance/integrations/RSAArcher/jobs/155/jobInstances/180|Automated test job instance configured by script. Index: 13|
|projects/project/locations/location/instances/instance/integrations/RSAArcher/jobs/155/jobInstances/224|Automated test job instance configured by script. Index: 57|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/170/jobInstances/193|Automated test job instance configured by script. Index: 26|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/169/jobInstances/192|Automated test job instance configured by script. Index: 25|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/164/jobInstances/187|Automated test job instance configured by script. Index: 20|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/165/jobInstances/188|Automated test job instance configured by script. Index: 21|
|projects/project/locations/location/instances/instance/integrations/SentinelOneV2/jobs/244/jobInstances/204|Automated test job instance configured by script. Index: 37|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/174|Automated test job instance configured by script. Index: 7|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/160/jobInstances/185|Automated test job instance configured by script. Index: 18|
|projects/project/locations/location/instances/instance/integrations/Tools/jobs/226/jobInstances/202|Automated test job instance configured by script. Index: 35|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/119|Automated test job instance configured by script. Index: 5|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/151|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/154|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/160/jobInstances/78|Automated test job instance configured by script. Index: 49|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/165/jobInstances/83|Automated test job instance configured by script. Index: 54|
|projects/project/locations/location/instances/instance/integrations/RSAArcher/jobs/155/jobInstances/73|Automated test job instance configured by script. Index: 44|


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
|1New Playbook||
|2New Playbook||
|Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|New Playbook||
|Nw Playbook||
|Carbon Black Cloud Remediation||
|Copy of Carbon Black Cloud Remediation - 1||


## Jobs
|Name|Description|
|----|-----------|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/158/jobInstances/76|Automated test job instance configured by script. Index: 47|
|projects/project/locations/location/instances/instance/integrations/AzureSecurityCenter/jobs/189/jobInstances/72|Automated test job instance configured by script. Index: 43|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/105|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/52|Automated test job instance configured by script. Index: 23|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/53|Automated test job instance configured by script. Index: 24|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/114|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/49|Automated test job instance configured by script. Index: 20|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/134/jobInstances/121|Automated test job instance configured by script. Index: 7|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/157/jobInstances/75|Automated test job instance configured by script. Index: 46|
|projects/project/locations/location/instances/instance/integrations/Luminar IOCs and Leaked Credentials/jobs/129/jobInstances/48|Automated test job instance configured by script. Index: 19|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/51|Automated test job instance configured by script. Index: 22|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/106|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/104|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/96|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/50|Automated test job instance configured by script. Index: 21|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/95|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/94|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/86|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/84|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/31|Automated test job instance configured by script. Index: 2|
|projects/project/locations/location/instances/instance/integrations/CaseFederation/jobs/42/jobInstances/29|Automated test job instance configured by script. Index: 0|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/27|This job will synchronize Google SecOps Alerts and Crowdstrike alerts. The job synchronizes comments and status. Requires “Crowdstrike Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” or “Identity Protections Detection Connector” you will need to add an “Alert_ID” context value for the job to be able to find the correct information.|
|projects/project/locations/location/instances/instance/integrations/MicrosoftGraphMailDelegated/jobs/146/jobInstances/28|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|projects/project/locations/location/instances/instance/integrations/CrowdStrikeFalcon/jobs/197/jobInstances/24|This job will synchronize Google SecOps Alerts and Crowdstrike alerts. The job synchronizes comments and status. Requires “Crowdstrike Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” or “Identity Protections Detection Connector” you will need to add an “Alert_ID” context value for the job to be able to find the correct information.|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/30|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/Group-IB-DRP/jobs/130/jobInstances/118|Automated test job instance configured by script. Index: 4|
|projects/project/locations/location/instances/instance/integrations/FreshworksFreshservice/jobs/135/jobInstances/122|Automated test job instance configured by script. Index: 8|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/74|Automated test job instance configured by script. Index: 45|
|projects/project/locations/location/instances/instance/integrations/GoogleChronicle/jobs/156/jobInstances/23|This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM. Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.|
|projects/project/locations/location/instances/instance/integrations/NessusScanner/jobs/142/jobInstances/60|Automated test job instance configured by script. Index: 31|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/133/jobInstances/120|Automated test job instance configured by script. Index: 6|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/56|Automated test job instance configured by script. Index: 27|
|projects/project/locations/location/instances/instance/integrations/Microsoft365Defender/jobs/198/jobInstances/85|Automated test job instance configured by script. Index: 1|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/140/jobInstances/58|Automated test job instance configured by script. Index: 29|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/139/jobInstances/57|Automated test job instance configured by script. Index: 28|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/138/jobInstances/123|Automated test job instance configured by script. Index: 9|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/141/jobInstances/59|Automated test job instance configured by script. Index: 30|
|projects/project/locations/location/instances/instance/integrations/BMCRemedyITSM/jobs/193/jobInstances/79|Automated test job instance configured by script. Index: 50|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/159/jobInstances/77|Automated test job instance configured by script. Index: 48|
|projects/project/locations/location/instances/instance/integrations/CaServiceDesk/jobs/195/jobInstances/54|Automated test job instance configured by script. Index: 25|
|projects/project/locations/location/instances/instance/integrations/MicrosoftAzureSentinel/jobs/201/jobInstances/61|Automated test job instance configured by script. Index: 32|
|projects/project/locations/location/instances/instance/integrations/PaloAltoCortexXDR/jobs/203/jobInstances/25|This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.|
|projects/project/locations/location/instances/instance/integrations/RSAArcher/jobs/155/jobInstances/73|Automated test job instance configured by script. Index: 44|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/164/jobInstances/82|Automated test job instance configured by script. Index: 53|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/165/jobInstances/83|Automated test job instance configured by script. Index: 54|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/160/jobInstances/78|Automated test job instance configured by script. Index: 49|
|projects/project/locations/location/instances/instance/integrations/Exchange/jobs/132/jobInstances/119|Automated test job instance configured by script. Index: 5|
|projects/project/locations/location/instances/instance/integrations/MicrosoftTeams/jobs/163/jobInstances/128|hey this is manually added Automated test job instance configured by script. Index: 52|


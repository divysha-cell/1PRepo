# GitSync

## Integrations
|Name|Description|
|----|-----------|
|AWS GuardDuty|Amazon GuardDuty informs you of the status of your AWS environment by producing security findings. GuardDuty helps to detect and manage threats to your AWS system.|
|AWS IAM Access Analyzer|AWS IAM Access Analyzer is built on Zelkova, which translates IAM policies into equivalent logical statements, and runs a suite of general-purpose and specialized logical solvers (satisfiability modulo theories) against the problem. Access Analyzer applies Zelkova repeatedly to a policy with increasingly specific queries to characterize classes of behaviors the policy allows, based on the content of the policy. To learn more about satisfiability modulo theories, see Satisfiability Modulo Theories. Access Analyzer does not examine access logs to determine whether an external entity accessed a resource within your zone of trust. It generates a finding when a resource-based policy allows access to a resource, even if the resource was not accessed by the external entity. Access Analyzer also does not consider the state of any external accounts when making its determination. That is, if it indicates that account 11112222333 can access your S3 bucket, it knows nothing about the state of users, roles, service control policies (SCP), and other relevant configurations in that account. This is for customer privacy – Access Analyzer doesn't consider who owns the other account. It is also for security – if the account is not owned by the Access Analyzer customer, it is still important to know that an external entity could gain access to their resources even if there are currently no principals in the account that could access the resources. Access Analyzer considers only certain IAM condition keys that external users cannot directly influence, or that are otherwise impactful to authorization. Access Analyzer does not currently report findings from AWS service principals or internal service accounts. In rare cases where Access Analyzer isn't able to fully determine whether a policy statement grants access to an external entity, it errs on the side of declaring a false positive finding. Access Analyzer is designed to provide a comprehensive view of the resource sharing in your account, and strives to minimize false negatives.|
|AWS Security Hub|AWS Security Hub gives you a comprehensive view of your high-priority security alerts and security posture across your AWS accounts. There are a range of powerful security tools at your disposal, from firewalls and endpoint protection to vulnerability and compliance scanners. But oftentimes this leaves your team switching back-and-forth between these tools to deal with hundreds, and sometimes thousands, of security alerts every day.|
|Active Directory|Microsoft Active Directory integration facilitates the centralized management and synchronization of Windows user accounts with Security Center's administrator and cardholder accounts.|
|AirTable|Airtable can store information in a spreadsheet that's visually appealing and easy-to-use, but it's also powerful enough to act as a database that businesses can use for customer-relationship management (CRM), task management, project planning, and tracking inventory.|
|AlienVault USM Anywhere|AlienVault USM Anywhere delivers powerful threat detection, incident response, and compliance management for cloud, on-premises, and hybrid environments.|
|Amazon Macie|Amazon Macie is a powerful security and compliance service that provides an automatic method to detect, identify, and classify data within your AWS account.|
|Anomali Staxx|Anomali STAXX provides bi-directional sharing of threat intelligence from STIX/TAXII sources that are in the cloud (such as Anomali Limo, http://hailataxii.com, an ISAC, or Anomali ThreatStream) or on premise. With Anomali STAXX, you can connect to STIX/TAXII servers, discover and configure their threat feeds, and poll (download) threat intelligence from those feeds. You can also import threat intelligence into Anomali STAXX and push (upload) selected observables to other STIX/TAXII servers.|
|Apache Kafka|Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.|
|Arcsight|Real-time threat detection and automated response backed by a powerful, open, and intelligent SIEM (Security Information and Event Management).|
|Vmware Carbon Black Cloud|The VMware Carbon Black Cloud is a cloud-native endpoint protection platform (EPP) that combines the intelligent system hardening and behavioral prevention needed to keep emerging threats at bay, using a single lightweight agent, and an easy-to-use console.|
|CrowdStrike Falcon|CrowdStrike Falcon is the leader in next-generation endpoint protection, threat intelligence and incident response through cloud-based endpoint protection.|
|Cybersixgill Actionable Alerts|By integrating Cybersixgill actionable alerts, Google SecOps customers gain a premium,automated threat intelligence solution based on the most comprehensive data sources from the deep, dark and surface web. It is customizable, enabling users to define key assets relevant to their brand, industry, and geolocation. Users can covertly monitor critical assets such as IP addresses, domains, vulnerabilities, and VIPs for activity on the underground and closed sources - and prioritize, as well as respond to threats directly from the Google SecOps dashboard.|
|EclecticIQ|EclecticIQ is a global provider of threat intelligence technology and services.  The most targeted organizations in the world – including governments and large enterprises – use our platform to automate intelligence management at scale and accelerate collaboration across security teams.|
|EmailV2|Email integration over smtp and imap protocols|
|Extrahop|ExtraHop provides cloud-native cybersecurity solutions to help enterprises detect and respond to advanced threats—before they compromise your business.|
|FireEye ETP|FireEye Email Threat Prevention Cloud (ETP) is different from traditional email security. It is a complete, cloud-based email security solution that delivers automatic protection from the targeted, spear-phishing attacks. Plus, it includes industry-leading FireEye Advanced Threat Intelligence.|
|FireEye Helix|To protect against advanced threats, organizations need to integrate their security and apply the right expertise and processes. FireEye Helix is a cloud-hosted security operations platform that allows organizations to take control of any incident from alert to fix.|
|Freshworks Freshservice|Freshservice is a cloud-based IT Help Desk and service management solution that enables organizations to simplify their IT operations. The solution offers features that include a ticketing system, self-service portal and knowledge-base.|
|Functions|A set of math and data manipulation actions created for Google SecOps Community to power up playbook capabilities.|
|Google Chronicle|Google SecOps enables you to examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed from within your enterprise. To enable the Google API client to communicate with the Backstory API you will need Google Developer Service Account Credential, https://developers.google.com/identity/protocols/OAuth2#serviceaccount.|
|Google SecOps AI Agents|This integration provides first-party AI agents for Google Chronicle. It allows users to leverage Google's advanced AI capabilities for security operations and threat intelligence within the Chronicle platform.|
|Google Security Command Center|Security management, data risk & compliance monitoring platform to help with vulnerability management. Detect & respond to security vulnerabilities.|
|IntSights|The only all-in-one external threat protection platform designed to neutralize cyberattacks outside the wire.|
|Lists|A set of tools to facilitate managing custom lists within Google SecOps.|
|McAfeeESM|McAfee® Enterprise Security Manager, the industry-leading SIEM solution from McAfee, provides an intelligent, actionable, and integrated platform to protect your customers’ business and grow yours.|
|Microsoft Azure Sentinel|Microsoft Azure Sentinel is a scalable, cloud-native, security information event management (SIEM) and security orchestration automated response (SOAR) solution. Azure Sentinel delivers intelligent security analytics and threat intelligence across the enterprise, providing a single solution for alert detection, threat visibility, proactive hunting, and threat response.|
|PerimeterX|Integration of PerimeterX Code Defender alerting with Google SecOps|
|Phishrod|PhishRod is an integrated & analytics driven solution for phishing readiness, security awareness automation, threat advisory & policy compliance management. It helps organizations to empower end users and cascade the actionable human intelligence across the organization to deter cyber attacks.|
|Qualys EDR|Qualys Multi-Vector EDR unifies different context vectors like asset discovery, rich normalized software inventory, end-of-life visibility, vulnerabilities and exploits, misconfigurations, in-depth endpoint telemetry, and network reachability with a powerful backend to correlate it all for accurate assessment, detection and response – all in a single, cloud-based app.|
|Sumologic|Sumo Logic is a cloud-based Machine data analytics company focusing on security, operations and BI usecases. It provides log management and analytics services that leverage machine-generated big data to deliver real-time IT insights.|
|VirusTotal|VirusTotal is a service that analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content. VirusTotal aggregates many antivirus products and online scan engines to check for viruses that the user's own antivirus may have missed, or to verify against any false positives. Use VirusTotal to investigate suspicious files, domains, URLs, IP addresses, and hashes.|


## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|AWS Cloud Trail - Insights Connector Instance|None|True|
|AWS GuardDuty - Findings Connector Instance|None|True|
|AWS IAM Access Analyzer - Findings Connector Instance|None|True|
|AWS Security Hub - Findings Connector Instance|None|False|
|AirTable Connector Instance|None|False|
|AlienVault USM Anywhere Connector Instance|None|False|
|AlienVault USM Appliance Connector Instance|None|False|
|Amazon Macie - Findings Connector Instance|None|False|
|Anomali Staxx - Indicators Connector Instance|None|True|
|Apache Kafka - Messages Connector Instance|None|False|
|ArcSight - Security Events Connector Instance|None|False|
|Arcsight ESM Connector Instance|None|False|
|Azure Security Center - Security Alerts Connector Instance|None|True|
|VMware Carbon Black Cloud Alerts Connector Instance|None|True|
|VMware Carbon Black Cloud Alerts and Events Baseline Connector Instance|None|True|
|VMware Carbon Black Cloud Alerts and Events Tracking Connector Instance|None|True|
|CA Service Desk Connector Instance|None|True|
|Crowdstrike - Alerts Connector Instance|None|True|
|Crowdstrike - Detections Connector Instance|None|True|
|Crowdstrike - Identity Protection Detections Connector Instance|None|True|
|Crowdstrike - Incidents Connector Instance|None|True|
|Crowdstrike Falcon Streaming Events Connector Instance|None|True|
|Cybersixgill Actionable Alerts Instance|None|False|
|EclecticIQ - Feed Connector Instance|None|False|
|Exchange EML Connector Instance|None|True|
|Exchange Mail Connector Instance|None|True|
|Exchange Mail Connector v2 Instance|None|True|
|Exchange Mail Connector v2 with Oauth Authentication Instance|None|True|
|Extrahop - Detections Connector Instance|None|False|
|FireEye ETP - Email Alerts Connector Instance|None|False|
|FireEye Helix - Alerts Connector Instance|None|False|
|Freshservice Tickets Connector Instance|None|False|
|Google Chronicle - Chronicle Alerts Connector Instance|None|True|
|Google Security Command Center - Findings Connector Instance|None|False|
|DRP Typosquatting Connector Instance|None|False|
|DRP Violations Connector Instance|None|False|
|DRP Violations Review Connector Instance|None|False|
|Intsights Connector Instance|None|False|
|McAfee ESM Connector Instance|None|False|
|McAfee ESM Correlations Connector Instance|None|False|
|Microsoft 365 Defender - Incidents Connector Instance|None|True|
|Microsoft Azure Sentinel Incident Connector Instance|None|True|
|Microsoft Azure Sentinel Incident Connector v2 Instance|None|True|
|Microsoft Sentinel Incident Tracking Connector Instance|None|True|
|Microsoft Graph Mail Delegated Connector Instance|None|True|
|MS SecureScore Alert Instance|None|False|
|MS365 MFA Alert Instance|None|False|
|ObserveIT - Alerts Connector Instance|None|False|
|Palo Alto Cortex XDR Connector Instance|None|True|
|Slack Connector For Code Defender Instance|None|False|
|PhishRod - Incidents Connector Instance|None|False|
|Qualys EDR - Events Connector Instance|None|False|
|SOCRadar Alarms Connector Instance|None|True|
|SentinelOne - Alerts Connector Instance|None|True|
|SentinelOne - Threats Connector Instance|None|True|
|ServiceNow Connector Instance|None|True|
|Splunk ES - Notable Events Connector Instance|None|True|
|Splunk Pull Connector Instance|None|True|
|Splunk Query Connector Instance|None|True|
|Sumologic Connector Instance|None|False|
|Vectra RUX - Entities Connector Instance|None|False|


## Playbooks
|Name|Description|
|----|-----------|
|AWS EC2 Containment|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|AWS EC2 Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|AWS Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|AWS Users Containment|An embedded workflow that can receive inputs and return an output.|
|Amazon Web Services Cloud Platform Starting Playbook|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Copy of AWS EC2 Containment|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|Copy of AWS EC2 Containment - 2|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|Copy of AWS EC2 Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of AWS EC2 Enrichment - 2|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of AWS Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of AWS Enrichment - 2|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of AWS Users Containment|An embedded workflow that can receive inputs and return an output.|
|Copy of AWS Users Containment - 2|An embedded workflow that can receive inputs and return an output.|
|Copy of Amazon Web Services Cloud Platform Starting Playbook|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Copy of Amazon Web Services Cloud Platform Starting Playbook - 2|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Copy of Copy of AWS EC2 Containment|This block allows the playbook to automatically stop EC2 instances that were identified in the alert as potentially compromised or suspicious, supporting the containment phase of the incident response process.|
|Copy of Copy of AWS EC2 Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of Copy of AWS Enrichment|This block retrieves EC2 instance data associated with the case and provides context for other actions or analysis.|
|Copy of Copy of AWS Users Containment|An embedded workflow that can receive inputs and return an output.|
|Copy of Copy of Amazon Web Services Cloud Platform Starting Playbook|Amazon Web Services Cloud Platform Starting Playbook provides reference implementation of how Amazon Web Services Cloud Platform alerts can be processed in Google SecOps.|
|Copy of Copy of Copy of New Playbook||
|Copy of Copy of CrowdStrike Containment|This block allows the playbook to perform containment actions on endpoints by targeting the IPs and hostnames associated with the case, helping to prevent further compromise during incident response.|
|Copy of Copy of CrowdStrike Falcon Starting Playbook|CrowdStrike Falcon Starting Playbook provides reference implementation of how CrowdStrike Falcon alerts can be processed in Google SecOps.|
|Copy of Copy of GTI Enrichment|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of Copy of GTI Enrichment - 1|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of Copy of Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Copy of Google SecOps Enrichment - 1|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Copy of Google Workspace Enrichment|This block enriches user entities with relevant information from Google Workspace, providing additional context to support investigation and response activities.|
|Copy of Copy of High Risk Users Check|This block checks Google GTI sourced alerts against a SOAR custom list to find matches of targeted Industries.|
|Copy of Copy of MITRE Enrichment|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|Copy of Copy of New Playbook||
|Copy of Copy of New Playbook - 2||
|Copy of Copy of New Playbook - 2 - 2||
|Copy of CrowdStrike Containment|This block allows the playbook to perform containment actions on endpoints by targeting the IPs and hostnames associated with the case, helping to prevent further compromise during incident response.|
|Copy of CrowdStrike Containment - 2|This block allows the playbook to perform containment actions on endpoints by targeting the IPs and hostnames associated with the case, helping to prevent further compromise during incident response.|
|Copy of CrowdStrike Falcon Starting Playbook|CrowdStrike Falcon Starting Playbook provides reference implementation of how CrowdStrike Falcon alerts can be processed in Google SecOps.|
|Copy of CrowdStrike Falcon Starting Playbook - 2|CrowdStrike Falcon Starting Playbook provides reference implementation of how CrowdStrike Falcon alerts can be processed in Google SecOps.|
|Copy of GTI Enrichment|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of GTI Enrichment - 1|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of GTI Enrichment - 1 - 2|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of GTI Enrichment - 2|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Copy of Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Google SecOps Enrichment - 1|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Google SecOps Enrichment - 1 - 2|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Google SecOps Enrichment - 2|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Copy of Google Workspace Enrichment|This block enriches user entities with relevant information from Google Workspace, providing additional context to support investigation and response activities.|
|Copy of Google Workspace Enrichment - 2|This block enriches user entities with relevant information from Google Workspace, providing additional context to support investigation and response activities.|
|Copy of High Risk Users Check|This block checks Google GTI sourced alerts against a SOAR custom list to find matches of targeted Industries.|
|Copy of High Risk Users Check - 2|This block checks Google GTI sourced alerts against a SOAR custom list to find matches of targeted Industries.|
|Copy of MITRE Enrichment|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|Copy of MITRE Enrichment - 2|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|Copy of New Block|An embedded workflow that can receive inputs and return an output.|
|Copy of New Playbook||
|Copy of New Playbook - 2||
|Copy of New Playbook - 3||
|CrowdStrike Containment|This block allows the playbook to perform containment actions on endpoints by targeting the IPs and hostnames associated with the case, helping to prevent further compromise during incident response.|
|CrowdStrike Falcon Starting Playbook|CrowdStrike Falcon Starting Playbook provides reference implementation of how CrowdStrike Falcon alerts can be processed in Google SecOps.|
|GTI Enrichment|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|GTI Enrichment - 1|This block enhances case entities with Google Threat Intelligence enrichment information. Works for IPs, URLs, hostnames, domains, hashes (MD5, SHA-1, SHA-256), threat actors, and CVEs.|
|Google SecOps Enrichment|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Google SecOps Enrichment - 1|This block retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Google Workspace Enrichment|This block enriches user entities with relevant information from Google Workspace, providing additional context to support investigation and response activities.|
|High Risk Users Check|This block checks Google GTI sourced alerts against a SOAR custom list to find matches of targeted Industries.|
|MITRE Enrichment|This block retrieves detailed information about MITRE ATT&CK techniques and their associated mitigations, providing valuable context to understand adversary behaviors and possible defensive actions.|
|New Block|An embedded workflow that can receive inputs and return an output.|
|New Playbook||
|fresh New Block|An embedded workflow that can receive inputs and return an output.|
|fresh New Playbook||


## Visual Families
|Name|Description|
|----|-----------|
|Carbon Black File Modifications|VMware Carbon Black EDR captures four types of file system activity: File creation – the creation of a new file. File Write – the first time a file is written to after being opened or created. File Write Complete – the closing of a file that was written to.This event includes both the file path and also the MD5/SHA256 of the written file. The event is only captured for binaries (Windows PE files such as EXE, DLL and drivers), Adobe Docs (PDF), OfficeXML docs (docx, doc, xlsx, xls, pptx, ppt)  and zip archives (zip) that are smaller than 10MB in size. Can be enabled or disabled independently of filemod collection by deselecting "Non-binary file writes" Not available on macOS and Linux sensors File deletion – the deletion of an existing file.|
|Carbon Black Network Connections Event|VMware Carbon Black EDR captures network connections with the following characteristics: Both TCP over IPv4 or UDP over IPv4 connections Both inbound and outbound connections Network connections record TCP or UDP protocol, the remote IPv4 address, port and the domain name associated with the remote IPv4 Address Inbound connections capture the local port. If the sensor is installed on a typically configured web server, the reported port is 80. Outbound connections capture the remote port, uutbound connections made after DNS resolution the name that resolves to the captured IPV4 address is also reported. The sensor utilizes a passive sensing approach to capturing the domain name, so no additional network traffic is generated in order to capture the name. For DNS/DHCP servers, high CPU and/or memory can be seen due to the high number of netconn events. Rather than disabling all netconns, disable DNS capture on that machine. CB Response: Windows Sensor Causing High CPU/memory Utilization on Netconn Intense Server.|
|Carbon Black Process Event|Cross Process Event and Child Process Events: VMware Carbon Black EDR provides a cross-process event type that records an occurrence of a process that crosses the security boundary of another process. While some of these events are benign, others can indicate an attempt to change the behavior of the target process by a malicious process.|


## Jobs
|Name|Description|
|----|-----------|
|12 Actions Monitor|Notifies of all the actions, that have individually failed at least 3 times, in the last 3 hours|
|Refresh Token Renewal Job1234556789|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|Refresh Token Renewal Job2345678|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|Refresh Token Renewal Job23456789|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|Refresh Token Renewal Job23466543|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|Refresh Token Renewal Job34|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|Refresh Token Renewal Job345678|Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.|
|Siemplify Job- Cases Collector|Collect cases and connector logs from Publisher.|
|Sync Alerts - AutoTest 1|Automated test job instance. Index: 9|
|Sync Alerts - AutoTest 2|Automated test job instance. Index: 36|
|Sync Alerts|This job synchronizes Google SecOps Alerts and Microsoft Defender XDR Alerts. It ensures that comments and status are synchronized bi-directionally between both systems. Note: Assignee synchronization occurs exclusively from Microsoft Defender to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the "Microsoft Defender XDR Alert" tag. If the alert didn’t originate from "Microsoft 365 Defender - Incidents Connector",  you will need to add an "Alert_ID" context value to the alert for the job to be able to find the correct information.|
|Sync Alerts2|This job will synchronize Google SecOps Alerts and Crowdstrike alerts. The job synchronizes comments and status. Requires “Crowdstrike Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” or “Identity Protections Detection Connector” you will need to add an “Alert_ID” context value for the job to be able to find the correct information.|
|Sync Alerts234567|This job will synchronize Google SecOps Alerts and SentinelOne alerts. The job synchronizes status. Requires “SentinelOne Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” you will need to add an “Alert_ID” Alert Context Value for the job to be able to find the correct information.|
|Sync Alerts2345678|This job synchronizes Google SecOps Alerts and Microsoft Defender XDR Alerts. It ensures that comments and status are synchronized bi-directionally between both systems. Note: Assignee synchronization occurs exclusively from Microsoft Defender to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the "Microsoft Defender XDR Alert" tag. If the alert didn’t originate from "Microsoft 365 Defender - Incidents Connector",  you will need to add an "Alert_ID" context value to the alert for the job to be able to find the correct information.|
|Sync Alerts2345678765|This job synchronizes Google SecOps Alerts and Microsoft Defender XDR Alerts. It ensures that comments and status are synchronized bi-directionally between both systems. Note: Assignee synchronization occurs exclusively from Microsoft Defender to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the "Microsoft Defender XDR Alert" tag. If the alert didn’t originate from "Microsoft 365 Defender - Incidents Connector",  you will need to add an "Alert_ID" context value to the alert for the job to be able to find the correct information.|
|Sync Alerts34567|This job will synchronize Google SecOps Alerts and Crowdstrike alerts. The job synchronizes comments and status. Requires “Crowdstrike Alert” tag on the case. Note: If the alert didn’t originate from “Alerts Connector” or “Identity Protections Detection Connector” you will need to add an “Alert_ID” context value for the job to be able to find the correct information.|
|Sync Closed Incidents - AutoTest 1|Automated test job instance. Index: 5|
|Sync Closed Incidents - AutoTest 2|Automated test job instance. Index: 32|
|Sync Closed Incidents By Tag - AutoTest 1|Automated test job instance. Index: 23|
|Sync Closed Incidents By Tag|This job will synchronize BMC Remedy ITSM incidents that were created within Siemplify Case playbook and Siemplify cases. Note: in BMC Remedy ITSM statuses "Cancelled", "Closed" and "Resolved" are treated as closed. Additionally, in order for the job to work, it's required for the case to have 2 tags. First tag should be "BMC Remedy ITSM" and the second should be with the prefix "BMC Remedy ITSM:{Incident ID}". Job can only close incidents that are assigned in BMC Remedy ITSM.|
|Sync Closed Incidents|This job will synchronize closed ServiceNow incidents and Google SecOps alerts. This job works with ServiceNow incidents that were ingested as alerts and also cases, which contains tag “ServiceNow” and “TICKET_ID” context value with Incident Number inside of it.|
|Sync Closed Requests By Tag - AutoTest 1|Automated test job instance. Index: 1|
|Sync Closed Requests By Tag - AutoTest 2|Automated test job instance. Index: 28|
|Sync Closed Requests By Tag|This job will synchronize ServiceDeskPlus requests that were created within Siemplify Case playbook and Siemplify cases. Note: in ServiceDeskPlus statuses "Cancelled", "Closed" and "Resolved" are treated as closed. Additionally, in order for the job to work, it’s required for the case to have 2 tags. First tag should be "ServiceDeskPlus" and the second should be with the prefix "ServiceDeskPlus Requests:{request id}".|
|Sync Closed Requests By Tag34567|This job will synchronize ServiceDeskPlus requests that were created within Siemplify Case playbook and Siemplify cases. Note: in ServiceDeskPlus statuses "Cancelled", "Closed" and "Resolved" are treated as closed. Additionally, in order for the job to work, it’s required for the case to have 2 tags. First tag should be "ServiceDeskPlus" and the second should be with the prefix "ServiceDeskPlus Requests:{request id}".|
|Sync Closed Requests By Tag345678|This job will synchronize ServiceDeskPlus requests that were created within Siemplify Case playbook and Siemplify cases. Note: in ServiceDeskPlus statuses "Cancelled", "Closed" and "Resolved" are treated as closed. Additionally, in order for the job to work, it’s required for the case to have 2 tags. First tag should be "ServiceDeskPlus" and the second should be with the prefix "ServiceDeskPlus Requests:{request id}".|
|Sync Closed Requests By Tag56789|This job will synchronize ServiceDeskPlus requests that were created within Siemplify Case playbook and Siemplify cases. Note: in ServiceDeskPlus statuses "Cancelled", "Closed" and "Resolved" are treated as closed. Additionally, in order for the job to work, it’s required for the case to have 2 tags. First tag should be "ServiceDeskPlus" and the second should be with the prefix "ServiceDeskPlus Requests:{request id}".|
|Sync Comments - AutoTest 1|Automated test job instance. Index: 22|
|Sync Comments - AutoTest 2|Automated test job instance. Index: 49|
|Sync Comments56|Sync comments from CA Desk Manager to Siemplify.|
|Sync IOC Feeds - AutoTest 1|Automated test job instance. Index: 0|
|Sync IOC Feeds - AutoTest 2|Automated test job instance. Index: 27|
|Sync IOC Feeds|Scheduled job that fetches IOCs from configured SOCRadar Threat Feed collections and writes them to Chronicle SIEM reference lists. Creates one list per IOC type (ip, domain, hash, url). Run daily to keep threat intelligence feeds current.|
|Sync IOC Feeds109|Scheduled job that fetches IOCs from configured SOCRadar Threat Feed collections and writes them to Chronicle SIEM reference lists. Creates one list per IOC type (ip, domain, hash, url). Run daily to keep threat intelligence feeds current.|
|Sync IOC Feeds345678|Scheduled job that fetches IOCs from configured SOCRadar Threat Feed collections and writes them to Chronicle SIEM reference lists. Creates one list per IOC type (ip, domain, hash, url). Run daily to keep threat intelligence feeds current.|
|Sync Incidents - AutoTest 1|Automated test job instance. Index: 10|
|Sync Incidents - AutoTest 2|Automated test job instance. Index: 37|
|Sync Incidents Job - AutoTest 1|Automated test job instance. Index: 4|
|Sync Incidents Job - AutoTest 2|Automated test job instance. Index: 31|
|Sync Incidents Job|This job will synchronize incidents fields and attachments that are related to case/alerts in ServiceNow. For the job to work, you need to have the "ServiceNow Incident Sync" tag added to the case and "TICKET_ID" context value added to either Case or Alert depending on the parameter "Sync Level". Example of the "TICKET_ID": "INC0000050,INC0000051".|
|Sync Incidents V2 - AutoTest 1|Automated test job instance. Index: 14|
|Sync Incidents V2 - AutoTest 2|Automated test job instance. Index: 41|
|Sync Incidents V234567|Use the Sync Incidents V2 job to synchronize Google SecOps alerts with Microsoft Sentinel incidents. This job ensures that comments, statuses, and tags are synchronized bi-directionally between both systems. Note: Assignee and severity synchronization occurs exclusively from Microsoft Sentinel to Google SecOps. For the job to identify the correct information, the Google SecOps case must have the Microsoft Sentinel Incident tag. This job only works on alerts from the Microsoft Azure Sentinel Incident Connector v2.|
|Sync Incidents|Deprecated. This job synchronizes Google SecOps Alerts and Microsoft Sentinel Incidents. It ensures that comments, status, and tags are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the “Microsoft Sentinel Incident” tag. If the alert didn’t originate from “Microsoft Azure Sentinel Incident Connector v2”,  you will need to add an “Incident_ID” context value to the case for the job to be able to find the correct information.|
|Sync Incidents234|This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.|
|Sync Incidents34567|This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.|
|Sync Incidents5778|This job synchronizes Google SecOps Alerts and Palo Alto XDR Incidents. It ensures that comments and status are kept in sync between the two systems. For the job to identify the correct information, the Google SecOps case must have the "Palo Alto XDR Incident" tag. If the alert didn’t originate from "Palo Alto Cortex XDR Connector",  you will need to add an "Incident_ID" context value to the case for the job to be able to find the correct information.|
|Sync Table Record Comments - AutoTest 1|Automated test job instance. Index: 6|
|Sync Table Record Comments - AutoTest 2|Automated test job instance. Index: 33|
|Sync Table Record Comments By Tag - AutoTest 1|Automated test job instance. Index: 7|
|Sync Table Record Comments By Tag - AutoTest 2|Automated test job instance. Index: 34|
|Sync Table Record Comments By Tag4567|This job will synchronize comments in ServiceNow table records and Siemplify cases. Additionally, in order for the job to work, it’s required for the case to have 2 tags. First tag should be "ServiceNow {table name}", for example, "ServiceNow incident" and the second should be with the prefix "ServiceNow TicketId: {TICKET_ID}". Example of the "TICKET_ID": "INC0000050,INC0000051".|
|Sync Threats - AutoTest 1|Automated test job instance. Index: 8|
|Sync Threats - AutoTest 2|Automated test job instance. Index: 35|
|Sync Threats 2|This job will synchronize Google SecOps Alerts and SentinelOne threats. The job synchronizes comments and status. Requires “SentinelOne Threat” tag on the case. Note: If the alert didn’t originate from “Threats Connector” you will need to add an “Threat_ID” Alert Context Value for the job to be able to find the correct information.|
|Sync Threats|This job will synchronize Google SecOps Alerts and SentinelOne threats. The job synchronizes comments and status. Requires “SentinelOne Threat” tag on the case. Note: If the alert didn’t originate from “Threats Connector” you will need to add an “Threat_ID” Alert Context Value for the job to be able to find the correct information.|
|Sync Threats345678|This job will synchronize Google SecOps Alerts and SentinelOne threats. The job synchronizes comments and status. Requires “SentinelOne Threat” tag on the case. Note: If the alert didn’t originate from “Threats Connector” you will need to add an “Threat_ID” Alert Context Value for the job to be able to find the correct information.|
|Tag Untouched Cases - AutoTest 1|Automated test job instance. Index: 2|
|Tag Untouched Cases - AutoTest 2|Automated test job instance. Index: 29|
|Tag Untouched Cases new|This job will search all open cases, and identify cases that have not been touched in Max Time hours, and apply the tag/tags listed in the tags parameter|
|Tag Untouched Cases|This job will search all open cases, and identify cases that have not been touched in Max Time hours, and apply the tag/tags listed in the tags parameter|
|Tag Untouched Cases34567|This job will search all open cases, and identify cases that have not been touched in Max Time hours, and apply the tag/tags listed in the tags parameter|
|Tag Untouched Cases7890|This job will search all open cases, and identify cases that have not been touched in Max Time hours, and apply the tag/tags listed in the tags parameter|
|Token Renewal Job - AutoTest 1|Automated test job instance. Index: 19|
|Token Renewal Job - AutoTest 2|Automated test job instance. Index: 46|


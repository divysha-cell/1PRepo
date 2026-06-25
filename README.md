# GitSync

## Integrations
|Name|Description|
|----|-----------|
|Google Chronicle|Google SecOps enables you to examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed from within your enterprise. To enable the Google API client to communicate with the Backstory API you will need Google Developer Service Account Credential, https://developers.google.com/identity/protocols/OAuth2#serviceaccount.|
|Google SecOps AI Agents|This integration provides first-party AI agents for Google Chronicle. It allows users to leverage Google's advanced AI capabilities for security operations and threat intelligence within the Chronicle platform.|
|Palo Alto Cortex XDR|Cortex XDR - XDR is the world’s first detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks.  Cortex XDR accurately detects threats with behavioral analytics and reveals the root cause to speed up investigations.|


## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|Connector_35_AWSCloudTrail|Pull insights from AWS Cloud Trail.|True|
|Connector_54_AmazonMacie|Pull findings from Amazon Macie. Note: Whitelist works with Finding types, for example, SensitiveData:S3Object/Personal.|False|
|Connector_23_AnomaliStaxx|Pull indicators from Anomali Staxx|True|
|Connector_19_Arcsight|Arcsight ESM Connector|True|
|Connector_31_AzureADIdentityProtection|Pull information about risk detections from Azure AD Identity Protection. Note: whitelist filter works with "riskEventType" parameter.|False|
|Connector_42_AzureSecurityCenter|Deprecation Notice! This connector is planned to be deprecated on 30th March 2027. Visit documentation for more information. Pull security alerts from Azure Security Center. Note: whitelist works with alertType field.|True|
|Connector_48_BMCHelixRemedyForce|Pull information about incidents from BMC Helix Remedyforce.|False|
|Connector_53_BlueLiv|Pull security threats from BlueLiv. Connector fetches all of the latest threats from BlueLiv modules. Whitelist and blacklist filters work with BlueLiv module types. For example, if you want to get threats only from Hacktivism modules, you can turn on the whitelist and type in the Hacktivism type name.|False|
|Connector_30_CiscoAMP|Pull security events from Cisco AMP into Siemplify. Note: whitelist works with eventType parameter.|False|
|Connector_44_Devo|Connector can be used to fetch alert records from Devo siem.logtrust.alert.info table. Connector whitelist can be used to ingest only specific types of alerts based on alert context value.|False|
|Connector_52_DigitalShadows|Connector ingest incidents from Digital Shadows into Siemplify.|False|
|Connector_45_EmailV2|Configured Connector_45_EmailV2|False|
|Connector_41_Extrahop|Pull information about detections from Extrahop. Note: whitelist filter works with "type" parameter.|False|
|Connector_46_FireEyeHelix|Pull alerts from FireEye Helix.|False|
|Connector_34_FireEyeNX|Connector ingests FireEye NX alert into Siemplify.|False|
|Connector_51_FortiAnalyzer|Pull information about alerts from FortiAnalyzer. Note: Dynamic list filter works with the "subject" parameter.|False|
|Connector_39_Fortigate|Pull information about different threat logs from Fortigate. Note: whitelist filter works with "eventtype" parameter.|False|
|Connector_37_FortinetFortiSIEM|Connector can be used to fetch FortiSIEM incidents. Connector whitelist can be used to ingest only specific types of incidents based on incident’s “eventType” attribute value. SourceGroupIdentifier of the connector can be used to group Siemplify alerts based on incident id.  Connector requires FortiSIEM version 6.3 or newer.|False|
|Connector_20_FreshworksFreshservice|Connector can be used to fetch Freshservice tickets to create Siemplify alerts from. Connector whitelist can be used to ingest only specific types of tickets - Incident or Service Request|False|
|Connector_28_Gmail|The Gmail Connector retrieves Gmail emails from the specified mailbox. To filter specific values from the email body and subject, use the dynamic list regular expressions in the following format: “key: regex”. For example, after finding a match for the following regex: “subject: (?<=Subject: ).*”, the connector creates a Google SecOps alert event and adds a new key with the “subject” name to it. The new key value matches the regular expression.|False|
|Connector_40_GoogleAlertCenter|Pull information about alerts from Google Alert Center. Note: whitelist filter works with "type" parameter.|False|
|Connector_1_GoogleChronicle|Pull information about Rule based alerts from Google Chronicle. Note: dynamic list is used for filtering purposes. For all of the details please visit the documentation portal.|True|
|Connector_25_GoogleThreatIntelligence|Use the Google Threat Intelligence - DTM Alerts Connector to retrieve alerts from Google Threat Intelligence. The dynamic listworks with the "alert_type" parameter.|False|
|Connector_33_HarmonyMobile|Pull information about alerts from Harmony Mobile. Note: whitelist filter works with "threat_factors" parameter.|False|
|Connector_43_IllusiveNetworks|Pull incidents with related forensic timeline from Illusive Networks. Note: This connector requires changes to the rate limiting on the Illusive Networks server. Default rate limit is too small. All of the steps are available in the documentation. Whitelisting and Blacklisting is done via type of the incident|False|
|Connector_27_Intsights|Configured Connector_27_Intsights|False|
|Connector_36_LogRhythm|Pull alerts from LogRhythm using Rest API. Note: this connector is only supported for LogRhythm version 7.7+.|False|
|Connector_21_McAfeeEPO|Pull events from the EPOEvents table into Siemplify. Whitelist works with Analyzer names.|False|
|Connector_55_McAfeeMvisionEPOV2|Pull events from McAfee Mvision EPO V2.|False|
|Connector_49_NozomiNetworks|Connector to fetch Nozomi Networks Alerts to Siemplify.|False|
|Connector_18_Office365CloudAppSecurity|Fetches alerts from Office 365 CloudApp Security.|False|
|Connector_26_OpenSearch|OpenSearch Connector|False|
|Connector_50_Outpost24|Pull information about outscan findings from Outpost24. Note: whitelist filter works with "productName" parameter.|False|
|Connector_32_PaloAltoPrismaCloud|Pull alerts from Palo Alto Prisma Cloud. Dynamic List works with the “policy.name” parameter.|False|
|Connector_47_Phishrod|Pull information about incidents from PhishRod. Note: dynamic list filter works with “emailSubject” parameter.|False|
|Connector_22_QRadar|Qradar Baseline Offenses connector used to fetch offenses and create Chronicle SOAR alerts based on the Qradar offenses names. Connector will create a single SOAR alert per Qradar offense, and will not try to create additional SOAR alerts with new events from Qradar. Connector uses SOAR dynamic list, but by default if no whitelist rules are set, it will fetchingest all offenses returned from the Qradar API offenses. Connector requires Qradar API version 10.1 or higher.|False|
|Connector_38_QualysVM|Pull detections from Qualys VM. Note: whitelist works with "Type" parameter.|False|
|Connector_24_RSANetWitness|RSA Netwitness static query connector.|False|
|Connector_29_Rapid7InsightIDR|This connector was built using API endpoints that are in preview release. Pull information about investigation from Rapid7 InsightIDR. Note: Dynamic list filter works with the "title" parameter.|False|
|Connector_16_Site24x7|Pull information about alert logs from Site24x7.|False|
|Connector_15_Sophos|Pull alerts from Sophos Central into Siemplify. Note: alerts are available to API only for 24 hours.|False|
|Connector_17_Splunk|Splunk Pull Connector|True|
|Connector_14_StellarCyberStarlight|Pull security events from Stellar Cyber Starlight.  Note: dynamic list works with the Chronicle SOAR alert name, which can be either “event_category: event_name” or “_source_xdr_event_xdr_killchain_stage:_source_xdr_event_name”|False|
|Connector_11_SumoLogicCloudSIEM|Pull information about insights from Sumo Logic Cloud SIEM. Note: dynamic list filter works with "name" parameter.|False|
|Connector_12_Sumologic|Sumologic Connector|False|
|Connector_10_SymantecATP|Fetch incidents from Symantec ATP|False|
|Connector_9_SymantecICDX|Fetching events from SymantecICDX server using a query|False|
|Connector_13_SysdigSecure|Use the Sysdig Secure - Events Connector to pull events from Sysdig Secure. The dynamic list works with the "ruleName" parameter.|False|
|Connector_7_TenableIO|Pull vulnerabilities from Tenable.io. Note: connector works with plugin families in whitelist.|False|
|Connector_8_TenableSecurityCenter|Tenable Security Center Connector|False|
|Connector_6_TrendVisionOne|Pull information about workbench alerts from Trend Vision One. Note: dynamic list filter works with "model" parameter.|False|
|Connector_4_VaronisDataSecurityPlatform|Connector can be used to fetch alerts from the Varonis Data Security Platform. The connector dynamic list can be used to filter specific alerts for ingestion based on the Varonis Data Security Platform alert name.|False|
|Connector_3_Vectra|Vectra - Detections Connector|False|
|Connector_5_VirusTotalV3|Pull information about Livehunt notifications and related files from VirusTotal. Note: this connector requires a premium API token. Dynamic list works with "rule_name" parameter.|False|
|Connector_2_Zabbix|Zabbix connector - fetches events from Zabbix.|False|


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
|VisualFamily_1|Description for VisualFamily_1|
|VisualFamily_10|Description for VisualFamily_10|
|VisualFamily_11|Description for VisualFamily_11|
|VisualFamily_12|Description for VisualFamily_12|
|VisualFamily_13|Description for VisualFamily_13|
|VisualFamily_14|Description for VisualFamily_14|
|VisualFamily_15|Description for VisualFamily_15|
|VisualFamily_16|Description for VisualFamily_16|
|VisualFamily_17|Description for VisualFamily_17|
|VisualFamily_18|Description for VisualFamily_18|
|VisualFamily_19|Description for VisualFamily_19|
|VisualFamily_2|Description for VisualFamily_2|
|VisualFamily_20|Description for VisualFamily_20|
|VisualFamily_21|Description for VisualFamily_21|
|VisualFamily_22|Description for VisualFamily_22|
|VisualFamily_23|Description for VisualFamily_23|
|VisualFamily_24|Description for VisualFamily_24|
|VisualFamily_25|Description for VisualFamily_25|
|VisualFamily_26|Description for VisualFamily_26|
|VisualFamily_27|Description for VisualFamily_27|
|VisualFamily_28|Description for VisualFamily_28|
|VisualFamily_29|Description for VisualFamily_29|
|VisualFamily_3|Description for VisualFamily_3|
|VisualFamily_30|Description for VisualFamily_30|
|VisualFamily_4|Description for VisualFamily_4|
|VisualFamily_5|Description for VisualFamily_5|
|VisualFamily_6|Description for VisualFamily_6|
|VisualFamily_7|Description for VisualFamily_7|
|VisualFamily_8|Description for VisualFamily_8|
|VisualFamily_9|Description for VisualFamily_9|


## Jobs
|Name|Description|
|----|-----------|
|Google Chronicle Sync Job|This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM. Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.|


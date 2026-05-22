# GitSync

## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|Google Chronicle - Chronicle Alerts Connector|Pull information about Rule based alerts from Google Chronicle. Note: dynamic list is used for filtering purposes. For all of the details please visit the documentation portal.|True|


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
|1New Playbook||
|2New Playbook||
|New Playbook||
|Nw Playbook||
|IMPORT 1 - SecMon_Enrichment_and_Triage_Block|An embedded workflow that can receive inputs and return an output.|
|SecMon_Enrichment_and_Triage_Block|An embedded workflow that can receive inputs and return an output.|
|Carbon Black Cloud Remediation||
|Copy of Carbon Black Cloud Remediation - 1||


## Visual Families
|Name|Description|
|----|-----------|
|AV_THBn|newaddedmanually|
|Carbon Black File Modifications|VMware Carbon Black EDR captures four types of file system activity: File creation – the creation of a new file. File Write – the first time a file is written to after being opened or created. File Write Complete – the closing of a file that was written to.This event includes both the file path and also the MD5/SHA256 of the written file. The event is only captured for binaries (Windows PE files such as EXE, DLL and drivers), Adobe Docs (PDF), OfficeXML docs (docx, doc, xlsx, xls, pptx, ppt)  and zip archives (zip) that are smaller than 10MB in size. Can be enabled or disabled independently of filemod collection by deselecting "Non-binary file writes" Not available on macOS and Linux sensors File deletion – the deletion of an existing file.|
|Carbon Black Network Connections Event|VMware Carbon Black EDR captures network connections with the following characteristics: Both TCP over IPv4 or UDP over IPv4 connections Both inbound and outbound connections Network connections record TCP or UDP protocol, the remote IPv4 address, port and the domain name associated with the remote IPv4 Address Inbound connections capture the local port. If the sensor is installed on a typically configured web server, the reported port is 80. Outbound connections capture the remote port, uutbound connections made after DNS resolution the name that resolves to the captured IPV4 address is also reported. The sensor utilizes a passive sensing approach to capturing the domain name, so no additional network traffic is generated in order to capture the name. For DNS/DHCP servers, high CPU and/or memory can be seen due to the high number of netconn events. Rather than disabling all netconns, disable DNS capture on that machine. CB Response: Windows Sensor Causing High CPU/memory Utilization on Netconn Intense Server.|
|Carbon Black Process Event|Cross Process Event and Child Process Events: VMware Carbon Black EDR provides a cross-process event type that records an occurrence of a process that crosses the security boundary of another process. While some of these events are benign, others can indicate an attempt to change the behavior of the target process by a malicious process.|



# NessusScanner

Nessus is deployed by millions of users worldwide to identify vulnerabilities, policy-violating configurations and malware that attackers use to penetrate your or your customer's network.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://{ip-address}:{port}|
|Access Key|None|True|String||
|Secret Key|None|True|Password|*****|



## Actions
#### Create Scan
Create a new scan in Nessus with a template
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scan Name|Scan display name.|True|String||
|Scan Template Title|Scan template title value.|True|String||
|Description|Description content.|False|String||



#### Get Scan Templates
Get all scan templates from the server
Timeout - 600 Seconds



#### Get Scans
Fetch a list of existing scans
Timeout - 600 Seconds



#### Get Scan Report
Get a full report on the scan results
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scan Name|Scan display name.|True|String||



#### Launch Scan
Launch scan on the Nessus server
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scan Name|Scam display name.|True|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds






## Jobs

#### LaunchScanAndGetAReport
Job for initiating scan in Nessus and get scan report

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Api Root|True|String||
|Access Key|True|String||
|Secret Key|True|String||
|Scan Name|True|String||
|Scan Download Path|True|String||




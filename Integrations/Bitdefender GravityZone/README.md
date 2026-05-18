
# Bitdefender GravityZone

Bitdefender Control Center API's allow developers and SOC's to automate business workflows. Docs: https://github.com/snags141/SiemplifyIntegration_BitdefenderGravityZone

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Key|API Key generated under "My Account"|True|Password||
|Access URL|Access URL for Control Center API|True|String||
|Verify SSL|Verify SSL when making requests|False|Boolean||


#### Dependencies
| |
|-|
|certifi-2025.6.15-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|urllib3-2.5.0-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|


## Actions
#### Create Scan Task
This method creates a task to isolate the specified endpoint.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Task Name|The name of the task. If the parameter is not passed, the name will be automatically generated.|False|None||
|Target IDs|A list with the IDs of the targets to scan. The target ID can designate an endpoint or a container.|True|None||
|Scan Type|The type of scan. Available options are: 1 - quick scan; 2 - full scan; 3 - memory scan; 4 - custom scan|True|None||
|Custom Scan - Depth|The scan profile. Available options: 1 - aggressive; 2 - normal; 3 - permissive. This parameter is only used when scan type is Custom|False|None||
|Custom Scan - Paths|Comma-separated list of target paths to be scanned. This parameter is only used when scan type is Custom|False|None||



#### Create Scan Task by MAC Address
Use this method to generate a scan task for managed endpoints identified by their MAC address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|MAC Addresses|The list of mac addresses of the endpoints to be scanned. You can specify at most 100 MAC addresses at once|True|None||
|Scan Type|The type of scan. Available options are: 1 - quick scan; 2 - full scan; 3 - memory scan; 4 - custom scan|True|None||
|Task Name|The name of the task. If the parameter is not passed, the name will be automatically generated.|False|None||
|Custom Scan - Depth|The scan profile. Available options: 1 - aggressive; 2 - normal; 3 - permissive. This parameter is only used when scan type is Custom|False|None||
|Custom Scan - Paths|Comma-separated list of target paths to be scanned. This parameter is only used when scan type is Custom|False|None||



#### Get Custom Groups List
This method retrieves the list of groups under a specified group.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Parent ID|Parent group ID for which the child groups will be listed. 'Computers and Groups' and 'Deleted' groups are returned if the passed parameter is null.|False|None||



#### Blocklist - List Items
This method lists all the hashes that are present in the blocklist.
Timeout - 600 Seconds



#### Get Endpoints List
Get list of endpoints
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter - SSID|The SSID (Active Directory SID of the endpoint) used to filter the endpoints regardless of their protection status.|False|None||
|Filter - Depth - All Items Recursively|Boolean to filter all endpoints recursively within the Network Inventory of a company.|False|None||
|Filter - Security Servers|Boolean to filter all Security Servers|False|None||
|Filter - Managed Relays|Boolean to filter all endpoints with Relay role. |False|None||
|Filter - Managed Exchange Servers|Boolean to filter all protected Exchange servers.|False|None||
|Parent ID|The ID of the target company or group. If not specified or set with a company ID, the method returns only the endpoints under Computers and Groups.|False|None||
|Endpoints|Select whether to return only managed endpoints, unmanaged endpoints, or all endpoints.|True|None||
|Filter - Managed with BEST|Boolean to filter all endpoints with the security agent installed on them.|False|None||
|Filter - Name|A string for filtering the items by name. Minimum required string length is three characters.|False|None||
|Filter - MAC Addresses|Comma-separated list of MAC addresses used to filter the endpoints regardless of their protection status.|False|None||



#### Get Managed Endpoint Details
This method returns detailed information, such as: details to identify the endpoint and the security agent, the status of installed protection modules.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Endpoint ID|The ID of the endpoint for which the details will be returned|True|None||



#### Get Scan Tasks List
This method returns the list of scan tasks.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Task Status|The status of the task.|True|None||
|Task Name|Use an asterisk in front to search its appearance anywhere in the name. If omitted, only returns results where the name starts with the keyword|False|None||



#### Isolate Endpoint
This method creates a task to isolate the specified endpoint.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Endpoint ID|The ID of the endpoint for which the details will be returned|True|None||



#### Ping

Timeout - 600 Seconds



#### Policies - Get Details
This method retrieves all information related to a security policy.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy ID|The ID of the policy to be queried.|True|None||



#### Quarantine - Add File
This method creates a new task to add a file to quarantine.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Path|The absolute file path on disk. This can be at most 4096 characters in length and should have the format suitable to the target's operating system.|True|None||
|Endpoint IDs|A list with the IDs of the target endpoints. Max 100 targets at once. Only endpoints having the EDR Sensor module active are considered valid targets.|True|None||



#### Policies - List All
This method retrieves the list of available policies.
Timeout - 600 Seconds



#### Blocklist - Add Hashes
Use this method to add one or more file hashes to the Blocklist. Hashes supported: SHA256, MD5.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hash List|A comma-separated list of SHA256 or MD5 hashes.|True|None||
|Source Info|A description for the hashes.|True|None||



#### Quarantine - Remove Items
This method creates a new task to remove items from quarantine.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Service|Allowed services are: computers, for "Computers and Virtual Machines" or exchange, for "Security for Exchange"|True|None||
|Quarantine Item IDs|Comma-separated list of quarantine items IDs. The maximum number of items that can be removed once is 100.|True|None||



#### Quarantine - Get Items List
This method retrieves the list of quarantined items available for a company. An item can be a file or an Microsoft Exchange object.
The filter fields Threat Name, File Path, and IP Address work with partial matching.
The filter returns the items which are exact match or start with the specified value.
To use the specified value as a suffix, use the asterisk symbol (*). For example:
If filePath is C:\temp, the API returns all items originating from this folder, including sub-folders.
If filePath is *myfile.exe, then the API returns a list of all myfile.exe files from anywhere on the system.
The Exchange filters require a valid license key for Security for Exchange.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Service|Allowed services are: computers, for "Computers and Virtual Machines" or exchange, for "Security for Exchange"|True|None||
|Filter - Threat Name|Filters the quarantined items by threat name.This filter is available for computers and exchange services.|False|None||
|Filter - Start Date|Filters the items that quarantined after the specified date. Format for startDate is in ISO 8601.The filter is available for computers and exchange.|False|None||
|Filter - End Date|Filters the items quarantined before the specified date.Format for startDate is in ISO 8601.The filter is available for computers and exchange.|False|None||
|Filter - File Path|Filters the quarantined items by file path. This filter is available for computers service.|False|None||
|Filter - IP Address|Filters the quarantine items by IP address. This filter is available for computers service.|False|None||
|Filter - Action Status|Filters the quarantine items by action status. "Pending Save" Is only available to the Exchange Service.|False|None||
|Endpoint ID|ID of the computer for which you want to retrieve the quarantined items. If not passed, he method returns the items quarantined in the entire network.|False|None||



#### Quarantine - Restore Items
This method creates a new task to restore items from the quarantine.

Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Location to Restore|The absolute path to the folder where the items will be restored. If the parameter is not set, the original location will be used.|False|None||
|Quarantine Item IDs|Comma-separated list of quarantine items IDs. The maximum number of items that can be removed once is 100.|True|None||
|Service|Allowed services are: computers, for "Computers and Virtual Machines" or exchange, for "Security for Exchange"|True|None||
|Add Exclusion in Policy|Exclude the files to be restored from future scans. Exclusions do not apply to items with the Default Policy assigned.|False|None||



#### Set Endpoint Label
This method sets a new label to an endpoint.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Label|A string representing the label. The maximum allowed length is 64 characters. Enter an empty string to reset a previously set label.|True|None||
|Endpoint ID|The ID of the endpoint for which the details will be returned|True|None||



#### Blocklist - Remove Item
This method removes an item from the Blocklist, identified by its ID
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Hash ID|The ID of the item in the Blocklist to be deleted|True|None||



#### Get Hourly Usage for EC2 Instances
This method exposes the hourly usage for each Amazon instance category (micro, medium etc.).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Target Month|The month for which the usage is returned. The month will be provided in the following format: mm/yyyy. The default value is the current month.|True|None||



#### Get Network Inventory Items
This method returns network inventory items. Note - Some filters require a specific license to be active, otherwise they are ignored, resulting in an inaccurate API response. The field name works with partial matching.
The filter returns the items whose names are exact match or start with the specified value. To use the specified value as a suffix, use the asterisk symbol (*).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter - Name|A string for filtering the items by name. Minimum required string length is three characters.|False|None||
|Filter - MAC Addresses|Comma-separated list of MAC addresses used to filter the endpoints regardless of their protection status.|False|None||
|Filter - SSID|The SSID (Active Directory SID of the endpoint) used to filter the endpoints regardless of their protection status.|False|None||
|Filter - Depth - All Items Recursively|Boolean to filter all endpoints recursively within the Network Inventory of a company.|False|None||
|Filter - Security Servers|Boolean to filter all Security Servers|False|None||
|Filter - Managed Relays|Boolean to filter all endpoints with Relay role. |False|None||
|Filter - Managed Exchange Servers|Boolean to filter all protected Exchange servers.|False|None||
|Filter - Managed with BEST|Boolean to filter all endpoints with the security agent installed on them.|False|None||
|Filter - Virtual Machines|Boolean to filter all virtual machines.|False|None||
|Filter - Computers|Boolean to filter all computers.|False|None||
|Filter - EC2 Instances|Boolean to filter all Amazon EC2 Instances.|False|None||
|Filter - Groups|Boolean to filter all custom groups of endpoints.|False|None||
|Parent ID|The ID of the container for which the network items will be returned.|False|None||



#### Quarantine - Restore Exchange Items
This method creates a new task to restore items from the quarantine for Exchange Servers.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|EWS URL|The Exchange Web Services URL .The EWS URL is necessary when the Exchange Autodiscovery does not work.|False|None||
|Email|The email address of the Exchange user. This parameter is necessary when the email address is different from the username.|False|None||
|Password|The password of an Exchange user|True|None||
|Username|The username of an Microsoft Exchange user. The username must include the domain name.|True|None||
|Quarantine Item IDs|Comma-separated list of quarantine items IDs. The maximum number of items that can be removed once is 100.|True|None||



#### Restore Isolated Endpoint
This method creates a task to restore the specified endpoint from isolation.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Endpoint ID|The ID of the endpoint for which the details will be returned|True|None||



#### Reports - Get Download Links
This method returns an Object with information regarding the report availability for download and the corresponding download links.
The instant report is created one time only and available for download for less than 24 hours.
Scheduled reports are generated periodically and all report instances are saved in the GravityZone database.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|The report ID to fetch|True|None||



#### Reports - List All
This method returns the list of scheduled reports, according to the parameters received.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report Name|The name of the report.|False|None||
|Report Type|The report type.|False|None||










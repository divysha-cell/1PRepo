
# MISP

MISP is an open source software solution for collecting, storing, distributing and sharing cyber security indicators and threat about cyber security incidents

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://{IP}|
|Api Key|None|True|Password|*****|
|Use SSL|None|False|Boolean|False|
|CA Certificate File - parsed into Base64 String|None|False|String||


#### Dependencies
| |
|-|
|idna-3.8-py3-none-any.whl|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|


## Actions
#### Add Sighting to an Attribute
Add a sighting to attributes in MISP
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|Specify a comma-separated list of attribute identifiers to which you want to add a new sighting. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Event ID|Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if “Attribute Search“ is set to “Provided Event“.|False|String||
|Category|Specify a comma-separated list of categories. If specified, action will only add sightings to attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Type|Specify a comma-separated list of attribute types. If specified, action will only add sightings to attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst|False|String||
|Sightings Type|Specify the type of the Sighting.|True|List|Sighting|
|Source|Specify the source for the sighting. Example: SIEM, SOAR, Siemplify.|False|String||
|Date Time|Specify the date time for the sighting. Format: 2020-02-10 11:00:00.|False|String||
|Object UUID|Specify the uuid of the object that contains the desired attribute|False|String||
|Attribute Search|Specify, where action should search for attributes. If “Provided Event“ is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in “Event ID“ parameter. If “All Events“, action will search for attributes among all events and add sighting for all attributes that match our criteria. |False|List|Provided Event|
|Attribute UUID|Specify a comma-separated list of attribute UUIDs to which you want to add a new sighting. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values. |False|String||



#### Enrich Entities
Enrich entities based on the attributes in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Number of attributes to return|Specify how many attributes to return for entities.|True|String|300|
|Filtering condition|Specify the filtering condition for the action. If “Last“ is selected, action will use the oldest attribute for enrichment, if “First“ is selected, action will use the newest attribute for enrichment.|True|List|LAST|
|Create Insights|If enabled, action will generate an insight for every entity that was fully processed.|False|Boolean|true|
|Threat Level Threshold|Specify what should be the threshold for the threat level of the event, where the entity was found. If related event exceeds or matches threshold, entity will be marked as suspicious.|False|List|Low|



#### Get Related Events
Retrieve information about events that are related to entities in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Events Limit|Specify max amount of events to fetch. If not specified, all events will be fetched.|False|String||
|Mark As Suspicious|If enabled, action will mark entity as suspicious, if there is at least one related event to it.|False|Boolean|true|



#### Add Tag to an Event
Add tags to event in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event, for which you want to add tags.|True|String||
|Tag Name|Specify a comma-separated list of tags that you want to add to events.|True|String||



#### Create File Misp Object
Create a File Object in MISP. Requires one of: FILENAME, MD5, SHA1, SHA256, SSDEEP to be provided or “Use Entities“ parameter set to true.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event for which you want to add file objects.|True|String||
|FILENAME|Specify the name of the file, which you want to add to the event.|False|String||
|MD5|Specify the md5 of the file, which you want to add to the event.|False|String||
|SHA1|Specify the sha1 of the file, which you want to add to the event.|False|String||
|SHA256|Specify the sha256 of the file, which you want to add to the event.|False|String||
|SSDEEP|Specify the ssdeep of the file, which you want to add to the event. Format: size:hash:hash|False|String||
|Use Entities|If enabled, action will use entities in order to create objects. Supported entities: File name and hash. “Use Entities“ has priority over other parameters.|False|Boolean|false|



#### List Sightings of an Attribute
List available sightings for attributes in MISP
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|Specify a comma-separated list of attribute identifiers for which you want to list sightings. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Event ID|Specify the ID or UUID of the event, where to seach for attributes. This parameter is required, if “Attribute Search“ is set to “Provided Event“.|False|String||
|Category|Specify a comma-separated list of categories. If specified, action will only list sightings for attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Type|Specify a comma-separated list of attribute types. If specified, action will only list sightings for attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst|False|String||
|Attribute Search|Specify, where action should search for attributes. If “Provided Event“ is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in “Event ID“ parameter. If “All Events“, action will search for attributes among all events and list sightings for all attributes that match our criteria.|False|List|Provided Event|
|Attribute UUID|Specify a comma-separated list of attribute UUIDs for which you want to list sightings. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||



#### Create network-connection Misp Object
Create a network-connection Object in MISP. Requires one of: Dst-port, Src-port, IP-Src, IP-Dst to be provided or “Use Entities“ parameter set to true.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event to which you want to add network-connection objects.|True|String||
|Dst-port|Specify the destination port, which you want to add to the event.|False|String||
|Src-port|Specify the source port, which you want to add to the event.|False|String||
|Hostname-src|Specify the source hostname, which you want to add to the event.|False|String||
|Hostname-dst|Specify the source destination, which you want to add to the event.|False|String||
|IP-Src|Specify the source IP, which you want to add to the event.|False|String||
|IP-Dst|Specify the destination IP, which you want to add to the event.|False|String||
|Layer3-protocol|Specify the related layer 3 protocol, which you want to add to the event.|False|String||
|Layer4-protocol|Specify the related layer 4 protocol, which you want to add to the event.|False|String||
|Layer7-protocol|Specify the related layer 7 protocol, which you want to add to the event.|False|String||
|Use Entities|If enabled, action will use entities in order to create objects. Supported entities: IP Address. “Use Entities“ has priority over other parameters.|False|Boolean|false|
|IP Type|Specify what attribute type should be used with IP entities.|False|List|Source IP|



#### Delete an Attribute
Delete attributes in MISP. Supported hashes: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SSDeep.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|Specify a comma-separated list of attribute identifiers that you want to delete. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Event ID|Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if “Attribute Search“ is set to “Provided Event“ or Object UUID is provided.|False|String||
|Category|Specify a comma-separated list of categories. If specified, action will only delete attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Type|Specify a comma-separated list of attribute types. If specified, action will only delete attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst|False|String||
|Object UUID|Specify the uuid of the object that contains the desired attribute|False|String||
|Attribute UUID|Specify a comma-separated list of attribute UUIDs that you want to delete. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Attribute Search|Specify, where action should search for attributes. If “Provided Event“ is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in “Event ID“ parameter. If “All Events“, action will search for attributes among all events and delete all attributes that match our criteria.|False|List|Provided Event|



#### Create Url Misp Object
Create a URL Object in MISP. Requires “URL” to be provided or “Use Entities“ parameter set to true.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event to which you want to add URL objects.|True|String||
|URL|Specify the URL, which you want to add to the event.|False|String||
|Port|Specify the port, which you want to add to the event.|False|String||
|First seen|Specify, when the URL was first seen. Format: 2020-12-22T13:07:32Z|False|String||
|Last seen|Specify, when the URL was last seen. Format: 2020-12-22T13:07:32Z|False|String||
|Domain|Specify the domain, which you want to add to the event.|False|String||
|Text|Specify the additional text, which you want to add to the event.|False|String||
|IP|Specify the IP, which you want to add to the event.|False|String||
|Host|Specify the Host, which you want to add to the event.|False|String||
|Use Entities|If enabled, action will use entities in order to create objects. Supported entities: URL. “Use Entities“ has priority over other parameters.|False|Boolean|false|



#### Set IDS Flag for an Attribute
Set IDS flag for attributes in MISP
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|Specify a comma-separated list of attribute identifiers for which you want to set an IDS flag. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Event ID|Specify the ID or UUID of the event, where to seach for attributes. This parameter is required, if “Attribute Search“ is set to “Provided Event“.|False|String||
|Category|Specify a comma-separated list of categories. If specified, action will only set IDS flag for attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Type|Specify a comma-separated list of attribute types. If specified, action will only set IDS flag for attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst|False|String||
|Attribute Search|Specify, where action should search for attributes. If “Provided Event“ is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in “Event ID“ parameter. If “All Events“, action will search for attributes among all events and set IDS flag for all attributes that match our criteria.|False|List|Provided Event|
|Attribute UUID|Specify a comma-separated list of attribute UUIDs for which you want to set an IDS flag. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||



#### Download File
Download files related to event in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event from which you want to download files|False|String||
|Download Folder Path|Specify the absolute path to the folder, which should store files. If nothing is specified, action will create an attachment instead. Note: JSON result is only available, when you provide proper value for this parameter.|False|String||
|Overwrite|If enabled, action will overwrite existing files.|False|Boolean|false|



#### Unset IDS Flag for an Attribute
Unset IDS flag for attributes in MISP
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|Specify a comma-separated list of attribute identifiers for which you want to unset an IDS flag. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Event ID|Specify the ID or UUID of the event, where to seach for attributes. This parameter is required, if “Attribute Search“ is set to “Provided Event“.|False|String||
|Category|Specify a comma-separated list of categories. If specified, action will only unset IDS flag for attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Type|Specify a comma-separated list of attribute types. If specified, action will only unset IDS flag for attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst|False|String||
|Attribute Search|Specify, where action should search for attributes. If “Provided Event“ is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in “Event ID“ parameter. If “All Events“, action will search for attributes among all events and unset IDS flag for all attributes that match our criteria.|False|List|Provided Event|
|Attribute UUID|Specify a comma-separated list of attribute UUIDs for which you want to unset an IDS flag. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||



#### Get Event Details
Retrieve details about events in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify a comma-separated list of IDs or UUIDs of the events for which you want retrieve details.|True|String||
|Return Attributes Info|If enabled, action will create a case wall table for all of the attributes that are a part of the event.|False|Boolean|True|



#### List Event Objects
Retrieve information about available objects in MISP event.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify a comma-separated list of IDs and UUIDs of the events, for which you want to retrieve details.|True|String||
|Max Objects to Return|Specify how many objects to return.|False|String|50|



#### Add Tag to an Attribute
Add tags to attributes in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|Specify a comma-separated list of attribute identifiers to which you want to add tags. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Event ID|Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if “Attribute Search“ is set to “Provided Event“ or Object UUID is provided.|False|String||
|Tag Name|Specify a comma-separated list of tags that you want to add to attributes.|True|String||
|Category|Specify a comma-separated list of categories. If specified, action will only add tags to attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Type|Specify a comma-separated list of attribute types. If specified, action will only add tags to attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst|False|String||
|Object UUID|Specify the uuid of the object that contains the desired attribute.|False|String||
|Attribute UUID|Specify a comma-separated list of attribute UUIDs to which you want to add new tags. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Attribute Search|Specify, where action should search for attributes. If “Provided Event“ is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in “Event ID“ parameter. If “All Events“, action will search for attributes among all events and add sighting for all attributes that match our criteria.|False|List|Provided Event|



#### Create Event
Create a new event in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event Name|Specify the name for the new event.|True|String||
|Distribution|Specify the distribution of the event. Possible values: 0 - Organisation, 1 - Community, 2 - Connected, 3 - All. You can either provide a number or a string.|False|String|Community|
|Threat Level|Specify the threat level of the event. Possible values: 1 - High, 2 - Medium, 3 - Low, 4 - Undefined. You can either provide a number or a string.|False|String|High|
|Analysis|Specify the analysis of the event. Possible values: 0 - Initial, 1 - Ongoing, 2 - Completed. You can either provide a number or a string.|False|String|Initial|
|Publish|If enabled, action will publish the event to the community.|False|Boolean|false|
|Comment|Specify additional comments related to the event.|False|String||



#### Remove Tag from an Attribute
Remove tags from attributes in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attribute Name|Specify a comma-separated list of attribute identifiers from which you want to remove tags. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Event ID|Specify the ID or UUID of the event, where to search for attributes. This parameter is required, if “Attribute Search“ is set to “Provided Event“ or Object UUID is provided.|False|String||
|Tag Name|Specify a comma-separated list of tags that you want to remove from attributes.|True|String||
|Category|Specify a comma-separated list of categories. If specified, action will only remove tags from attributes that have matching category. If nothing is specified, action will ignore categories in attributes. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Type|Specify a comma-separated list of attribute types. If specified, action will only remove tags from attributes that have matching attribute type. If nothing is specified, action will ignore types in attributes. Example values: md5, sha1, ip-src, ip-dst|False|String||
|Object UUID|Specify the UUID of the object that contains the desired attribute.|False|String||
|Attribute UUID|Specify a comma-separated list of attribute UUIDs from which you want to remove new tags. Note: If both “Attribute Name“ and “Attribute UUID“ are specified, action will work with “Attribute UUID“ values.|False|String||
|Attribute Search|Specify, where action should search for attributes. If “Provided Event“ is selected, action will only search for attributes or attribute UUIDs in event with ID/UUID provided in “Event ID“ parameter. If “All Events“, action will search for attributes among all events and remove tags from all attributes that match our criteria.|False|List|Provided Event|



#### Create Virustotal-Report Object
Create a Virustotal-Report Object in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event to which you want to add URL objects.|True|String||
|Permalink|Specify the link to the VirusTotal report, which you want to add to the event.|True|String||
|Comment|Specify the comment, which you want to add to the event.|False|String||
|Detection Ratio|Specify the detection ration, which you want to add to the event.|False|String||
|Community Score|Specify the community score, which you want to add to the event.|False|String||
|First Submission|Specify first submission of the event. Format: 2020-12-22T13:07:32Z|False|String||
|Last Submission|Specify last submission of the event. Format: 2020-12-22T13:07:32Z|False|String||



#### Remove Tag from an Event
Remove tags from event in MISP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event, from which you want to remove tags.|True|String||
|Tag Name|Specify a comma-separated list of tags that you want to remove from events.|True|String||



#### Create IP-Port Misp Object
Create a IP-Port Object in MISP. Requires one of: Dst-port, Src-port, Domain, HOSTNAME, IP-Src, IP-Dst to be provided or “Use Entities“ parameter set to true.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event to which you want to add IP-Port objects.|True|String||
|Dst-port|Specify the destination port, which you want to add to the event.|False|String||
|Src-port|Specify the source port, which you want to add to the event.|False|String||
|Domain|Specify the domain, which you want to add to the event.|False|String||
|HOSTNAME|Specify the hostname, which you want to add to the event.|False|String||
|IP-Src|Specify the source IP, which you want to add to the event.|False|String||
|IP-Dst|Specify the destination IP, which you want to add to the event.|False|String||
|Use Entities|If enabled, action will use entities in order to create objects. Supported entities: IP Address. “Use Entities“ has priority over other parameters.|False|Boolean|false|
|IP Type|Specify what attribute type should be used with IP entities.|False|List|Source IP|



#### Delete an Event
Delete event in MISP
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event that you want to delete.|True|String||



#### Add Attribute
Add attributes based on entities to the event in MISP. Supported hashes: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SSDeep.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|TheSpecify the ID or UUID of the event, for which you want to add attributes.|True|String||
|Category|Specify the category for attributes. Possible values: Targeting data, Payload delivery, Artifacts dropped, Payload installation, Persistence mechanism, Network activity, Attribution, External analysis, Social network.|False|String||
|Distribution|Specify the distribution of the attribute. Possible values: 0 - Organisation, 1 - Community, 2 - Connected, 3 - All, 5 - Inherit. You can either provide a number or a string.|False|String|Community|
|For Intrusion Detection System|If enabled, attribute will be labeled as eligible to create an IDS signature out of it.|False|Boolean|false|
|Comment|Specify comment related to attribute.|False|String||
|Fallback IP Type|Specify what should be the fallback attribute type for the IP address entity.|False|List|Source Address|
|Fallback Email Type|Specify what should be the fallback attribute type for the email address entity.|False|List|Source Email Address|
|Extract Domain|If enabled, action will extract domain out of URL entity.|False|Boolean|true|



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Unpublish Event
The action allows the user to unpublish an event. Unpublishing an event prevents it from being visible to the shared groups.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event that you want to unpublish.|True|String||



#### Upload File
Upload a file to a MISP event.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event to which you want to upload this file.|True|String||
|File Path|Specify a comma-separated list of absolute filepaths of the files that you want to upload to MISP.|True|String||
|Category|Specify the category for the uploaded file. Possible values: External Analysis, Payload Delivery, Artifacts Dropped, Payload Installation.|False|String||
|Distribution|Specify the distribution for the uploaded file. Possible values: 0 - Organisation, 1 - Community, 2 - Connected, 3 - All. You can either provide a number or a string.|False|String|Community|
|For Intrusion Detection System|If enabled, uploaded file will be used for intrusion detection systems.|False|Boolean|False|
|Comment|Specify additional comments related to the uploaded file.|False|String||



#### Publish Event
The action allows the user to publish an event. Publishing an event shares it to the sharing group selected, making it visible to all members.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Event ID|Specify the ID or UUID of the event that you want to publish.|True|String||









## Connectors
#### MISP - Attributes Connector
Pull attributes from MISP.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API Root for MISP account.|True|String||
|API Key|API Key of the MISP account.|True|Password|*****|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve attributes from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|1|
|Max Attributes Per Cycle|How many attributes to process per one connector iteration.|True|Int|50|
|Lowest Threat Level To Fetch|Lowest severity that will be used to fetch alerts. Possible values: 1-4.|True|String|1|
|Attribute Type Filter|Filter attributes by their type, comma separated. If provided, only attributes with whitelisted type will be processed.|False|String||
|Category Filter|Filter attributes by their category, comma separated. If provided, only attributes with whitelisted category will be processed.|False|String||
|Galaxy Filter|Filter attributes by their parent event's galaxy, comma separated. If provided, only attributes that belong to an event with a whitelisted galaxy will be processed.|False|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the CheckPoint Cloud Guard server is valid.|False|Boolean|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|CA Certificate File - parsed into Base64 String|CA Certificate File - parsed into Base64 String|False|String||





Read123!@#
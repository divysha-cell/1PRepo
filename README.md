# GitSync

## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|Crowdstrike - Alerts Connector|Pull alerts from Crowdstrike. Dynamic List works with the "display_name" parameter. Note: To fetch identity protection detections use "Identity Protection Detections Connector".|False|


## Playbooks
|Name|Description|
|----|-----------|
|Crowdstrike Falcon Containment|This block performs containment on endpoints by targeting case-related IPs and hostnames to prevent further compromise. A boolean input controls manual or automatic execution. In automatic mode, the Upload IOCs and Isolate Endpoint flags determine which actions run. It returns true if successful, false on failure, or empty if no action is taken.|
|Google SecOps SIEM Enrichment|This block enriches entities and retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.|
|Crowdstrike Falcon Containment|This block performs containment on endpoints by targeting case-related IPs and hostnames to prevent further compromise. A boolean input controls manual or automatic execution. In automatic mode, the Upload IOCs and Isolate Endpoint flags determine which actions run. It returns true if successful, false on failure, or empty if no action is taken.|
|New Block|An embedded workflow that can receive inputs and return an output.|
|New Playbook||


## Visual Families
|Name|Description|
|----|-----------|
|Copy of AV|Anti-virus alerts visualization|
|Copy of AV_3nzr|Anti-virus alerts visualization|
|Copy of OS|User activity on machine|
|Copy of RACF|Mainframe resource access|


## Jobs
|Name|Description|
|----|-----------|
|Google Chro|This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM. Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/37/jobInstances/41|Automated random job 22 for integration Jira template Sync Closure|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/38/jobInstances/42|Automated random job 23 for integration Jira template Sync Comments|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/37/jobInstances/54|Automated random job 35 for integration Jira template Sync Closure|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/38/jobInstances/55|Automated random job 36 for integration Jira template Sync Comments|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/37/jobInstances/67|Automated random job 48 for integration Jira template Sync Closure|
|projects/project/locations/location/instances/instance/integrations/Jira/jobs/38/jobInstances/68|Automated random job 49 for integration Jira template Sync Comments|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/35/jobInstances/29|Automated random job 10 for integration LogRhythm template Sync Closed Cases|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/33/jobInstances/37|Automated random job 18 for integration LogRhythm template Sync Closed Alarms|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/34/jobInstances/38|Automated random job 19 for integration LogRhythm template Sync Case Comments|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/35/jobInstances/39|Automated random job 20 for integration LogRhythm template Sync Closed Cases|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/36/jobInstances/40|Automated random job 21 for integration LogRhythm template Sync Alarm Comments|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/33/jobInstances/50|Automated random job 31 for integration LogRhythm template Sync Closed Alarms|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/34/jobInstances/51|Automated random job 32 for integration LogRhythm template Sync Case Comments|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/35/jobInstances/52|Automated random job 33 for integration LogRhythm template Sync Closed Cases|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/36/jobInstances/53|Automated random job 34 for integration LogRhythm template Sync Alarm Comments|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/33/jobInstances/63|Automated random job 44 for integration LogRhythm template Sync Closed Alarms|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/34/jobInstances/64|Automated random job 45 for integration LogRhythm template Sync Case Comments|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/35/jobInstances/65|Automated random job 46 for integration LogRhythm template Sync Closed Cases|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/36/jobInstances/66|Automated random job 47 for integration LogRhythm template Sync Alarm Comments|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/33/jobInstances/27|Automated random job 8 for integration LogRhythm template Sync Closed Alarms|
|projects/project/locations/location/instances/instance/integrations/LogRhythm/jobs/34/jobInstances/28|Automated random job 9 for integration LogRhythm template Sync Case Comments|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/32/jobInstances/36|Automated random job 17 for integration QRadar template SyncCloseOffenses|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/32/jobInstances/49|Automated random job 30 for integration QRadar template SyncCloseOffenses|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/32/jobInstances/62|Automated random job 43 for integration QRadar template SyncCloseOffenses|
|projects/project/locations/location/instances/instance/integrations/QRadar/jobs/32/jobInstances/26|Automated random job 7 for integration QRadar template SyncCloseOffenses|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/28/jobInstances/32|Automated random job 13 for integration ServiceNow template Sync Table Record Comments By Tag|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/29/jobInstances/33|Automated random job 14 for integration ServiceNow template Sync Table Record Comments|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/30/jobInstances/34|Automated random job 15 for integration ServiceNow template Sync Incidents Job|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/31/jobInstances/35|Automated random job 16 for integration ServiceNow template Sync Closed Incidents|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/28/jobInstances/45|Automated random job 26 for integration ServiceNow template Sync Table Record Comments By Tag|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/29/jobInstances/46|Automated random job 27 for integration ServiceNow template Sync Table Record Comments|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/30/jobInstances/47|Automated random job 28 for integration ServiceNow template Sync Incidents Job|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/31/jobInstances/48|Automated random job 29 for integration ServiceNow template Sync Closed Incidents|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/28/jobInstances/22|Automated random job 3 for integration ServiceNow template Sync Table Record Comments By Tag|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/28/jobInstances/58|Automated random job 39 for integration ServiceNow template Sync Table Record Comments By Tag|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/29/jobInstances/23|Automated random job 4 for integration ServiceNow template Sync Table Record Comments|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/29/jobInstances/59|Automated random job 40 for integration ServiceNow template Sync Table Record Comments|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/30/jobInstances/60|Automated random job 41 for integration ServiceNow template Sync Incidents Job|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/31/jobInstances/61|Automated random job 42 for integration ServiceNow template Sync Closed Incidents|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/30/jobInstances/24|Automated random job 5 for integration ServiceNow template Sync Incidents Job|
|projects/project/locations/location/instances/instance/integrations/ServiceNow/jobs/31/jobInstances/25|Automated random job 6 for integration ServiceNow template Sync Closed Incidents|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/26/jobInstances/20|Automated random job 1 for integration Splunk template Sync Splunk ES Comments|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/26/jobInstances/30|Automated random job 11 for integration Splunk template Sync Splunk ES Comments|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/27/jobInstances/31|Automated random job 12 for integration Splunk template Sync Splunk ES Closed Events|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/27/jobInstances/21|Automated random job 2 for integration Splunk template Sync Splunk ES Closed Events|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/26/jobInstances/43|Automated random job 24 for integration Splunk template Sync Splunk ES Comments|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/27/jobInstances/44|Automated random job 25 for integration Splunk template Sync Splunk ES Closed Events|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/26/jobInstances/56|Automated random job 37 for integration Splunk template Sync Splunk ES Comments|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/27/jobInstances/57|Automated random job 38 for integration Splunk template Sync Splunk ES Closed Events|
|projects/project/locations/location/instances/instance/integrations/Splunk/jobs/26/jobInstances/69|Automated random job 50 for integration Splunk template Sync Splunk ES Comments|


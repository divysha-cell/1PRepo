# GitSync

## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|Crowdstrike - Alerts Connector|Pull alerts from Crowdstrike. Dynamic List works with the "display_name" parameter. Note: To fetch identity protection detections use "Identity Protection Detections Connector".|True|


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
|Job_Random_Jira_22|Automated random job 22 for integration Jira template Sync Closure|
|Job_Random_Jira_23|Automated random job 23 for integration Jira template Sync Comments|
|Job_Random_Jira_35|Automated random job 35 for integration Jira template Sync Closure|
|Job_Random_Jira_36|Automated random job 36 for integration Jira template Sync Comments|
|Job_Random_Jira_48|Automated random job 48 for integration Jira template Sync Closure|
|Job_Random_Jira_49|Automated random job 49 for integration Jira template Sync Comments|
|Job_Random_LogRhythm_10|Automated random job 10 for integration LogRhythm template Sync Closed Cases|
|Job_Random_LogRhythm_18|Automated random job 18 for integration LogRhythm template Sync Closed Alarms|
|Job_Random_LogRhythm_19|Automated random job 19 for integration LogRhythm template Sync Case Comments|
|Job_Random_LogRhythm_20|Automated random job 20 for integration LogRhythm template Sync Closed Cases|
|Job_Random_LogRhythm_21|Automated random job 21 for integration LogRhythm template Sync Alarm Comments|
|Job_Random_LogRhythm_31|Automated random job 31 for integration LogRhythm template Sync Closed Alarms|
|Job_Random_LogRhythm_32|Automated random job 32 for integration LogRhythm template Sync Case Comments|
|Job_Random_LogRhythm_33|Automated random job 33 for integration LogRhythm template Sync Closed Cases|
|Job_Random_LogRhythm_34|Automated random job 34 for integration LogRhythm template Sync Alarm Comments|
|Job_Random_LogRhythm_44|Automated random job 44 for integration LogRhythm template Sync Closed Alarms|
|Job_Random_LogRhythm_45|Automated random job 45 for integration LogRhythm template Sync Case Comments|
|Job_Random_LogRhythm_46|Automated random job 46 for integration LogRhythm template Sync Closed Cases|
|Job_Random_LogRhythm_47|Automated random job 47 for integration LogRhythm template Sync Alarm Comments|
|Job_Random_LogRhythm_8|Automated random job 8 for integration LogRhythm template Sync Closed Alarms|
|Job_Random_LogRhythm_9|Automated random job 9 for integration LogRhythm template Sync Case Comments|
|Job_Random_QRadar_17|Automated random job 17 for integration QRadar template SyncCloseOffenses|
|Job_Random_QRadar_30|Automated random job 30 for integration QRadar template SyncCloseOffenses|
|Job_Random_QRadar_43|Automated random job 43 for integration QRadar template SyncCloseOffenses|
|Job_Random_QRadar_7|Automated random job 7 for integration QRadar template SyncCloseOffenses|
|Job_Random_ServiceNow_13|Automated random job 13 for integration ServiceNow template Sync Table Record Comments By Tag|
|Job_Random_ServiceNow_14|Automated random job 14 for integration ServiceNow template Sync Table Record Comments|
|Job_Random_ServiceNow_15|Automated random job 15 for integration ServiceNow template Sync Incidents Job|
|Job_Random_ServiceNow_16|Automated random job 16 for integration ServiceNow template Sync Closed Incidents|
|Job_Random_ServiceNow_26|Automated random job 26 for integration ServiceNow template Sync Table Record Comments By Tag|
|Job_Random_ServiceNow_27|Automated random job 27 for integration ServiceNow template Sync Table Record Comments|
|Job_Random_ServiceNow_28|Automated random job 28 for integration ServiceNow template Sync Incidents Job|
|Job_Random_ServiceNow_29|Automated random job 29 for integration ServiceNow template Sync Closed Incidents|
|Job_Random_ServiceNow_3|Automated random job 3 for integration ServiceNow template Sync Table Record Comments By Tag|
|Job_Random_ServiceNow_39|Automated random job 39 for integration ServiceNow template Sync Table Record Comments By Tag|
|Job_Random_ServiceNow_4|Automated random job 4 for integration ServiceNow template Sync Table Record Comments|
|Job_Random_ServiceNow_40|Automated random job 40 for integration ServiceNow template Sync Table Record Comments|
|Job_Random_ServiceNow_41|Automated random job 41 for integration ServiceNow template Sync Incidents Job|
|Job_Random_ServiceNow_42|Automated random job 42 for integration ServiceNow template Sync Closed Incidents|
|Job_Random_ServiceNow_5|Automated random job 5 for integration ServiceNow template Sync Incidents Job|
|Job_Random_ServiceNow_6|Automated random job 6 for integration ServiceNow template Sync Closed Incidents|
|Job_Random_Splunk_1|Automated random job 1 for integration Splunk template Sync Splunk ES Comments|
|Job_Random_Splunk_11|Automated random job 11 for integration Splunk template Sync Splunk ES Comments|
|Job_Random_Splunk_12|Automated random job 12 for integration Splunk template Sync Splunk ES Closed Events|
|Job_Random_Splunk_2|Automated random job 2 for integration Splunk template Sync Splunk ES Closed Events|
|Job_Random_Splunk_24|Automated random job 24 for integration Splunk template Sync Splunk ES Comments|
|Job_Random_Splunk_25|Automated random job 25 for integration Splunk template Sync Splunk ES Closed Events|
|Job_Random_Splunk_37|Automated random job 37 for integration Splunk template Sync Splunk ES Comments|
|Job_Random_Splunk_38|Automated random job 38 for integration Splunk template Sync Splunk ES Closed Events|
|Job_Random_Splunk_50|Automated random job 50 for integration Splunk template Sync Splunk ES Comments|


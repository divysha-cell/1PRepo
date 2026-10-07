## Google Chro
This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM.
 Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.


**Run Interval In Seconds:** 3600

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Environment|String|True|Default Environment|
|API Root|String|True|https://backstory.googleapis.com|
|User's Service Account|Password|False|*****|
|Workload Identity Email|Password|False|*****|
|Max Hours Backwards|String|False|24|
|Verify SSL|Boolean|False|true|

## Google Chronicle Sync Job
This job will synchronize information about Chronicle SOAR Cases and Chronicle SOAR Alerts with Chronicle SIEM.
 Note: This job is only supported from Chronicle SOAR version 6.1.44 and higher.


**Run Interval In Seconds:** 3600

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Environment|String|True|Default Environment|
|API Root|String|True|https://us-chronicle.googleapis.com/v1alpha/projects/84044654851/locations/us/instances/1ce5182d-fdba-4dca-a71f-1b748e42f580|
|User's Service Account|Password|False|*****|
|Workload Identity Email|Password|False|*****|
|Max Hours Backwards|String|False|24|
|Verify SSL|Boolean|False|false|

## Job_Random_Jira_22
Automated random job 22 for integration Jira template Sync Closure


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{jira_address}|
|Username|String|False||
|API Token|Password|True|*****|
|Environment|String|False||
|Project Names|String|True|project names separated by comma|
|Days Backwards|String|True|1|

## Job_Random_Jira_23
Automated random job 23 for integration Jira template Sync Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{jira_address}|
|Username|String|False||
|API Token|Password|True|*****|
|Environment|String|False||
|Project Names|String|False|project names separated by comma|
|Days Backwards|String|False|1|
|Siemplify Comment Prefix|String|True|Google SecOps:|
|Jira Comment Prefix|String|True|Jira Comment Sync Job:|

## Job_Random_Jira_35
Automated random job 35 for integration Jira template Sync Closure


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{jira_address}|
|Username|String|False||
|API Token|Password|True|*****|
|Environment|String|False||
|Project Names|String|True|project names separated by comma|
|Days Backwards|String|True|1|

## Job_Random_Jira_36
Automated random job 36 for integration Jira template Sync Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{jira_address}|
|Username|String|False||
|API Token|Password|True|*****|
|Environment|String|False||
|Project Names|String|False|project names separated by comma|
|Days Backwards|String|False|1|
|Siemplify Comment Prefix|String|True|Google SecOps:|
|Jira Comment Prefix|String|True|Jira Comment Sync Job:|

## Job_Random_Jira_48
Automated random job 48 for integration Jira template Sync Closure


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Environment|String|False||
|API Root|String|True|https://{jira_address}|
|Username|String|False||
|API Token|Password|True|*****|
|Project Names|String|True|project names separated by comma|
|Days Backwards|String|True|1|

## Job_Random_Jira_49
Automated random job 49 for integration Jira template Sync Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{jira_address}|
|Username|String|False||
|API Token|Password|True|*****|
|Environment|String|False||
|Project Names|String|False|project names separated by comma|
|Days Backwards|String|False|1|
|Siemplify Comment Prefix|String|True|Google SecOps:|
|Jira Comment Prefix|String|True|Jira Comment Sync Job:|

## Job_Random_LogRhythm_10
Automated random job 10 for integration LogRhythm template Sync Closed Cases


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_18
Automated random job 18 for integration LogRhythm template Sync Closed Alarms


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_19
Automated random job 19 for integration LogRhythm template Sync Case Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|

## Job_Random_LogRhythm_20
Automated random job 20 for integration LogRhythm template Sync Closed Cases


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_21
Automated random job 21 for integration LogRhythm template Sync Alarm Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|

## Job_Random_LogRhythm_31
Automated random job 31 for integration LogRhythm template Sync Closed Alarms


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_32
Automated random job 32 for integration LogRhythm template Sync Case Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|

## Job_Random_LogRhythm_33
Automated random job 33 for integration LogRhythm template Sync Closed Cases


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_34
Automated random job 34 for integration LogRhythm template Sync Alarm Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|

## Job_Random_LogRhythm_44
Automated random job 44 for integration LogRhythm template Sync Closed Alarms


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_45
Automated random job 45 for integration LogRhythm template Sync Case Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|

## Job_Random_LogRhythm_46
Automated random job 46 for integration LogRhythm template Sync Closed Cases


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_47
Automated random job 47 for integration LogRhythm template Sync Alarm Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|

## Job_Random_LogRhythm_8
Automated random job 8 for integration LogRhythm template Sync Closed Alarms


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Max Hours Backwards|String|False|24|

## Job_Random_LogRhythm_9
Automated random job 9 for integration LogRhythm template Sync Case Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https:/{{IP}}:8501|
|Api Token|Password|True|*****|
|Verify SSL|Boolean|False|true|

## Job_Random_QRadar_17
Automated random job 17 for integration QRadar template SyncCloseOffenses


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://x.x.x.x|
|API Token|Password|True|*****|
|API Version|String|False||
|Days Backwards|Int|False|1|

## Job_Random_QRadar_30
Automated random job 30 for integration QRadar template SyncCloseOffenses


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://x.x.x.x|
|API Token|Password|True|*****|
|API Version|String|False||
|Days Backwards|Int|False|1|

## Job_Random_QRadar_43
Automated random job 43 for integration QRadar template SyncCloseOffenses


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://x.x.x.x|
|API Token|Password|True|*****|
|API Version|String|False||
|Days Backwards|Int|False|1|

## Job_Random_QRadar_7
Automated random job 7 for integration QRadar template SyncCloseOffenses


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://x.x.x.x|
|API Token|Password|True|*****|
|API Version|String|False||
|Days Backwards|Int|False|1|

## Job_Random_ServiceNow_13
Automated random job 13 for integration ServiceNow template Sync Table Record Comments By Tag


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Table Name|String|True|dummy_val|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_14
Automated random job 14 for integration ServiceNow template Sync Table Record Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Table Name|String|True|dummy_val|

## Job_Random_ServiceNow_15
Automated random job 15 for integration ServiceNow template Sync Incidents Job


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Sync Level|String|True|Case|
|Max Hours Backwards|Int|True|24|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_16
Automated random job 16 for integration ServiceNow template Sync Closed Incidents


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Max Hours Backwards|Int|False|24|
|Table Name|String|True|dummy_val|

## Job_Random_ServiceNow_26
Automated random job 26 for integration ServiceNow template Sync Table Record Comments By Tag


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Table Name|String|True|dummy_val|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_27
Automated random job 27 for integration ServiceNow template Sync Table Record Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Table Name|String|True|dummy_val|

## Job_Random_ServiceNow_28
Automated random job 28 for integration ServiceNow template Sync Incidents Job


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Sync Level|String|True|Case|
|Max Hours Backwards|Int|True|24|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_29
Automated random job 29 for integration ServiceNow template Sync Closed Incidents


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Max Hours Backwards|Int|False|24|
|Table Name|String|True|dummy_val|

## Job_Random_ServiceNow_3
Automated random job 3 for integration ServiceNow template Sync Table Record Comments By Tag


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Table Name|String|True|dummy_val|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_39
Automated random job 39 for integration ServiceNow template Sync Table Record Comments By Tag


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Table Name|String|True|dummy_val|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_4
Automated random job 4 for integration ServiceNow template Sync Table Record Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Table Name|String|True|dummy_val|

## Job_Random_ServiceNow_40
Automated random job 40 for integration ServiceNow template Sync Table Record Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Table Name|String|True|dummy_val|

## Job_Random_ServiceNow_41
Automated random job 41 for integration ServiceNow template Sync Incidents Job


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Sync Level|String|True|Case|
|Max Hours Backwards|Int|True|24|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_42
Automated random job 42 for integration ServiceNow template Sync Closed Incidents


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Max Hours Backwards|Int|False|24|
|Table Name|String|True|dummy_val|

## Job_Random_ServiceNow_5
Automated random job 5 for integration ServiceNow template Sync Incidents Job


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Sync Level|String|True|Case|
|Max Hours Backwards|Int|True|24|
|Verify SSL|Boolean|False|true|

## Job_Random_ServiceNow_6
Automated random job 6 for integration ServiceNow template Sync Closed Incidents


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Api Root|String|True|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|String|True|dummy_val|
|Password|Password|True|*****|
|Verify SSL|Boolean|False|true|
|Client ID|String|False||
|Client Secret|Password|False|*****|
|Refresh Token|Password|False|*****|
|Use Oauth Authentication|Boolean|False|false|
|Max Hours Backwards|Int|False|24|
|Table Name|String|True|dummy_val|

## Job_Random_Splunk_1
Automated random job 1 for integration Splunk template Sync Splunk ES Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_11
Automated random job 11 for integration Splunk template Sync Splunk ES Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_12
Automated random job 12 for integration Splunk template Sync Splunk ES Closed Events


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|Max Hours Backwards|String|False|24|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_2
Automated random job 2 for integration Splunk template Sync Splunk ES Closed Events


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|Max Hours Backwards|String|False|24|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_24
Automated random job 24 for integration Splunk template Sync Splunk ES Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_25
Automated random job 25 for integration Splunk template Sync Splunk ES Closed Events


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|Max Hours Backwards|String|False|24|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_37
Automated random job 37 for integration Splunk template Sync Splunk ES Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_38
Automated random job 38 for integration Splunk template Sync Splunk ES Closed Events


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|Max Hours Backwards|String|False|24|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||

## Job_Random_Splunk_50
Automated random job 50 for integration Splunk template Sync Splunk ES Comments


**Run Interval In Seconds:** 120

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Server Address|String|True|https://<ip>:8089|
|Username|String|False||
|Password|Password|False|*****|
|API Token|Password|False|*****|
|CA Certificate File|String|False||
|Verify SSL|Boolean|False||


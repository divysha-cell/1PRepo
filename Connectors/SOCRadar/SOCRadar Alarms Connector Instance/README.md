# SOCRadar Alarms Connector Instance



Integration: SOCRadar

Integration Version: 1

Device Product Field: device_product

Event Name Field: alarm_id
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Environment Field Name|Name of the field where the environment name is stored. If empty, uses default environment.|False|dummy_value|
|Environment Regex Pattern|A regex pattern to run on the environment field value.|False|.*|
|API Root|SOCRadar API base URL.|True|https://platform.socradar.com/api|
|API Key|SOCRadar platform API key with Incident API V4 permissions.|True|*****|
|Company ID|SOCRadar company identifier (numeric).|True|dummy_value|
|Verify SSL|Enable SSL certificate verification for API requests.|False|true|
|Max Alerts Per Cycle|Maximum number of alarms to ingest per polling cycle.|False|100|
|Extract Indicators|Extract IOCs (IP, URL, Email, MD5, SHA1, SHA256) from alarm content as separate indicator events for entity mapping. Default true.|False|true|
|Severity Filter|Comma-separated severity levels to fetch: LOW, MEDIUM, HIGH, CRITICAL. Leave empty for all.|False|dummy_value|
|Status Filter|Status filter: OPEN, CLOSED, ON_HOLD. Default: OPEN.|False|OPEN|
|Main Type Filter|Comma-separated alarm main types. E.g.: Attack Surface Management, Deep & Dark Web Monitoring. Leave empty for all.|False|dummy_value|
|Sub Type Filter|Comma-separated alarm sub-types. E.g.: Stolen Credentials On Dark Web Bot Market. Leave empty for all.|False|dummy_value|
|Tags Filter|Comma-separated tags to filter alarms by. Leave empty for all.|False|dummy_value|
|Assignees Filter|Comma-separated assignee names or emails to filter alarms by. Leave empty for all.|False|dummy_value|


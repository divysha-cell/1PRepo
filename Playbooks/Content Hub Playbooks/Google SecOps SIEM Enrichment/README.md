# Google SecOps SIEM Enrichment
This block enriches entities and retrieves relevant details about users and assets involved in the case, enhancing the context available for analysis and subsequent actions within Google SecOps SOAR.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Join Emails|Form query string from given parameters.|SiemplifyUtilities|Query Joiner|
|User and Email Query|Action sets a value for a key specified that is stored in the Siemplify database. Available scopes to get context values for: Alert, Case, Global. Action is not working on Siemplify entities. Note: Key Name parameter is case insensitive.|Siemplify|Set Scope Context Value|
|Target Resource Activity|Execute custom UDM query in Google Chronicle. Note: 120 action executions are allowed per hour.|GoogleChronicle|Execute UDM Query|
|Enrich Entities|Enrich entities using information from Google SecOps. Supported entities: File Hash, IP Address, Domain, Hostname, URL (extracts domain part of URL), User, Email (User entity with email regex). Note: this action only works with Chronicle API authentication. Backstory API is not supported.|GoogleChronicle|Enrich Entities|
|User Query|Action sets a value for a key specified that is stored in the Siemplify database. Available scopes to get context values for: Alert, Case, Global. Action is not working on Siemplify entities. Note: Key Name parameter is case insensitive.|Siemplify|Set Scope Context Value|
|Emails Query|Action sets a value for a key specified that is stored in the Siemplify database. Available scopes to get context values for: Alert, Case, Global. Action is not working on Siemplify entities. Note: Key Name parameter is case insensitive.|Siemplify|Set Scope Context Value|
|User Activity|Execute custom UDM query in Google Chronicle. Note: 120 action executions are allowed per hour.|GoogleChronicle|Execute UDM Query|
|Join Emails 2|Form query string from given parameters.|SiemplifyUtilities|Query Joiner|


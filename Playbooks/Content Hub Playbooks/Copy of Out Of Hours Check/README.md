# Copy of Out Of Hours Check
This Block will check if the Alert is processing outside of typical business hours.  Some alert responses might react different (e.g. OOH escalation) at different parts of the day.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|
|teamHourOnline|08|
|teamHourOffline|17|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Tag OOH|Add given tag to the case the current alert is grouped to|Siemplify|Case Tag|
|Siemplify_Case Comment_1|Add a comment to the case the current alert has been grouped to|Siemplify|Case Comment|
|GetHour|Returns the current date and time |Tools|Get Current Time|


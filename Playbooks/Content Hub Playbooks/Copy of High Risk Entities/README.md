# Copy of High Risk Entities
This block increases the alert risk score when risky entities from a custom list are detected. It receives the Custom List Category and a Risk Score Increase value as inputs, which are used to increase the alert score if matches are found. The block returns true if successful or false on failure.



**Enabled:** True

**Version:** 0

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False



##### Input Parameters
|Name|Default Value|
|----|-------------|
|Custom List Category|High Risk Users|
|Risky Score Increase|10|



### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|Find Matches|This action will render a Jinja2 template using a JSON input.  |TemplateEngine|Render Template|
|Update Alert Score|This will update the alert score by the amount supplied in the 'Input' parameter. |Tools|Update Alert Score|
|Retrieve Relevant Entities|Search a specified string within the records of an environment's custom list. (If no values are provided will return all custom lists records)|Lists|Search Environment Custom Lists|


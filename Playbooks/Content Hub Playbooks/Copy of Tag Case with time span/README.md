# Copy of Tag Case with time span
A Block that Tags the case with the time span between Alerts.  Can be used for Case queue filters.



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
|Get Case Data||Tools|Get Case Data|
|Remainder Results|This action will render a Jinja2 template using a JSON input.  |TemplateEngine|Render Template|
|Subtract first from last|A set of built in math operators:Plus - returns a result for the sum of 2 argumentsSub - returns a result for 1 argument minus the otherMulti - returns a result for 1 argument multiplied by the otherDiv - returns a result for 1 argument divided by the otherMod - returns the result of the percentage between 2 arguments|Functions|Math Arithmetic|
|Tag Time Span|Add given tag to the case the current alert is grouped to|Siemplify|Case Tag|
|Round Results||Functions|Math Functions|
|Remove Tag|Remove tags from a case.|Siemplify|Remove Tag|
|Get existing Case Tags||Functions|String Functions|
|Delta in ms to minutes||Functions|Math Arithmetic|


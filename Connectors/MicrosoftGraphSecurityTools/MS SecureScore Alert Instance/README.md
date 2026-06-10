# MS SecureScore Alert Instance



Integration: MicrosoftGraphSecurityTools

Integration Version: 4

Device Product Field: Microsoft 365

Event Name Field: SecureScore
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Threshold|Specify the Secure Score threshold. If your Secure Score drops below this threshold, an alert will be raised.|False|0|
|Tenant ID|Tenant ID  from Azure|True|x|
|Secret ID|Secret ID from Azure|True|*****|
|Default Priority|Set the default priority (-1 to 100). Informative = -1, Low = 40, Medium = 60, High = 80, Critical = 100|True|60|
|Client ID|Client ID from Azure|True|x|
|Certificate Path|If authentication based on certificates is used instead of client secret, specify path to the certificate on Siemplify server|False|dummy_value|
|Certificate Password|Optional, if certificate is password-protected, specify the password to open the certificate file.|False|*****|


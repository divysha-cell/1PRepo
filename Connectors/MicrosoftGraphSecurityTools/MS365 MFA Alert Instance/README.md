# MS365 MFA Alert Instance



Integration: MicrosoftGraphSecurityTools

Integration Version: 4

Device Product Field: Microsoft 365

Event Name Field: MFA Alert
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Tenant ID|Tenant ID from Azure|True|x|
|Self Service Reset Alert|Create alert when a user has the ability to self-service reset their password/MFA.|False|false|
|Secret ID|Secret ID from Azure|True|*****|
|MFA Registration Alert|Create alert when a user is not registered for MFA. Recommended.|False|true|
|Exclude Guests|Exclude guests/external users from alerts (emails containing #EXT#)|False|false|
|Client ID|Client ID from Azure|True|x|
|Certificate Path|If authentication based on certificates is used instead of client secret, specify path to the certificate on Siemplify server|False|dummy_value|
|Certificate Password|Optional, if certificate is password-protected, specify the password to open the certificate file.|False|*****|


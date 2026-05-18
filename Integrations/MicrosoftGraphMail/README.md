
# MicrosoftGraphMail

Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Azure AD Endpoint|The Microsoft Entra endpoint to connect to.|True|String||
|Microsoft Graph Endpoint|The Microsoft Graph endpoint to connect to.|True|String||
|Client ID|The client (application) ID of the Microsoft Entra application to use in the integration.|True|String||
|Secret ID|The client secret value of the Microsoft Entra app to use in the integration.|True|Password||
|Tenant|The Microsoft Entra ID (tenant ID) value.|True|String||
|Default Mailbox|The default mailbox to use in the integration.|True|String||
|Mail field source|If enabled, user's mailbox address will be fetched from the 'mail' attribute of user's details. Otherwise, user's mailbox address will be fetched from the 'userPrincipalName' field.|False|Boolean||
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|Password||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|Password||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|Password||
|Verify SSL|If selected, the integration verifies that the SSL certificate for the connection to the Microsoft Graph server is valid.|False|Boolean||


#### Dependencies
| |
|-|
|proto_plus-1.25.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|siemplify_html2text-2020.1.16-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|emaildata-0.3.4-py3-none-any.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|anyio-4.6.2.post1-py3-none-any.whl|
|red-black-tree-mod-1.20.tar.gz|
|soupsieve-2.6-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|google_auth-2.36.0-py2.py3-none-any.whl|
|urllib3-2.2.3-py3-none-any.whl|
|extract_msg-0.52.0-py3-none-any.whl|
|oletools-0.60.2-py2.py3-none-any.whl|
|exceptiongroup-1.2.2-py3-none-any.whl|
|easygui-0.98.3-py2.py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|pyth3-0.7-py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|ebcdic-1.1.1-py2.py3-none-any.whl|
|msoffcrypto_tool-5.4.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|icalendar-6.0.1-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|pytz-2024.2-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|pcodedmp-1.2.6-py2.py3-none-any.whl|
|httpcore-1.0.6-py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|tzdata-2024.2-py2.py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|IMAPClient-3.0.1-py2.py3-none-any.whl|
|charset_normalizer-3.4.0-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|olefile-0.47-py2.py3-none-any.whl|
|googleapis_common_protos-1.65.0-py2.py3-none-any.whl|
|tzlocal-5.2-py3-none-any.whl|
|compressed_rtf-1.0.6.tar.gz|
|RTFDE-0.1.2-py3-none-any.whl|
|google_api_core-2.23.0-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|colorclass-2.2.2-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|google_api_python_client-2.151.0-py2.py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|TIPCommon-2.2.16-py2.py3-none-any.whl|
|PyJWT-2.9.0-py3-none-any.whl|
|lark-1.1.9-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Forward Email
Forward email including previous threads. If permissions allow, action can send an email from a mailbox different that is specified in the integration configuration. Note: Action is not running on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Specify the optional email address from which if permissions allow, email should be sent. By default, the email will be sent from the default mailbox specified in the integration configuration.|True|None||
|Mail ID|Specify the mail ids or internetMessageIds of the message that you want to forward.|True|None||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|None||
|Subject|Specify the mail subject part.|True|None||
|Send to|Specify the arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|None||
|CC|Specify the arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the 'Send to' field.|False|None||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the 'Send to' field.|False|None||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|None||
|Mail Content|Specify the email body part.|True|None||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|None||



#### Send Vote Email
Send email with easy answering options, to allow stakeholders to be included in workflow processes. This action uses Google SecOps HTML templates to format the email. If permissions allow, the action sends an email from a mailbox different than the one specified in the integration configuration. Note: This action is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Optional email address to send an email from (if permissions allow it). By default, the email is sent from the default mailbox specified in the integration configuration.|True|None||
|Subject|Email subject.|True|None||
|Send to|Arbitrary comma-separated list of email addresses for the email recipients, for example, user1@company.co, user2@company.co.|True|None||
|CC|Arbitrary comma-separated list of email addresses to use in the CC email field. Use the same format as for the "Send to" field.|False|None||
|BCC|Arbitrary comma-separated list of email addresses to use in the BCC email field. Use the same format for the "Send to" field.|False|None||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|None||
|Email HTML Template|The question you would like to ask, or describe the decision you would like the recipient to be able to respond to|True|None||
|Structure of voting options|Structure of the vote to send to the recipients.|True|None||
|Reply-To Recipients|Comma-separated list of recipients used in the Reply-To header. Note: The Reply-To header is added to force email replies to specific email addresses instead of the email sender address stated in the From field.|False|None||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|None||



#### Extract Data from Attached EML
Extract data from the email EML attachments and return it in the actions JSON result. The action supports .eml, .msg, .ics file formats. Note: Action is not running on SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|By default, the action attempts to search for an email in the default mailbox specified in the integration configuration. If permissions allow, the action can execute search in other mailboxes. This parameter accepts multiple values as a comma-separated string.|True|None||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|None||
|Mail IDs|Specify the mail ids or internetMessageIds to search for. This parameter accepts multiple values as a comma-separated string.|True|None||
|Regex Map JSON|JSON definition containing regular expressions to apply to the attached email file and produce additional key values in the action JSON result. Example of the JSON definition is as follows: {ips: \b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\b}|False|None||



#### Get Mailbox Account Out Of Facility Settings
Get the mailbox account out of facility (OOF) settings for the provided Google SecOps User entity. Note: This action uses the beta version of Microsoft Graph APIs.
Timeout - 600 Seconds



#### Mark Email as Not Junk
Mark an email as not junk for a specific mailbox. This action removes the sender from the list of blocked senders and moves the message to the Inbox folder. Note: This action uses the beta version of Microsoft Graph APIs and is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|A mailbox to search for an email in. By default, the action  attempts to search for the email in the default mailbox that you specified in the integration configuration. With correct permissions, the action can execute a search in other mailboxes. Parameter accepts multiple values as a comma separated string. |True|None||
|Folder Name|A mailbox folder to search in.|True|None||
|Mail IDs|Specify the mail ids or internetMessageIds to mark as not junk. Parameter accepts multiple values as a comma separated string.|True|None||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Move Email To Folder
Move one or multiple emails from source email folder to another folder in the mailbox. If permissions allow, action can move emails in mailboxes other than the one provided in the integration configuration. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Move In Mailbox|By default, move operation will be executed in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well. If permissions allow, action can search in other mailboxes as well. Parameter accepts multiple values as a comma separated string.|True|None||
|Source Folder Name|Specify the source folder name to move mail from. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None||
|Destination Folder Name|Specify the destination folder name to move mail to. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None||
|Mail IDs|Specify the mail ids or internetMessageIds to search for. Parameter accepts multiple values as a comma separated string. If mail id or internet message id is provided, it takes priority for the search, subject and sender filters are ignored.|False|None||
|Subject Filter|Specify the subject of the email to search for. Filter works with "contains" logic.|False|None||
|Sender Filter|Specify the sender of the email to search for. Filter works with "equals" logic.|False|None||
|Time Frame (minutes)|Specify time frame in minutes to search emails for.|False|None||
|Only Unread|If enabled, action searches only for the unread emails.|False|None||
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch (single connection to O365). If nothing is provided, default value of 25 will be used.|False|None||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|None||
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|None||



#### Download Attachments from Email
Download attachments from an email based on the provided criteria. Note: Action is not running on SecOps entities. Action is running asynchronously. Adjust the script timeout value in the SecOps IDE for action as needed. If the downloaded attachments contain "/" or "\" characters in their names, the characters will be replaced with the '_' character.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|By default, the action  attempts to search for an email in the default mailbox specified in the integration configuration. If permissions allow, the action can execute search in other mailboxes. This parameter accepts multiple values as a comma-separated string.|True|None||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|None||
|Download Destination|Destination to save the downloaded attachments to. By default, the action attempts to save the attachment to the Google Cloud storage bucket. Saving an attachment to the local file system is a fallback option.|True|None||
|Download Path|Path to download attachments to. When saving attachments to the Google Cloud bucket or a local file system, the action expects download path to be specified in the unix-like format, for example, “/tmp/test”.|True|None||
|Mail IDs|Specify the mail ids or internetMessageIds to search for. Parameter accepts multiple values as a comma separated string. If mail id or internet message id is provided, it takes priority for the search, subject and sender filters are ignored.|False|None||
|Subject Filter|Specify the subject of the email to search for. Filter works with "contains" logic.|False|None||
|Sender Filter|Specify the sender of the email to search for. Filter works with "equals" logic.|False|None||
|Download Attachments from EML|If checked, the action downloads attachments from attached EML files.|False|None||
|Download Attachments to unique path?|If checked, the action downloads attachments to the unique path under the path value provided in the “Download Path” parameter to avoid overwiting of previously downloaded attachments.|False|None||
|How many mailboxes to process in a single batch|Number of  mailboxes to process in a single batch (single connection to O365). If no value is provided, the default value of 25 mailboxes is used.|False|None||



#### Send Email
Send email from a specific mailbox to an arbitrary list of recipients. Action can send either plain text or html emails. If permissions allow, action can send an email from a mailbox different that is specified in the integration configuration. Note: Action is not running on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|CC|Specify the arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the "Send to" field.|False|None||
|Send From|Specify the optional email address from which if permissions allow, email should be sent. By default, the email will be sent from the default mailbox specified in the integration configuration.|True|None||
|Subject|Specify the mail subject part.|True|None||
|Send to|Specify the arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|None||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the "Send to" field.|False|None||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|None||
|Mail Content Type|Specify the type of email content: either plain text or html.|False|None||
|Mail Content|Specify the email body part.|True|None||
|Reply-To Recipients|Specify a comma-separated list of recipients that will be used in the "Reply-To" header. Note: The Reply-To header is added when the originator of the message wants any replies to the message to go to that particular email address rather than the one in the "From:" address.|False|None||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|None||



#### Send Email HTML
Send email with the Google SecOps HTML template from a specific mailbox to an arbitrary list of recipients. If permissions allow, the action sends an email from a mailbox different than the one specified in the integration configuration. Note: Action is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Optional email address to send an email from (if permissions allow it). By default, the email is sent from the default mailbox specified in the integration configuration.|True|None||
|Subject|Email subject.|True|None||
|Send to|Specify the arbitrary comma-separated list of email addresses for the email recipients,for example, user1@company.co, user2@company.co.|True|None||
|CC|Arbitrary comma-separated list of email addresses to use in the CC email field. Use the same format as for the "Send to" field.|False|None||
|BCC|Arbitrary comma-separated list of email addresses to use in the BCC email field. Use the same format for the "Send to" field.|False|None||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|None||
|Email HTML Template|The question you would like to ask, or describe the decision you would like the recipient to be able to respond to|True|None||
|Reply-To Recipients|Comma-separated list of recipients used in the Reply-To header. Note: The Reply-To header is added to force email replies to specific email addresses instead of the email sender address stated in the From field.|False|None||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|None||



#### Search Emails
Execute email search in the configured mailbox based on provided search criteria. If permissions allow, action can search in mailboxes other than the one provided in the integration configuration. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search in Mailbox|By default, the search will be executed in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well. Parameter accepts multiple values as a comma separated string. Note that it’s not recommended to perform a search against a big number of mailboxes with this action, for complex searches it is recommended to use Exchange Extension Pack.|True|None||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None||
|Subject Filter|Specify the subject of the email to search for. Filter works with “contains” logic.|False|None||
|Sender Filter|Specify the sender of the email to search for. Filter works with “equals” logic.|False|None||
|Time Frame (minutes)|Specify time frame in minutes to search emails for.|False|None||
|Max Emails To Return|Specify how many emails action should return. If value is not provided, API default is used.|False|None||
|Only Unread|If enabled, action will search only for unread emails.|False|None||
|Select All Fields For Return|If enabled, action will return all available fields for the found email.|False|None||
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch (single connection to O365). If nothing is provided, default value of 25 will be used.|False|None||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|None||
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|None||



#### Wait For Email From User
Wait for user's response based on an email sent via the "Send Mail" action. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mail ID|Specify the id or internetMessageId of the email, which current action would be waiting for. If the message has been sent using Send Email action, please select SendEmail.JSONResult|id or Send Email.JsonResult|internetMessageId field as a placeholder. Search Emails action also can return ids for emails.|True|None||
|Wait for All Recipients to Reply?|If enabled,  the action will wait for responses from all of the recipients until timeout, and not finish upon getting the first response.|False|None||
|Wait Stage Exclude pattern|Specify the regular expression to exclude specific replies from the wait stage. Works with subject and body parts of the email. Example is, to exclude automatic Out-Of-Office emails to be considered as recipient reply, and instead wait for actual user reply.|False|None||
|Folder to Check for Reply|Specify the mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|None||
|Fetch Response Attachments|If enabled, if recipient replies with attachment - fetch recipient response and add it as attachment for the action result.|False|None||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|None||
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|None||



#### Send Thread Reply
Send a message as a reply to the email thread. If permissions allow, action can send an email from a mailbox different that is specified in the integration configuration. Note: Action is not running on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Send From|Specify the optional email address from which if permissions allow, email should be sent. By default, the email will be sent from the default mailbox specified in the integration configuration.|True|None||
|Mail ID|Specify the ID or internetMessageId of the message to which you want to send a reply.|True|None||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None||
|Attachments Paths|Specify the attachments to be added, parameter expects full paths to be provided, for example: /<work directory>/file1.pdf. Parameter accepts multiple values as a comma separated string.|False|None||
|Mail Content|Specify the email body part.|True|None||
|Reply All|If enabled, action will send a reply to all recipients related to the original email. Note: this parameter has priority over “Reply To“ parameter.|False|None||
|Reply To|Specify a comma-separated list of emails to which you want to send this reply. If nothing is provided and “Reply All“ is disabled, action will only send a reply to the sender of the email. If “Reply All“ is enabled, action will ignore this parameter.|False|None||
|Attachment Location|Location where the attachments to be added are stored. By default, the action attempts to get the attachment from the Google Cloud storage bucket, another option is to fetch it from the local file system.|True|None||



#### Mark Email as Junk
Mark an email as junk for a specific mailbox. This action adds the email sender to the list of blocked senders and moves the message to the Junk Email folder. Note: This action uses the beta version of Microsoft Graph APIs and is not running on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|A mailbox to search for an email in. By default, the action  attempts to search for the email in the default mailbox that you specified in the integration configuration. With correct permissions, the action can execute a search in other mailboxes. Parameter accepts multiple values as a comma separated string.|True|None||
|Folder Name|A mailbox folder to search in.|True|None||
|Mail IDs|Specify the mail ids or internetMessageIds to mark as junk. Parameter accepts multiple values as a comma separated string.|True|None||



#### Delete Email
Delete one or multiple emails from the mailbox based on provided search criteria. If permissions allow, action can move emails in mailboxes other than the one provided in the integration configuration. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Delete In Mailbox|By default, delete operation will be executed in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well. Parameter accepts multiple values as a comma separated string.|True|None||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None||
|Mail IDs|Specify the mail ids or internetMessageIds to search for. Parameter accepts multiple values as a comma separated string. If mail id or internet message id is provided, it takes priority for the search, subject and sender filters are ignored.|False|None||
|Subject Filter|Specify the subject of the email to search for. Filter works with “contains” logic.|False|None||
|Sender Filter|Specify the sender of the email to search for. Filter works with “equals” logic.|False|None||
|Time Frame (minutes)|Specify time frame in minutes to search emails for.|False|None||
|Only Unread|If enabled, action searches only for the unread emails.|False|None||
|How many mailboxes to process in a single batch|Specify how many mailboxes action should process in a single batch (single connection to O365). If nothing is provided, default value of 25 will be used.|False|None||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|None||
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|None||



#### Save Email to the Case
Save email or email attachments to the Chronicle Case Wall. If permissions allow, action can save emails from mailboxes other than the one provided in the integration configuration. Action is not working on Chronicle entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search In Mailbox|By default, action will try to search for email in the default mailbox specified in the integration configuration. If permissions allow, action can search in other mailboxes as well.|True|None||
|Folder Name|Specify the mailbox folder to search in. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|None||
|Mail ID|Specify the mail id or internetMessageId to save email and attachments to the case. If the message has been sent using Send Email action, please select SendEmail.JSONResult|id or Send Email.JsonResult|internetMessageId field as a placeholder. Search Emails action also can return ids for emails.|True|None||
|Save Only Email Attachments|If enabled, action will save only attachments of the specified email.|False|None||
|Attachment To Save|If "Save Only Email Attachments" checkbox is enabled, action can save only specific attachments that are specified in this parameter. Parameter accepts multiple values as a comma-separated string.|False|None||
|Base64 Encode|If enabled, encode the email file to base64 encoding.|False|None||
|Save Email to the Case Wall|If enabled, save the Email directly to the SecOps Case Wall.|False|None||



#### Wait For Vote Email Results
Wait for the user response based on the vote email sent using the Send Vote Email action. This action is asynchronous. Adjust the action timeout in the IDE accordingly. This action is not working on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vote Mail Sent From|By default, the email is sent from the default mailbox specified in the integration configuration. In this parameter optionally a different value can be specified, if the vote mail was sent from a different mailbox.|True|None||
|Mail ID|ID or internetMessageId of the vote email that the action waits for. If the message was sent using Send Vote Email action, select SendVoteEmail.JSONResult|id or Send Email.JsonResult|internetMessageId field as a placeholder. The Search Emails action also can return email IDs.|True|None||
|Wait for All Recipients to Reply?|If selected, the action waits for responses from all recipients until timeout and doesn't complete execution receiving the first response.|False|None||
|Wait Stage Exclude pattern|Regular expression to exclude specific replies from the wait stage. The regular expression works with the email subject and body. For example, you can use this parameter to exclude  automatic Out of Office emails wait for an actual user reply.|False|None||
|Folder to Check for Reply|Email folder in the mailbox that was used to send the email with question to search for the user reply in. Parameter also accepts a comma separated list of folders to check the user response in multiple folders. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|None||
|Folder to check for Sent Mail|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the sent mail in this folder. Parameter also accepts a comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|None||
|Fetch Response Attachments|If selected and the recipient replies with an attachment, the action fetches the recipient response and adds it as an attachment for the action result.|False|None||









## Connectors
#### Microsoft Graph Mail Connector
Connector can be used to fetch emails from the Microsoft Graph Mail service. Connector dynamic list can be used to filter specific values from the email body and subject parts using regexes. By default, regex is used to filter out the urls from the email.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Proxy Server Address|The address of the proxy server to use.|False|None||
|Proxy Username|The proxy username to authenticate with.|False|None||
|Proxy Password|The proxy password to authenticate with.|False|None||
|Mail field source|If enabled, user's mailbox address will be fetched from the 'mail' attribute of user's details. Otherwise, user's mailbox address will be fetched from the 'userPrincipalName' field.|False|None|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft Graph Mail server is valid.|False|None|true|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|None||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|None||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|None||
|Environment Field Name|Describes the name of the field where the environment name is stored.If environment field isn't found, environment is ""|False|None||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return value unchanged.Used to allow the user to manipulate the environment field via regex logicIf regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|None|.*|
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|None||
|Azure AD Endpoint|Azure AD endpoint to connect to. Can be different for different tenant types.|True|None|https://login.microsoftonline.com|
|Microsoft Graph Endpoint|Microsoft Graph endpoint to connect to.  Can be different for different tenant types.|True|None|https://graph.microsoft.com|
|Mail Address|Mail address to use for connector.|True|None||
|Client ID|For Office 365 Oauth authentication, Client (Application) ID of Azure Active Directory App that will be used for the integration.|True|None||
|Client Secret|For Office 365 Oauth authentication, secret can be provided for the auth flow.|True|None||
|Microsoft Entra ID Directory ID|For Microsoft 365 OAuth authentication, the tenant (directory) ID of the Microsoft Entra ID application that you used in the integration.|True|None||
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|None|Inbox|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve emails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|None|24|
|Max Emails Per Cycle|Fetch X emails per connector cycle|True|None|10|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|None|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read.|False|None|false|
|Disable Overflow|If enabled, the connector will ignore the Siemplify overflow mechanism when creating alerts.|False|None|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file.|False|None|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|None|orig|
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|None|attach|
|Create a Separate Siemplify Alert per Attached Mail File|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|None|false|
|Headers to add to events|Specify what values should be filtered from the "internetMessageHeaders" list and what will be added to the Siemplify event. By default, all headers are added, if only specific headers are needed - specify them as a comma separated list by their name, example: "DKIM-Signature", "Received", "From". If no internetHeaders should be added specify a keyword: None|False|None||
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|None||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|None||





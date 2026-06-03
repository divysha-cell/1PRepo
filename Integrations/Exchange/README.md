
# Exchange

Integration provides support for Microsoft Exchange 2010 - 2019 and Microsoft Office365 mail servers. Integration uses Exchange Web Services (EWS) for communication. Integration includes a series of actions to send out emails and work with received emails, along with a connector to monitor specific mailboxes and ingest emails from that mailboxes as alerts to Google SecOps for further analysis.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|ServerAddress|None|True|String||
|Mail Address|None|True|String||
|Domain|None|False|String||
|Use Domain For Authentication|None|False|Boolean|False|
|Use Autodiscover Service|None|False|Boolean|False|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|Boolean|False|
|Username|None|False|String||
|Password|None|False|Password|*****|
|Client ID|None|False|String||
|Client Secret|None|False|Password|*****|
|Tenant (Directory) ID|None|False|String||
|Redirect URL|None|False|String|http://localhost|
|Refresh Token|None|False|Password|*****|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|Password|*****|
|Verify SSL|None|False|Boolean|False|


#### Dependencies
| |
|-|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|setuptools-80.9.0-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|siemplify_html2text-2020.1.16-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|urllib3-2.3.0-py3-none-any.whl|
|emaildata-0.3.4-py3-none-any.whl|
|defusedxml-0.7.1-py2.py3-none-any.whl|
|pygments-2.18.0-py3-none-any.whl|
|pytz-2020.1-py2.py3-none-any.whl|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_auth-2.38.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.68.0-py2.py3-none-any.whl|
|dnspython-2.7.0-py3-none-any.whl|
|red-black-tree-mod-1.20.tar.gz|
|soupsieve-2.6-py3-none-any.whl|
|IMAPClient-2.1.0-py2.py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|cachetools-5.5.2-py3-none-any.whl|
|certifi-2025.1.31-py3-none-any.whl|
|anyio-4.8.0-py3-none-any.whl|
|extract_msg-0.52.0-py3-none-any.whl|
|oletools-0.60.2-py2.py3-none-any.whl|
|cached_property-2.0.1-py3-none-any.whl|
|oscrypto-1.3.0-py3-none-any.whl|
|pytest_runner-6.0.1-py3-none-any.whl|
|easygui-0.98.3-py2.py3-none-any.whl|
|asn1crypto-1.5.1-py2.py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|lxml-5.3.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|pyth3-0.7-py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|ebcdic-1.1.1-py2.py3-none-any.whl|
|msoffcrypto_tool-5.4.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|pyparsing-3.2.1-py3-none-any.whl|
|icalendar-6.0.1-py3-none-any.whl|
|python-smail-0.9.0.tar.gz|
|html2text-2024.2.26.tar.gz|
|isodate-0.7.2-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|protobuf-5.29.3-cp38-abi3-manylinux2014_x86_64.whl|
|six-1.16.0-py2.py3-none-any.whl|
|requests_ntlm-1.3.0-py3-none-any.whl|
|google_api_python_client-2.161.0-py2.py3-none-any.whl|
|requests_oauthlib-2.0.0-py2.py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|oauthlib-3.2.2-py3-none-any.whl|
|pcodedmp-1.2.6-py2.py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|tzdata-2024.2-py2.py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_core-2.24.1-py3-none-any.whl|
|exchangelib-5.5.0-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|olefile-0.47-py2.py3-none-any.whl|
|tzlocal-5.2-py3-none-any.whl|
|ntlm_auth-1.5.0-py2.py3-none-any.whl|
|compressed_rtf-1.0.6.tar.gz|
|RTFDE-0.1.2-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|colorclass-2.2.2-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|proto_plus-1.26.0-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|TIPCommon-2.2.16-py2.py3-none-any.whl|
|lark-1.1.9-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|httpcore-1.0.7-py3-none-any.whl|
|pyspnego-0.11.1-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Add Domains to Exchange-Siemplify Inbox Rules
Action will get as a parameter a list of Domains, and will be able to create or update a rule, filtering the domains from your mailboxes. Actions can be modified in the parameters using rule parameter. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Specify the Domains you would like to add to the rule, in a comma separated list.|False|String||
|Rule to add Domains to|Specify the rule to add the Domains to. If the rule doesn't exist - action will create it where it's missing.|True|List|Siemplify - Domains List - Move To Junk|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Block Sender by Message ID
Action will get as a parameter a list of message IDs, and will be able to mark it as junk. Marking an item as junk using this action will add the item sender's mail address to the "Blocked Senders List", and will also move it to the "Junk" folder. NOTICE - to mark emails in all mailboxes, please configure impersonation permissions: https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed. NOTE: Action is supported only from Exchange Server version 2013 and newer, if a lower version is used, action will fail with the appropriate message.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Move item to Junk folder?|Should the action move the specified messages to the junk folder|False|Boolean|true|
|Message IDs|Filter condition, specify emails with which message ids to find. Should accept comma separated list of message ids to mark as junk. If message id is provided, subject, sender and recipient filters are ignored.|False|String||
|Mailboxes list to perform on|Filter condition, If you have a specific list of mailboxes you would like to conduct the operation on, for better timing, please provide them here. Should accept a comma separated list of mail addresses, to mark the messages as junk in. If a mailboxes list is provided, "Perform Action in all Mailboxes" parameter will be ignored.|False|String||
|Folder Name|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Subject Filter|Filter condition, specify subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Mark All Matching Emails|Filter condition, specify if action should Mark all matched by criteria emails from the mailbox or Mark only first match.|False|Boolean|false|
|Perform action in all mailboxes|If checked, move to junk and block sender emails in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails.|False|String||



#### Download Attachments
Download email attachments from email to specific file path on Siemplify server. NOTICE - to search for an email in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed. Additionally, please note that if the downloaded attachments have "/" or "\" characters in the names, those will be replaced with the '_' character.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Download Path|File path on the server where to download the email attachments|True|String||
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated multiple message ids. If message id is provided, subject filter is ignored|False|String||
|Subject Filter|Filter condition to search emails by specific subject|False|String||
|Sender Filter|Filter condition to search emails by specific sender|False|String||
|Only Unread|If checked, download attachments only from unread emails|False|Boolean|false|
|Download Attachments from EML|If checked, download attachments also from attached EML files|False|Boolean|false|
|Download Attachments to unique path?|If checked, download attachments to unique path  under file path provided in “Download Path” parameter to avoid previously downloaded attachments overwrite.|False|Boolean|false|
|Search in all mailboxes|If checked, search in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Search in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Mailboxes|Specify a comma-separated list of mailboxes that need to be searched. This parameter has priority over "Search in all mailboxes".|False|String||



#### Get Mail EML File
Fetch message EML file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Folder to fetch from. Default is Inbox. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Message ID|Message ID|True|String||
|Base64 Encode|Base64 Encode|False|Boolean|true|



#### List Exchange-Siemplify Inbox Rules
Action will get as a parameter a rule name, from the Exchange-Siemplify Inbox rules, and will list it. If no mailboxes to list for will be provided, the rules for the logged in user will be listed. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Name To List|Specify the Rule name you would like to list from the relevant mailboxes|True|List||
|Mailboxes list to perform on|Filter condition, If you have a specific list of mailboxes you would like to conduct the operation on, for better timing, please provide them here. Should accept a comma separated list of mail addresses to list the rules from. If a mailboxes list is provided, "Perform Action in all Mailboxes" parameter will be ignored.|False|String||
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Add Senders to Exchange-Siemplify Inbox Rule
Action will get as a parameter a list of Email Addresses, or will work on User entities with Email regexes (if parameters are not provided), and will be able to create a new rule, filtering the senders from your mailboxes. Actions can be modified in the parameters using the rule parameter. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Senders|Specify the Senders you would like to add to the rule, in a comma separated list. If no parameter will be provided, action will work with User entities.|False|String||
|Rule to add senders to|Specify the rule to add the sender to. If the rule doesn't exist - action will create it where it's missing.|True|List|Siemplify - Senders List - Move To Junk|
|Should add senders' domain to the corresponding Domains List rule as well?|Specify whether the action should automatically take the domains of the provided email addresses and add them as well to the corresponding domain rules (same rule action for domains)|False|Boolean|false|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Delete Exchange-Siemplify Inbox Rules
Action will get as a parameter a rule name and will delete it from all the specified mailboxes. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Name To Delete|Specify the Rule name you would like to completely delete from the relevant mailboxes|True|List||
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Search Mails
Search for specific emails in configured mailbox using multiple provided search criteria. Action return information on found in mailbox emails in JSON format. NOTICE - to search for an email in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Message IDs|Specify a comma-separated list of message ids that need to be searched. Note: this filter has priority over the other ones.|False|String||
|Subject Filter|Filter condition, specify what subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails|False|String||
|Only Unread|Filter condition, specify if search should look only for unread emails|False|Boolean|false|
|Max Emails To Return|Return max X emails as an action result|False|String|100|
|Search in all mailboxes|If checked, search in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Search in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Mailboxes|Specify a comma-separated list of mailboxes that need to be searched. This parameter has priority over "Search in all mailboxes".|False|String||
|Start Time|Specify the start time for the email search. Format: ISO 8601. This parameter has a priority over "Time Frame (minutes)".|False|String||
|End Time|Specify the end time for the email search. Format: ISO 8601. If nothing is provided and "Start Time" is valid then this parameter will use current time.|False|String||
|Body Regex Filter|Specify a regex pattern that needs to be searched in body part of the email.|False|String||



#### Send Email And Wait
Send email and wait action, Send to field is comma separated. Note: Sender's display name can be configured in the client under the account settings
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The subject of the email|True|String||
|Send to|Recipient email address. Multiple addresses can be separated by commas|True|String|user@domain.com|
|CC|CC email address. Multiple addresses can be separated by commas|False|String|user@domain.com|
|BCC|bcc email address. Multiple addresses can be separated by commas|False|String||
|Mail content|Email body|True|EmailContent||
|Fetch Response Attachments|Allows attachment of files from response mail.|False|Boolean||
|Folder to Check for Reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|



#### Send Mail
Send Email from specific mailbox to an arbitrary list of recipients. Action can be used to inform users about specific alerts created in the Siemplify or inform about the results of processing of specific alerts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The mail subject part|True|String||
|Send to|Arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|String||
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the "Send to" field|False|String||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the "Send to" field|False|String||
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email. For example: C:\<Siemplify work dir>\file1.pdf, C:\<Siemplify work dir>\image2.jpg|False|String||
|Mail content|The email body part|True|EmailContent||
|Reply-To Recipients|Specify a comma-separated list of recipients that will be used in the "Reply-To" header. Note: The Reply-To header is added when the originator of the message wants any replies to the message to go to that particular email address rather than the one in the "From:" address.|False|String||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to either encrypt or sign the email. Note: for signing you need to also provide "Base64 Encoded Signature". For encryption, only this parameter needs to have a value.|False|Password|*****|
|Base64 Encoded Signature|Specify a base64 encoded signature that will be used to sign the email. Note: "Base64 Encoded Certificate" needs to be provided as well for signature to work and contain the signing certificate.|False|Password|*****|



#### Send Thread Reply
Send a message as a reply to the email thread.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message ID|Specify the ID of the message to which you want to send a reply.|True|String||
|Folder Name|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Content|Specify the content of the reply.|True|EmailContent||
|Attachments Paths|Specify a comma separated list of attachments file paths stored on the server for addition to the email.|False|String||
|Reply All|If enabled, action will send a reply to all recipients related to the original email. Note: this parameter has priority over “Reply To“ parameter.|False|Boolean|true|
|Reply To|Specify a comma-separated list of emails to which you want to send this reply. If nothing is provided and “Reply All“ is disabled, action will only send a reply to the sender of the email. If “Reply All“ is enabled, action will ignore this parameter.|False|String||



#### Send Vote Mail
Send emails with easy answering options, to allow stakeholders to be combined in the automated processes without accessing the Siemplify UI.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The mail subject part|True|String||
|Send To|Arbitrary comma separated list of email addresses for the email recipients. For example: user1@company.co, user2@company.co|True|String||
|CC|Arbitrary comma separated list of email addresses to be put in the CC field of email. Format is the same as for the "Send to" field|False|String||
|BCC|Arbitrary comma separated list of email addresses to be put in the BCC field of email. Format is the same as for the "Send to" field|False|String||
|Attachments Paths|Comma separated list of attachments file paths stored on the server for addition to the email. For example: C:\<Siemplify work dir>\file1.pdf, C:\<Siemplify work dir>\image2.jpg|False|String||
|Question or Decision Description|The question you would like to ask, or describe the decision you would like the recipient to be able to respond to|True|EmailContent||
|Structure of voting options|Choose the structure of the vote to be sent to the recipients|True|List|Yes/No|



#### Unblock Sender by Message ID
Action will get as a parameter a list of message IDs, and will be able to unmark it as junk. Unmarking an item as junk using this action will remove the item sender's mail address from the "Blocked Senders List". To move it back to the inbox, please tick the appropriate checkbox in the action parameters. NOTICE - to unmark emails in all mailboxes, please configure impersonation permissions: https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed. NOTE: Action is supported only from Exchange Server version 2013 and newer, if a lower version is used, action will fail with the appropriate message.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Move items back to Inbox?|Should the action move the specified messages back to the inbox folder|False|Boolean|true|
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated list of message ids to unmark as junk. If message id is provided, subject, sender and recipient filters are ignored.|False|String||
|Mailboxes list to perform on|Filter condition, If you have a specific list of mailboxes you would like to conduct the operation on, for better timing, please provide them here. Should accept a comma separated list of mail addresses to unmark the messages as junk in. If a mailboxes list is provided, "Perform Action in all Mailboxes" parameter will be ignored.|False|String||
|Folder Name|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Junk Email|
|Subject Filter|Filter condition, specify subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Unmark All Matching Emails|Filter condition, specify if action should Unmark all matched by criteria emails from the mailbox or Unmark only first match.|False|Boolean|false|
|Perform action in all mailboxes|If checked, move to junk and block sender emails in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action  in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails.|False|String||



#### Wait for Vote Mail Results
Use this action to fetch the responses of a vote mail sent by the "Send Vote Mail" action, in order to wait for the responses and get them inside Siemplify.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Vote Mail message_id|Message_id of the vote email, which current action would be waiting for. If message has been sent using Send Vote Mail action, please select SendVoteMail.JSONResult|message_id field as a placeholder.|True|String||
|Mail Recipients|Comma-separated list of recipient emails, response from which current action would be waiting for. Please select SendVoteMail.JSONResult|to_recipients field as a placeholder.|True|String||
|Folder to Check for Reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Folder to check for Sent Mail|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the sent mail in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.|True|String|Sent Items|
|How long to wait for recipient reply (minutes)|How long in minutes to wait for the user's reply before marking it timed out.|True|String|1440|
|Wait for All Recipients to Reply?|Parameter can be used to define if there are multiple recipients - should the Action wait for responses from all of recipients until timeout, or Action should wait for first reply to proceed.|False|Boolean|true|



#### Get Account Out Of Facility Settings
Get account out of facility (OOF) settings for the provided Siemplify User entity. Note 1: If the target User entity is a username, not a mail address, please run Enrich Entities from Active Directory integration first to try to use the information about User's mail stored in Active Directory. Note 2: For integration to return the information, it should have delegation or impersonation permissions to the target account mailbox. Link to impersonation permission configuration: https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange
Timeout - 600 Seconds



#### Move Mail To Folder
Move one or multiple emails from source email folder to another folder in mailbox. NOTICE - to search and move emails in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Source Folder Name|Source folder to move emails from. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String||
|Destination Folder Name|Destination folder to move emails to. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String||
|Source Mailbox|Specify the source mailbox to move the email from. Parameter accepts multiple values as a comma-separated string. If multiple values are provided, matching emails are copied from every accessible specified mailbox|False|String||
|Destination Mailbox|Specify the destination mailbox to move the matching emails to|False|String||
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated multiple message ids. If message id is provided, subject filter is ignored|False|String||
|Subject Filter|Filter condition, specify what subject to search for emails|False|String||
|Only Unread|Filter condition, specify if search should look only for unread emails|False|Boolean|false|
|Move in all mailboxes|If checked, search and move emails in all mailboxes accessible with current impersonalization settings. If the source or destination mailbox is specified, this parameter is ignored. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Move in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails|False|String||
|Limit the Amount of Information Returned in the JSON Result|If enabled, the amount of information returned by the action will be limited only to the key email fields.|False|Boolean|true|
|Disable the Action JSON Result|If enabled, action will not return JSON result.|False|Boolean|false|



#### Ping
Test connectivity to Microsoft Exchange instance with parameters provided at the integration configuration page on Marketplace tab.
Timeout - 600 Seconds



#### Remove Domains from Exchange-Siemplify Inbox Rules
Action will get as a parameter a list of Domains, and will be able to remove the provided domains from the existing rules. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Domains|Specify the Domains you would like to remove from the rule, in a comma separated list.|False|String||
|Rule to remove Domains from|Specify the rule to remove the Domains from. If the rule doesn’t exist - action will do nothing.|True|List|Siemplify - Domains List - Move To Junk|
|Remove Domains from all available Rules|Specify whether action should look for the provided domains in all of Siemplify inbox rules.|False|Boolean|false|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Save Mail Attachments To The Case
Save email attachments from email stored in monitored mailbox to the Case Wall.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Message ID|Message id to find an email to download attachments from.|True|String||
|Attachment To Save|If parameter is not specified - save all email attachments to the case wall. If parameter specified - save only matching attachment to the case wall.|False|String||



#### Delete Mail
Delete one or multiple email from the mailbox that matches search criterias. Delete can be done for the first email that matched the search criteria, or it can be done for all matching emails. NOTICE - to delete emails in all mailboxes, please configure impersonation permissions. https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Message IDs|Filter condition, specify emails with which email ids to find. Should accept comma separated list of message ids to search for. If message id is provided, subject, sender and recipient filters are ignored.|False|String||
|Mailboxes|Specify a comma-separated list of mailboxes that need to be searched. This parameter has priority over “Delete in all mailboxes“.|False|String||
|Subject Filter|Filter condition, specify subject to search for emails|False|String||
|Sender Filter|Filter condition, specify who should be the sender of needed emails|False|String||
|Recipient Filter|Filter condition, specify who should be the recipient of needed emails|False|String||
|Delete All Matching Emails|Filter condition, specify if action should delete all matched by criteria emails from the mailbox or delete only first match.|False|Boolean|false|
|Delete from all mailboxes|If checked, delete emails in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Delete from all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|25|
|Time Frame (minutes)|Filter condition, specify in what time frame in minutes should action look for emails|False|String||



#### Send Mail HTML
Send an email with HTML template content, Send to field is comma separated. Note: Sender's display name can be configured in the client under the account settings
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Subject|The subject of the email|True|String||
|Send to|Recipient email address. Multiple addresses can be separated by commas|True|String||
|CC|CC email address. Multiple addresses can be separated by commas|False|String||
|BCC|BCC email address. Multiple addresses can be separated by commas|False|String||
|Attachments Paths|Full path to attachments to be uploaded. Comma sepreated. e.g. C:\Desktop\x.txt,C:\Desktop\sample.txt|False|String||
|Mail content|Mail body|True|EmailContent||



#### Wait for mail from user
Wait for user's response based on an email sent via Send Email action. Note: please adjust the async timeout for action (polling timeout) and global action timeout in Siemplify server configuration as needed. Action input parameter "How long to wait for recipient reply (minutes)" cant be bigger than Siemplify server global timeout value.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Mail message_id|Message_id of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult|message_id field as a placeholder.|True|String||
|Mail Date|Send timestamp of the email, which current action would be waiting for. If message has been sent using Send Email action, please select SendEmail.JSONResult|email_date field as a placeholder.|True|String||
|Mail Recipients|Comma-separated list of recipient emails, response from which current action would be waiting for. If message has been sent using Send Email action, please select Select SendEmail.JSONResult|to_recipients field as a placeholder.|True|String||
|How long to wait for recipient reply (minutes)|How long in minutes to wait for the user's reply before marking it timed out.|True|String|1440|
|Wait for All Recipients to Reply?|Parameter can be used to define if there are multiple recipients - should the Action wait for responses from all of recipients until timeout, or Action should wait for first reply to proceed.|False|Boolean|true|
|Wait Stage Exclude pattern|Regular expression to exclude specific replies from the wait stage. Works with body part of email. Example is, to exclude automatic Out-Of-Office emails to be considered as recipient reply, and instead wait for actual user reply.|False|String||
|Folder to Check for Reply|Parameter can be used to specify mailbox email folder (mailbox that was used to send the email with question) to search for the user reply in this folder. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Fetch Response Attachments|If selected, if recipient replies with attachment - fetch recipient response and add it as attachment for the action result|False|Boolean|false|



#### Extract EML Data
Extract data from email's EML attachments.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Folder Name|Folder to fetch from. Default is Inbox. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|False|String|Inbox|
|Message ID|e.g. <1701cf01ba314032b2f1df43262a7723@gmail.com>|True|String||
|Regex Map JSON|e.g. {ips: \b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\b}|False|String||



#### Get Authorization
For integration configuration with Oauth authentication, run the action and browse to the received URL to get a link with access code. That link needs to be provided to the Generate Token action next to get the refresh token.
Timeout - 600 Seconds



#### Remove Senders from Exchange-Siemplify Inbox Rules
Action will get as a parameter a list of Senders, or will work on User entities (if parameters are not provided), and will be able to remove the provided Senders from the existing rules. WARNING: Action will modify your current users inbox rules, using EWS. NOTICE - to perform operation, please configure EDiscovery Group and Author permissions. For full details, please visit: https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchang. NOTE: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Senders|Specify the Senders you would like to remove from the rule, in a comma separated list. If no parameter will be provided, action will work with entities.|False|String||
|Rule to remove Senders from|Specify the rule to remove the Senders from. If the rule doesn't exist - action will do nothing.|True|List|Siemplify - Senders List - Move To Junk|
|Remove Senders from all available Rules|Specify whether action should look for the provided Senders in all of Siemplify inbox rules.|False|Boolean|false|
|Should remove senders' domains from the corresponding Domains List rule as well?|Specify whether the action should automatically take the domains of the provided email addresses and remove them as well from the corresponding domain rules (same rule action for domains)|False|Boolean|false|
|Perform action in all mailboxes|If checked, action will be performed in all mailboxes accessible with current impersonalization settings. If delegated access is used, implicitly specify the mailboxes to search in the "Mailboxes" parameter.|False|Boolean|false|
|How many mailboxes to process in a single batch|In case "Perform action in all mailboxes" is checked, action works in batches, this parameter controls how many mailboxes action should process in single batch (single connection to mail server).|False|String|50|



#### Generate Token
For integration configuration with Oauth authentication, get a refresh token using the authorization URL received in the Get Authorization action.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Authorization URL|Use the authorization URL received in the Get Authorization URL action to request a refresh token.|True|String||






## Jobs

#### Oauth Token Expiry Notification Job
Note that the job is deprecated and will be removed in the next 6 months. Oauth Token Expiry Notification Job is recommended to use if integration is working with Oauth refresh tokens. Refresh tokens are valid only for 90 days, after that User will need to create a new refresh token to use in the integration. This job will send reminder emails to the configured recipient list when the token will expire in 10, 5 and 1 day. Once a new token is set in this job, the notification timer will start over.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Mail Server Address|True|String|outlook.office365.com|
|Mail Address for sending notifications|True|String||
|Notifications Recipients List|True|String||
|Client ID|True|String||
|Client Secret|False|Password|*****|
|Tenant (Directory) ID|True|String||
|Refresh Token|True|Password|*****|

#### Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Integration Environments|False|String||
|Connector Names|False|String||



## Connectors
#### Exchange EML Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server IP|Server IP|True|IP|x.x.x.x|
|Domain|Specify the domain value to use for authentication.|True|String||
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|True|String||
|Password|Password|True|Password|*****|
|Mail Address|Mail Address|True|Email||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|Boolean|True|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|Boolean|false|
|Folder Name|The field name used to determine the folder name. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Environment Field Name|Environment Field Name|False|String||
|Environment Regex Pattern|Environment Regex Pattern|False|String||
|Unread Emails Only|Unread Emails Only|False|Boolean|false|
|Mark Emails as Read|Mark Emails as Read|False|Boolean|false|
|Max Days Backwards|Number of days before the first connector iteration to retrieve EML attachments from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Int|1|
|Encode Data as UTF-8|Indicates whether to encode the email data with UTF-8 or not. Setting to True is recommended.|False|Boolean|true|
|Attach EML or MSG File to the Case Wall|If checked, the forwarded EML or MSG file will be attached to the Case Wall.|False|Boolean||
|Exclusion Body Regex|Exclude those emails, whose body matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|Boolean|false|
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|String||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|Boolean|false|


#### Exchange Mail Connector v2
Exchange Mail Connector v2

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|String||
|Headers to add to events|Specify what headers from emails should be added to the events. Parameter accepts multiple values as a comma separated string. Provided values can be exact match or set as a regex.|False|String||
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|String||
|Mail Server Address|Mail server IP address to connect to. If connecting to O365, server address should be set to outlook.office365.com|True|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Mail Address|Mail address to use in integration, to use for sending out emails and work with received emails for this email (mailbox)|True|String||
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|Boolean|false|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|Boolean|false|
|Domain|Specify the domain value to use for authentication.|True|String||
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|True|String||
|Password|A password to authenticate with on mail server|True|Password|*****|
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|Boolean|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read|False|Boolean|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file|False|Boolean|false|
|Offset Time In Days|Number of days before the first connector iteration to retrieve emails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Int|5|
|Fetch Backwards Time Interval (minutes)|Time interval connector should use to fetch events from max hours backwards or connector last run timestamp. This parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Its recommended to adjust this value accordingly to the environment, for example 60 minutes or less.|False|Int|0|
|Max Emails Per Cycle|Fetch x emails per connector cycle|True|Int|10|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|Boolean|false|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|Boolean|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String|orig|
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String|attach|
|Create a Separate Siemplify Alert per Attached Mail File?|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Email Padding Period (minutes)|Specify an optional time period in minutes connector should fetch emails for prior to the latest timestamp.|False|Int|0|
|URL Regex|The regex connector uses to parse URLs from the processed emails.|True|String|(?i)\[?(?:(?:(?:http|https)(?:://))|www\.(?!://))(?:[a-zA-Z0-9\-\._~:;/\?#\[\]@!\$&'\(\)\*\+,=%])+|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|Password|*****|
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|String||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|Boolean|false|


##### Allowlist
| |
|-|
||
||


#### Exchange Mail Connector v2 with Oauth Authentication
Connector can be used to monitor specific mailboxes on Office 365 mail servers that require Oauth authentication. Get Authorization and Generate Token actions can be used to obtain refresh token that should be set in the connector. Note: Make sure to configure the integration first for the Oauth authentication.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|String||
|Headers to add to events|Specify what headers from emails should be added to the events. Parameter accepts multiple values as a comma separated string. Provided values can be exact match or set as a regex.|False|String||
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False|String||
|Mail Server Address|Mail server IP address to connect to. If connecting to O365, server address should be set to outlook.office365.com|True|String|outlook.office365.com|
|Mail Address|Mail address to use for connector.|True|String||
|Client ID|For Office 365 Oauth authentication, Client (Application) ID of Azure Active Directory App that will be used for the integration.|True|String||
|Client Secret|For Office 365 Oauth authentication, secret can be provided for the auth flow.|False|Password|*****|
|Tenant (Directory) ID|For Office 365 Oauth authentication, Azure Tenant (Directory) ID.|True|String||
|Refresh Token|For Office 365 Oauth authentication, refresh token that was obtained from running “Get Authorization” and “Generate Token” actions.|True|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|Boolean|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read|False|Boolean|false|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|Boolean|false|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file|False|Boolean|false|
|Offset Time In Days|Number of days before the first connector iteration to retrieve mails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Int|5|
|Fetch Backwards Time Interval (minutes)|Time interval connector should use to fetch events from max hours backwards or connector last run timestamp. This parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Its recommended to adjust this value accordingly to the environment, for example 60 minutes or less.|False|Int|0|
|Max Emails Per Cycle|Fetch x emails per connector cycle|True|Int|10|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|Boolean|false|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|Boolean|false|
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|String|orig|
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|String|attach|
|Create a Separate Siemplify Alert per Attached Mail File?|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|Boolean|false|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False|String||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Email Padding Period (minutes)|Specify an optional time period in minutes connector should fetch emails for prior to the latest timestamp.|False|Int|0|
|URL Regex|The regex connector uses to parse URLs from the processed emails.|True|String|(?i)\[?(?:(?:(?:http|https)(?:://))|www\.(?!://))(?:[a-zA-Z0-9\-\._~:;/\?#\[\]@!\$&'\(\)\*\+,=%])+|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False|Password|*****|
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False|Password|*****|
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|String||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|Boolean|false|


##### Allowlist
| |
|-|
||
||


#### Exchange Mail Connector
Exchange Mail Connector

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Server Ip|x.x.x.x|True|IP||
|Domain|Specify the domain value to use for authentication.|True|String||
|Username|Specify Username to authenticate with on mail server. Username can be provided without the domain part or in either UPN (user@fully_qualified_DNS_domain_name) or Down-Level Logon Name (domain\username) format.|False|String||
|Password|Password|True|Password|*****|
|Mail Address|Mail address to pull emails from. e.g. user@domain.com|True|String||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|Boolean|false|
|Use Domain For Authentication|If enabled, value provided for domain parameter will be concatenated to authenticate on the mail server as username@domain. If “Username” is specified in the username@domain or domain\username formats, this parameter is ignored and values from “Domain” and “Username” parameters are not concatenated.|False|Boolean|True|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|Boolean|false|
|Unread Emails Only|If checked, pull only unread mails|False|Boolean|True|
|Mark Emails as Read|If checked, mark mails as read after pulling them|False|Boolean|False|
|Attach Original EML|If checked, attach the original message as eml file.|False|Boolean|false|
|Folder Name|The field name used to determine the folder name. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|String|Inbox|
|Environment Field Name|If defined - connector will extract the environment from the specified event field. You can manipulate the field data using the Regex pattern field to extract specific string. In case the the extracted environment field and Siemplify environment name are not equal - you can map them in the map.json that is auto-generated on the first run, inside the <run-folder>.<run-folder> = C:\Siemplify_Server\Scripting\SiemplifyConnectorExecution<Connector_Folder>|False|Int||
|Environment Regex Pattern|If defined - the connector will implement the specific RegEx pattern on the data from "envirnment field" to extract specific string. For example - extract domain from sender's address: "(?<=@)(\S+$)"|False|Int||
|Max Days Backwards|Number of days before the first connector iteration to retrieve mails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. e.g. 3|True|String|5|
|Exclusion Subject Regex|Exclude those emails, whose subject matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Exclusion Body Regex|Exclude those emails, whose body matches this regex. For example '([N|n]ewsletter)|([O|o]ut of office)' finds all emails containing 'Newsletter' or 'Out of office' keywords.|False|String||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|
|Event Fields to Exclude|Comma-separated list of fields to exclude from events. Example: field1,field2|False|String||
|Exclude Attachments|If enabled, connector will not ingest email attachments and add them to cases.|False|Boolean|false|





Read123!@#
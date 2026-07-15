
# Mimecast

Mimecast cloud cybersecurity services for email, data, and web provides your organization with archiving and continuity needed to prevent compromise.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Mimecast instance.|True|String|https:/{{api root}}|
|Application ID|Application ID of the Mimecast instance. You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|String||
|Application Key|Application Key of the Mimecast instance. You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|Password|*****|
|Access Key|Access Key of the Mimecast instance. You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|Password|*****|
|Secret Key|Secret Key of the Mimecast instance. You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|Password|*****|
|Client ID|Client ID of the Mimecast instance. You need to provide "Client ID" and "Client Secret" for the authentication to work.|False|String||
|Client Secret|Client Secret of the Mimecast instance. You need to provide "Client ID" and "Client Secret" for the authentication to work.|False|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Mimecast server is valid.|False|Boolean|True|


#### Dependencies
| |
|-|
|proto_plus-1.25.0-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|cryptography-43.0.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|pyOpenSSL-24.2.1-py3-none-any.whl|
|anyio-4.6.2.post1-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|TIPCommon-2.2.0-py2.py3-none-any.whl|
|google_auth-2.36.0-py2.py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|googleapis_common_protos-1.66.0-py2.py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|httpcore-1.0.6-py3-none-any.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|google_api_core-2.23.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|google_api_python_client-2.152.0-py2.py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|


## Actions
#### Release Message
Release message in Mimecast. Note: only messages with status "Held" can be released.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message ID|Specify the ID of the message that needs to be released.|True|String||
|Release To Sandbox|If enabled, action will release the message to the sandbox.|False|Boolean|false|



#### Reject Message
Reject message in Mimecast. Note: only messages with status "Held" can be rejected.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message ID|Specify the ID of the message that needs to be rejected.|True|String||
|Note|Specify an additional note containing an explanation regarding why the message was rejected.|False|String||
|Reason|Specify the reason for rejection.|False|List|Select One|
|Notify Sender|If enabled, action will notify the sender about rejection.|False|Boolean|false|



#### Simple Archive Search
Search archive emails using defined parameters in Mimecast. Note: when providing time make sure to take in the account timezones. For ease of use, Siemplify instance and Mimecast instance should be in the same timezone.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Fields To Return|Specify a comma-separated list of fields that needs to be returned.|True|String||
|Mailboxes|Specify a comma-separated list of mailboxes that need to be searched.|False|String||
|From|Specify a comma-separated list of email addresses from which the emails were sent.|False|String||
|To|Specify a comma-separated list of email addresses to which the emails were sent.|False|String||
|Subject|Specify a subject that needs to be searched.|False|String||
|Time Frame|Specify a time frame for the search. If "Custom" is selected, you also need to provide "Start Time".|True|List|Last Hour|
|Start Time|Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601|False|String||
|End Time|Specify the end time for the search. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.|False|String||
|Max Emails To Return|Specify how many emails to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"size": 6648, "attachmentcount": 3, "subject": "test2", "displayfrom": "spam@mimecast.org", "id": "eNolj0tvgzAQhP-LzyDtGmNDOKUPklZNKzX0lQsytklpeLTY0EPV_16n7OHTajSa2f0h1qhpNI0mK5J_MPxxxx-1vt3Y5PUBC12h3BcXb3aQu8O1klBc7eqU5e7mJe9bd7e1JCCdsVYeTTsMp-nTDSfT-1ysOMYxVLEBJYyhCYKQUZJiyjjTtRYJF4LXkDljHc36qW0zChT9HQgRpXCeRf6H7ynICgIym9E2g6_AgMhRvTfz8sixVKEpJwtYIvJy1p4hLS-f9mtEsY4Elks-nBdvdGbskIUAcRgjMpZQQX7_APnsVEU", "smash": "1b61550b5e0c7ee28107a38919464dfd78677xxx", "displayto": "spam@mimecast.org", "receiveddate": "2021-06-21T07:22:00+0000", "status": "ARCHIVED"}, {"size": 6662, "attachmentcount": 3, "subject": "test2", "displayfrom": "phishing@mimecast.org", "id": "eNolT2FLwzAU_C_5mhbfy5K0XT_VgUOc2OlEGUJo07SWda0mbVHE_25mH9xxHMcd74c4oydr2oqsSUlb2ELTiE-9l_Z12ApK60dR39GX_Pp7t8tLw6joK7y9b8rD0cHX0e7R3rxd5dnDJo8oCcjZOFc0phuG0_QxDifT-2JZaV6wRBQriKWUItY1alGYmFclAx7XEiKNSZSOxo0s7aeuSxkwBOmBnMHlFvuf_M6BrCEgs7GuHfwEBqSw-r2dl08apUOjJgeoEKWaK88hU5vnpwwxylYRqqUfLsIHR2PPyEMAGQpvJ4Jz8vsHnMxxxx", "smash": "6dc4a295a30866658cf1c5ae84dbxxxx", "displayto": "phishing@mimecast.org", "receiveddate": "2021-06-21T05:42:00+0000", "status": "ARCHIVED"}]
```



#### Report Message
Deprecated. Report message in Mimecast. Note: only messages with status "Held", "Archived", "Bounced" can be reported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message ID|Specify the ID of the message that needs to be reported.|True|String||
|Comment|Specify the comment for the report.|False|String||
|Report As|Specify the report type for the message.|False|List|Spam|



#### Advanced Archive Search
Search archive emails using a custom XML query in Mimecast. Note: when providing time make sure to take in the account timezones. For ease of use, Siemplify instance and Mimecast instance should be in the same timezone.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|XML Query|Specify an XML query that should be used when searching for archive emails. Please visit documentation for more details.|True|String||



##### JSON Results
```json
[{"size": 6648, "attachmentcount": 3, "subject": "test2", "displayfrom": "spam@mimecast.org", "id": "eNolj0tvgzAQhP-LzyDtGmNDOKUPklZNKzX0lQsytklpeLTY0EPV_16n7OHTajSa2f0h1qhpNI0mK5J_MPxxxx-1vt3Y5PUBC12h3BcXb3aQu8O1klBc7eqU5e7mJe9bd7e1JCCdsVYeTTsMp-nTDSfT-1ysOMYxVLEBJYyhCYKQUZJiyjjTtRYJF4LXkDljHc36qW0zChT9HQgRpXCeRf6H7ynICgIym9E2g6_AgMhRvTfz8sixVKEpJwtYIvJy1p4hLS-f9mtEsY4Elks-nBdvdGbskIUAcRgjMpZQQX7_APnsVEU", "smash": "1b61550b5e0c7ee28107a38919464dfd78677xxx", "displayto": "spam@mimecast.org", "receiveddate": "2021-06-21T07:22:00+0000", "status": "ARCHIVED"}, {"size": 6662, "attachmentcount": 3, "subject": "test2", "displayfrom": "phishing@mimecast.org", "id": "eNolT2FLwzAU_C_5mhbfy5K0XT_VgUOc2OlEGUJo07SWda0mbVHE_25mH9xxHMcd74c4oydr2oqsSUlb2ELTiE-9l_Z12ApK60dR39GX_Pp7t8tLw6joK7y9b8rD0cHX0e7R3rxd5dnDJo8oCcjZOFc0phuG0_QxDifT-2JZaV6wRBQriKWUItY1alGYmFclAx7XEiKNSZSOxo0s7aeuSxkwBOmBnMHlFvuf_M6BrCEgs7GuHfwEBqSw-r2dl08apUOjJgeoEKWaK88hU5vnpwwxylYRqqUfLsIHR2PPyEMAGQpvJ4Jz8vsHnMxxxx", "smash": "6dc4a295a30866658cf1c5ae84dbxxxx", "displayto": "phishing@mimecast.org", "receiveddate": "2021-06-21T05:42:00+0000", "status": "ARCHIVED"}]
```



#### Block Sender
Block sender in Mimecast.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sender|Specify the email address of the sender to block.|True|String||
|Recipient|Specify the email address of the recipient to block.|True|String||



#### Permit Sender
Permit sender in Mimecast.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Sender|Specify the email address of the sender to permit.|True|String||
|Recipient|Specify the email address of the recipient to permit.|True|String||



#### Create Block Sender Policy
Create a Block Sender policy in Mimecast.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Enforced|If enabled, the policy is enforced.|False|Boolean|true|
|Response|Provide the type of response that will be associated with the created policy.|False|List|Block Sender|
|Description|Description for the policy.|True|String||
|Extracted Data|Define from where the information about sender and recipient should be extracted.|False|List|Both|
|Sender|From whom the message should be sent for it to be blocked. Only needed if “Sender Type” is one of: Email Domain, Email Address, Header Display Name. This parameter is ignored if a different  “From Type” value is selected.|False|String||
|Sender Type|Type of the sender for the policy.|False|List|Email Domain|
|Recipient|To whom the message should be sent for it to be blocked. Only needed if “Recipient Type” is one of: Email Domain, Email Address, Header Display Name. This parameter is ignored if a different  “Recipient Type” value is selected.|False|String||
|Recipient Type|Type of the recipient for the policy.|False|List|Email Domain|
|Comment|Comment for a policy.|False|String||
|Bidirectional|If enabled, the policy will be defined in a bidirectional way.|False|Boolean|true|
|Start Time|Start time for the policy. If nothing is provided, start time will be set to eternal. Expects ISO 8601 format. Example: 2025-03-07T16:03:00Z|False|String||
|End Time|End time for the policy. If nothing is provided, end time will be set to eternal. Expects ISO 8601 format. Example: 2025-03-07T16:03:00Z|False|String||



##### JSON Results
```json
{"option": "block_sender", "id": "xxx-xxx-xxx-xxx", "policy": {"description": "g", "fromPart": "both", "from": {"type": "individual_email_address", "emailAddress": "exm@gmail.com"}, "to": {"type": "everyone"}, "fromType": "individual_email_address", "fromValue": "exm@gmail.com", "toType": "everyone", "toValue": null, "fromEternal": true, "toEternal": true, "fromDate": "1900-01-01T00:00:00+0000", "toDate": "2100-01-01T23:59:59+0000", "override": false, "bidirectional": true, "conditions": {}, "enabled": true, "enforced": true, "createTime": "2025-04-04T11:41:23+0000", "lastUpdated": "2025-04-04T11:41:23+0000"}}
```



#### Ping
Test connectivity to the Mimecast with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds









## Connectors
#### Mimecast - Message Tracking Connector
Pull information about messages from the "Message Tracking" tab in Mimecast. Note: whitelist works on the "queueDetailStatus/bounceType" parameter.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|API Root|API root of the Mimecast instance.|True|String|https:/{{api root}}|
|Application ID|Application ID of the Mimecast instance. You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|String||
|Application Key|Application Key of the Mimecast instance. You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|Password|*****|
|Access Key|Access Key of the Mimecast instance.  You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|Password|*****|
|Secret Key|Secret Key of the Mimecast instance.  You need to provide "Application ID", "Application Key", "Access Key" and "Secret Key" for the authentication to work.|False|Password|*****|
|Client ID|Client ID of the Mimecast instance. You need to provide "Client ID" and "Client Secret" for the authentication to work.|False|String||
|Client Secret|Client Secret of the Mimecast instance. You need to provide "Client ID" and "Client Secret" for the authentication to work.|False|Password|*****|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Mimecast server is valid.|False|Boolean|true|
|Domains|A comma-separated list of domains for which to query messages.|True|String||
|Lowest Risk To Fetch|Lowest risk that will be used to fetch messages. Possible values: Negligible, Low, Medium, High. If nothing is provided, the connector will ingest all messages.|False|String||
|Status Filter|A comma-separated list of status filters for the messages. Possible values: delivery, held, accepted, bounced, deferred, rejected, archived. If nothing is provided, the connector will ingest all messages.|False|String|held|
|Route Filter|A comma-separated route filters for the messages. Possible values: internal, outbound, inbound. If nothing is provided, the connector will ingest all messages.|False|String||
|Queue Reason Filter|A comma-separated list of queue reasons that should filter the messages. If nothing is provided, this filter is ignored.|False|String||
|Ingest Messages Without Risk|If enabled, the connector will ingest messages even if there is no info about risk. Siemplify Alerts generated from those messages will have priority set to Informational.|False|Boolean|true|
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve messages from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Default: 1 hour. Max: 30 days.|False|Int|1|
|Max Messages To Return|How many messages to process per one connector iteration. Default: 100.|False|Int|20|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password|*****|





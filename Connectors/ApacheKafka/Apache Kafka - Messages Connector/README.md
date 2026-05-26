# Apache Kafka - Messages Connector
The Apache Kafka Connector retrieves messages from Apache Kafka.


Integration: ApacheKafka

Integration Version: 2

Device Product Field: Product Name

Event Name Field: event_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Poll Timeout|Poll timeout to consume a message from Kafka, in seconds.|False|5|
|Case Name Template|A custom case name.
You can use placeholders in the format [field_name], for example: Phishing - [event_mailbox].
This parameter adds a custom_case_name key to the Google SecOps event.
The connector extracts placeholder values from the first Google SecOps event, and placeholders are only supported for fields that contain a string value.|False||
|Alert Name Template|A custom alert name.
You can use placeholders in the format [field_name], for example: Phishing - [event_mailbox].
The connector extracts placeholder values from the first Google SecOps event, and placeholders are only supported for fields that contain a string value.
If you do not provide a value or use an invalid template, the connector uses the fallback value "{Connector name} - Alert".|True|b|
|Rule Generator Template|A custom rule generator.
You can use placeholders in the format [field_name], for example: Phishing - [event_mailbox].
The connector extracts placeholder values from the first Google SecOps event, and placeholders are only supported for fields that contain a string value.
If you do not provide a value or use an invalid template, the connector uses the fallback value "{Connector name} - Rule Generator".|True|h|
|Timestamp Field|The name of the field that contains the Google SecOps alert timestamp.
If the timestamp is not in Unix epoch format, its format must be defined in the Timestamp Format parameter.|True|timestamp|
|Timestamp Format|The format of the message timestamp.
The connector requires this format to process messages correctly.
If the timestamp is not in Unix epoch format and a timestamp format is not configured, the connector will fail.|False|%Y-%m-%dT%H:%M:%S.%fZ|
|Severity Mapping JSON|The JSON object used by the connector to extract the severity level from the message.|True|{"Default": 60}|
|Unique ID Field|The name of the field that provides a unique message identifier. If a value is not set, the connector generates and uses a SHA-256 hash as the message identifier.|False||
|Disable Overflow|If enabled, the connector ignores the Google SecOps overflow mechanism when creating alerts.|False|true|
|Verify SSL|If enabled, the integration validates the SSL certificate for the Apache Kafka connection.|False|true|
|Proxy Server Address|The address of the proxy server.|False||
|Proxy Username|The username for proxy authentication.|False||
|Environment Field Name|The name of the field that stores the environment name.
If the field is not found, the system uses the default environment. |False||
|Environment Regex Pattern|A regular expression pattern that runs on the value from the Environment Field Name field to manipulate the result.
The default value, .*, retrieves the raw field value.
If the regular expression pattern is empty or the environment value is null, the system uses the default environment.|False|.*|
|Kafka Brokers|A comma-separated list of Kafka brokers to connect to, in the format `hostname:port`.|True|b|
|Use TLS for connection|If enabled, the integration uses TLS encryption for authentication. A CA certificate is mandatory for this connection.|False|false|
|Use SASL PLAIN with TLS for connection|If enabled, the integration uses the SASL PLAIN username and password mechanism for authentication. This option requires a SASL Username and Password to be provided. It is only supported with TLS encryption, which requires a CA certificate.|False|false|
|Proxy Password|The password for proxy authentication.|False|*****|
|CA certificate of Kafka server|The Certificate Authority (CA) certificate used to verify the identity of the Kafka server.|False|*****|
|Client certificate|The client's certificate for mutual TLS authentication with the Kafka server.|False|*****|
|Client certificate key|The private key that corresponds to the client's certificate, used for mutual TLS authentication.|False|*****|
|Client certificate key password|The password used to decrypt the client certificate's private key.|False|*****|
|SASL PLAIN Username|The username for SASL PLAIN authentication with Kafka brokers.|False||
|SASL PLAIN Password|The password for SASL PLAIN authentication with Kafka brokers.|False|*****|
|Topic|The Kafka topic from which incidents are retrieved.|True|b|
|Consumer group ID|The identifier of the consumer group used when retrieving incidents.|False||
|Partitions|A CSV list of partitions from which to fetch messages.|False||
|Initial Offset|The initial offset specifies where the connector starts fetching messages.
A positive integer fetches from that offset number.
 To start from the beginning or end of the partition, use the values 'earliest' or 'latest'.|False||
|Max Messages To Fetch|The maximum number of messages the connector processes per iteration.|True|100|


This is a Readme addonon
# 11Vectra RUX - Entities Connector
The connector retrieves entities and detections from the Vectra RUX platform. Each Vectra entity is mapped to an alert, and the detections associated with the entity are mapped as alert events. The alert grouping rule should be set with the Source Grouping Identifier to attach the updated alert to the same case, and the grouping limit should be set to the maximum possible value.


Integration: VectraRUX

Integration Version: 3

Device Product Field: Vectra RUX

Event Name Field: detection_type
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|API Root|The base URL of the API, used as the entry point for all API requests.|True|https://<address>:<port>|
|Client ID|A unique identifier assigned to each client to authenticate and authorize API requests.|True|12345|
|Client Secret|A confidential key associated with the client ID, used to authenticate and securely authorize API requests.|True|*****|
|Entity Type|Type of the Entity
(Account, Host)
|True|Host|
|Limit|Number of entities to fetch|False||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from for the first time. Default: 0|False|0|
|Prioritized|If it is set (present), only entities whose priority score is above
the configured priority threshold will be included in the
response|False|false|
|Specific Tag|A specific tag to filter results|False||


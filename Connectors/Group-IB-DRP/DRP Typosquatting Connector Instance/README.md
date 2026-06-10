# DRP Typosquatting Connector Instance



Integration: Group-IB-DRP

Integration Version: 1

Device Product Field: title

Event Name Field: id
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|API login| Email used for DRP portal login |True|your@email.com   |
|API key|API token from DRP profile   |True|*****|
|API URL|DRP URL|True|https://drp.group-ib.com/client_api/|
|Verify SSL|Verify the server's SSL certificate.|False|true|
|Case name|Default — label shown on cases  |True|Typosquatting Domain |
|Case type|type|True|Typosquatting    |
|Case severity|Options: Informative / Low / Medium / High / Critical |True|Medium|
|Start date|Blank = start from 1 day ago. Set YYYY-MM-DD only for a historical backfill |False|dummy_value|


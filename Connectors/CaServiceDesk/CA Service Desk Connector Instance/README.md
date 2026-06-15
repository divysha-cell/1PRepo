# CA Service Desk Connector Instance



Integration: CaServiceDesk

Integration Version: 27

Device Product Field: device_product

Event Name Field: description
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|API Root|e.g. http://x.x.x.x:8080|True|dummy_value|
|Username|Username|True|dummy_value|
|Password|Password|True|*****|
|Ticket ID Field|Incident id field key as it appear at the ticket JSON e.g. ref_num|True|ref_num|
|Groups List|Filter incidents by groups|False|dummy_value|
|Proxy Server Address|The address of the proxy server to use.|False|dummy_value|
|Start Time Field|Represent the key of the start time at the ticket. e.g. open_date|True|open_date|
|End Time Field|Represent the key of the end time at the ticket. e.g. last_mod_dt|True|last_mod_dt|
|Category Default Field|Represent the category key at the ticket. e.g. category|True|category|
|Category Fallback Field|e.g. category.sym|True|category.sym|
|User ID Field|Filter by user. e.g. customer.combo_name|True|customer.combo_name|
|Ticket Fields|Comma separated. e.g. customer.combo_name,category.sym,status.sym,priority.sym,active,log_agent.combo_name,assignee.combo_name,group.combo_name,affected_service.name,severity.sym,urgency.sym,impact.sym,problem.ref_num,resolution_code.sym,call_back_date,change.chg_ref_num,caused_by_chg.chg_ref_num,external_system_ticket,resolution_method.sym,symptom_code.sym,requested_by.combo_name,persistent_id,summary,description,open_date,last_mod_dt,resolve_date,close_date,ref_num|True|customer.combo_name,category.sym,status.sym,priority.sym,active,log_agent.combo_name,assignee.combo_name,group.combo_name,affected_service.name,severity.sym,urgency.sym,impact.sym,problem.ref_num,resolution_code.sym,call_back_date,change.chg_ref_num,caused_by_chg.chg_ref_num,external_system_ticket,resolution_method.sym,symptom_code.sym,requested_by.combo_name,persistent_id,summary,description,open_date,last_mod_dt,resolve_date,close_date,ref_num|
|List Of Users To Ignore|Comma separated. Filter incidents by users to ignore|False|dummy_value|
|Categories List|Filter incidents by categories|False|dummy_value|
|Proxy Username|The proxy username to authenticate with.|False|dummy_value|
|Proxy Password|The proxy password to authenticate with.|False|*****|


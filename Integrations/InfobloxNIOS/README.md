
# InfobloxNIOS

This integration enables Google SecOps to retrieve IP metadata from Infoblox Grid Manager and manage DNS Firewall protections through RPZs. It allows security teams to define RPZ rules that block DNS resolution for malicious or unauthorized domains, or redirect users to a walled garden by modifying DNS responses. In case of any queries, please reach out to support@infoblox.com.

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|The base URL of the API, used as the entry point for all API requests.|True|String||
|Username|The Infoblox account name used to authenticate API access.|True|String||
|Password|The corresponding password for the provided Infoblox username.|True|Password||
|Verify SSL|Verify SSL|False|Boolean||


#### Dependencies
| |
|-|
|cachetools-6.2.1-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|google_auth-2.42.1-py2.py3-none-any.whl|
|TIPCommon-2.2.11-py2.py3-none-any.whl|
|pyparsing-3.2.5-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|anyio-4.11.0-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|httplib2-0.31.0-py3-none-any.whl|
|certifi-2025.10.5-py3-none-any.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|requests-2.32.3-py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|protobuf-6.33.0-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|google_api_python_client-2.186.0-py3-none-any.whl|
|google_api_core-2.28.1-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.11-py3-none-any.whl|
|urllib3-2.5.0-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|google_auth_httplib2-0.2.1-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|googleapis_common_protos-1.71.0-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Create RPZ MX Rule
Adds a mail exchange override rule to an RPZ.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|Specify the name of the rule.|True|None||
|RP Zone|The zone to assign the rule to.|True|None||
|Mail Exchanger|Specify the mail exchanger for the rule.|True|None||
|Preference|Preference value for the rule.|True|None||
|Comment|Comment for this rule.|False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone.|False|None||



#### Create RPZ PTR Rule
Adds a reverse DNS lookup override in RPZ for an IP.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|PTR DName|The domain name of the RPZ substitute rule object of the PTR record.|True|None||
|RP Zone|The zone to assign the rule to.|True|None||
|Name|The name of the RPZ Substitute rule object of the PTR record.|False|None||
|Comment|Comment for this rule.|False|None||
|IPv4 Address|The IPv4 address of the substitute rule.|False|None||
|IPv6 Address|The IPv6 address of the substitute rule.|False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone.|False|None||



#### Create RPZ TXT Rule
Adds a TXT record rule in RPZ to associate text data with a DNS response. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|RP Zone|The zone to assign the rule to. |True|None||
|Name|Specify the name of the rule.|True|None||
|Text|Text associated with the record. |True|None||
|Comment|Comment for this rule. |False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone. |False|None||



#### Create RPZ CNAME Rule
Adds a CNAME rule to an existing RPZ to override DNS behavior. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Substitute Name|The substitute name to assign (substitute domain only). |False|None||
|Rule Type|The type of the rule to create.|True|None||
|Object Type|The type of the object for which to assign the rule.|True|None||
|Name|The rule name in a FQDN format.|True|None||
|RP Zone|The zone to assign the rule to.|True|None||
|Comment|Comment for this rule.|False|None||
|View|The DNS view in which the records are located. By default, the 'default' DNS view is searched.|False|None||
|Additional Parameters|JSON object containing additional parameters to create rpz rule.|False|None||



#### Create Response Policy Zone
Creates a new Response Policy Zone (RPZ) to define custom DNS responses.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|FQDN|The name of this DNS zone is in FQDN format.|True|None||
|Substitute Name|The alternative name of the redirect target is a substitute response policy zone.|False|None||
|Comment|Comment for the zone.|False|None||
|RPZ Policy|The override policy of the response policy zone. |False|None||
|RPZ Severity|The severity of the response policy zone.|False|None||
|RPZ Type|The type of the Response Policy Zone.|False|None||
|Fireeye Rule Mapping|Rules to map fireeye alerts.|False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone.|False|None||



#### Create RPZ A Rule
Creates an RPZ Substitute rule which maps domain name (A record) or an IPv4 address to a substitute IPv4 address for DNS redirection or blocking. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Object Type|The type of the object for which to create record.|True|None||
|Name|Specify the name of the rule.|True|None||
|RP Zone|The zone to assign the rule to.|True|None||
|IPv4 Address|The IPv4 address of the substitute rule.|True|None||
|Comment|Comment for this rule.|False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone.|False|None||



#### Create Host Record
Adds a host record to Infoblox with associated IP addresses. When configure_for_dns is enabled, it also creates corresponding A/AAAA and PTR DNS records. Useful for IPAM and DNS inventory management.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|The name of the host in FQDN format `{name}.{auth_zone}` (e.g. server1.auth.threat.zone). It must belong to an existing DNS zone.|True|None||
|IPv4 Addresses|Array of IPv4 address objects in the following format. (e.g. [{"ipv4addr":"192.168.1.100","mac":"00:11:22:33:44:55","configure_for_dhcp":true},...] ).|False|None||
|IPv6 Addresses|Array of IPv6 address objects in the following format. (e.g. [{"ipv6addr":"2001:db8::1"},{"ipv6addr":"2001:db8::2", etc.}])|False|None||
|View|The DNS view in which the record resides (e.g., "default").|False|None||
|Comment|Additional information or notes about this host record.|False|None||
|Aliases|Comma-separated list of DNS aliases (CNAMEs) for this host (e.g., "alias1.auth zone,alias2.auth zone").|False|None||
|Configure for DNS|When false, the host record doesn't have associated DNS records.|False|None||
|Extended Attributes|Comma-separated key/value formatted filter for extended attributes, e.g. "Site=New York,OtherProp=MyValue"|False|None||
|Additional Parameters|Comma-separated key/value formatted string for additional parameters supported by the API (e.g., "use_ttl=true,network_view=default").|False|None||



#### Create RPZ AAAA Rule
Creates an RPZ Substitute rule which maps domain name (AAAA record) or an IPv6 address to a substitute IPv6 address for DNS redirection or blocking. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Object Type|The type of the object for which to create record.|True|None||
|Name|Specify the name of the rule.|True|None||
|RP Zone|The zone to assign the rule to.|True|None||
|IPv6 Address|The IPv6 address of the substitute rule.|True|None||
|Comment|Comment for this rule.|False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone.|False|None||



#### Create RPZ NAPTR Rule
Adds a NAPTR override in RPZ to control DNS-based service discovery. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|Specify the name of the rule.|True|None||
|RP Zone|The zone to assign the rule to.|True|None||
|Order|Order parameter in NAPTR record defines the sequence of rule application when multiple rules exist.|True|None||
|Preference|The preference of the Substitute (NAPTR Record) Rule record.|True|None||
|Replacement|Substitute rule object `replacement` field of the NAPTR record. For non-terminal NAPTR records, this field specifies the next domain name to look up. |True|None||
|Comment|Comment for this rule.|False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone. |False|None||



#### Delete Response Policy Zone
Removes an existing Response Policy Zone from Infoblox.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference ID|The reference ID of the response policy zone.|True|None||



#### Delete RPZ Rule
Deletes a rule from a specified RPZ. Supports all RPZ record types by dynamically determining the object type from user input.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reference ID|The reference ID of the RPZ rule. |True|None||



#### DHCP Lease Lookup
Retrieves DHCP lease details for a MAC or IP address.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IP Address|Lease IP address (IPv4 or IPv6).|False|None||
|Hardware|MAC address for IPv4 leases. Regex or exact search supported.|False|None||
|Hostname|Hostname sent via DHCP option 12. Regex/exact search.|False|None||
|IPv6 DUID|IPv6 DUID identifier for IPv6 leases. Regex/exact search.|False|None||
|Protocol|One of: BOTH, IPV4, IPV6; exact match only.|False|None||
|Fingerprint|DHCP client fingerprint; case‑insensitive or regex search.|False|None||
|Username|User associated with lease request; case-insensitive/regex search.|False|None||
|Limit|Maximum numbers of objects to be returned.|False|None||



#### IP Lookup
Returns IPAM info for a given IP. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Limit|Maximum numbers of objects to be returned.|False|None||
|IP Address|The IP address for which to retrieve information, e.g. "192.168.1.1". Cannot be used in conjunction with network or from/to_ip arguments.|False|None||
|Network|The network that the IP belongs to is in FQDN/CIDR format, e.g. "192.168.1.0/24". Cannot be used in conjunction with ip or from/to_ip arguments.|False|None||
|From IP|The beginning of the IP range, e.g. "192.168.1.0". Must be used in conjunction with to_ip.|False|None||
|To IP|The end of the IP range, e.g. "192.168.1.254". Must be used in conjunction with from_ip.|False|None||
|Status|The status of the IP device. Used in conjunction with the network or ip argument. Possible values are All, Active, Used and Unused.|False|None||
|Extended Attributes|Comma-separated key/value formatted filter for extended attributes, e.g. "Site=New York,OtherProp=MyValue".|False|None||



#### Get Response Policy Zone Details
Retrieves configuration details for a specified RPZ.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|FQDN|The name of this DNS zone in FQDN format.|False|None||
|View|The name of the DNS view in which the zone resides ( e.g. “external”).|False|None||
|Comment|Comment for the zone.|False|None||
|Limit|Maximum number of objects to be returned.|False|None||



#### List Network Info
Lists defined IPv4/IPv6 networks and subnets in IPAM.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network|The network address in CIDR notation (e.g., "192.168.1.0/24") .|False|None||
|Limit|Maximum numbers of objects to be returned.|False|None||
|Extended Attributes|The comma-separated key/value formatted filter for extended attributes, e.g. "Site=New York,OtherProp=MyValue". |False|None||



#### Create RPZ SRV Rule
Adds an SRV record override in RPZ for service-based DNS lookups.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|Specify the name of the rule.|True|None||
|Priority|The priority of the Substitute (SRV Record) Rule.|True|None||
|RP Zone|The name of a response policy zone in which the record resides. |True|None||
|Port|The port of the Substitute (SRV Record) Rule.|True|None||
|Target|Text associated with the record.|True|None||
|Weight|The weight of the Substitute (SRV Record) Rule.|True|None||
|Comment|Comment for this rule.|False|None||
|Additional Parameters|JSON object containing additional parameters to create response policy zone.|False|None||



#### Update RPZ CNAME Rule
Updates an existing rule in RPZ CNAME to modify DNS behavior. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Substitute Name|The substitute name to assign (substitute domain only). |False|None||
|Reference ID|The reference ID of the existing RPZ rule to update.|True|None||
|Rule Type|The type of the rule to update.|True|None||
|Name|The rule name in a FQDN format.|True|None||
|RP Zone|The zone to assign the rule to.|True|None||
|Comment|Comment for this rule.|False|None||
|View|The DNS view in which the records are located. By default, the 'default' DNS view is searched.|False|None||
|Additional Parameters|JSON object containing additional parameters to create rpz rule.|False|None||



#### List Host Info
Retrieves host records from Infoblox including hostname, associated IPv4/IPv6 addresses (A/AAAA records), PTR records, DNS view information, and any configured extensible attributes.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|IPv4 Address|IPv4 address information.|False|None||
|Name|The hostname for the record. |False|None||
|IPv6 Address|IPv6 address information. |False|None||
|Extended Attributes|Comma-separated key/value formatted filter for extended attributes, e.g. "Site=New York,OtherProp=MyValue".|False|None||
|Limit|Maximum numbers of objects to be returned.|False|None||



#### Search RPZ Rule
Searches for a specific RPZ rule by its name.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Object Type|The Infoblox object type.|True|None||
|Rule Name|The full rule name (usually the rule name followed by its zone.(e.g. name.domain.com).|False|None||
|Output Fields|The comma-separated fields to include in the returned object (e.g., address, comment, etc.) .|False|None||
|Limit|Maximum number of objects to be returned. |False|None||



#### Ping
Use the Ping action to test the connectivity to API Service.
Timeout - 600 Seconds










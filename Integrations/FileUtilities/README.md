
# FileUtilities

A set of file utility actions created for Google SecOps Community to power up playbook capabilities.  

Python Version - V3_11
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Verify SSL|Verify SSL Certificates when executing requests to Chronicle SOAR instance.|False|Boolean|false|


#### Dependencies
| |
|-|
|proto_plus-1.27.0-py3-none-any.whl|
|requests-2.32.5-py3-none-any.whl|
|httplib2-0.31.2-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|certifi-2026.1.4-py3-none-any.whl|
|python_magic-0.4.27-py2.py3-none-any.whl|
|anyio-4.12.1-py3-none-any.whl|
|typing_extensions-4.15.0-py3-none-any.whl|
|file_magic-0.4.1-py3-none-any.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|pyopenssl-25.3.0-py3-none-any.whl|
|google_auth-2.47.0-py3-none-any.whl|
|google_api_core-2.29.0-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl|
|httpcore-1.0.9-py3-none-any.whl|
|google_auth_httplib2-0.3.0-py3-none-any.whl|
|pyparsing-3.3.2-py3-none-any.whl|
|urllib3-2.6.3-py3-none-any.whl|
|protobuf-6.33.4-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|cryptography-46.0.3-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|google_api_python_client-2.188.0-py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.11-py3-none-any.whl|
|googleapis_common_protos-1.72.0-py3-none-any.whl|
|pycparser-3.0-py3-none-any.whl|
|TIPCommon-2.3.0-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl|
|filelock-3.16.1-py3-none-any.whl|
|EnvironmentCommon-1.0.3-py3-none-any.whl|
|pyasn1-0.6.2-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|


## Actions
#### Decode Base64
The action decodes base64 input string and returns the json object.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64 Input|Base64 Input string you would like to decode|True|String| |
|Encoding|Choose the encoding option from the list|True|List|UTF-8|



#### Add Attachment
The action adds an attachment to the case wall (similar to attach evidence)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Name|The name of the attachment|True|String|Name|
|IsFavorite|Is the attachment marked as favorite in the case wall |False|Boolean|false|
|Base64 Blob|The attachment's content in Base64|True|String|<Base64 here>|
|Type|Attachment Type|True|String|.txt|
|Description|The description of the attachment |True|String|Description|



#### Create Hash From Base64
Returns hashes for provided base64s.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Base64|One more more base64 encoded strings. Strings should be separated by the defined separator.|True|Content|-|
|Hash Algorythm|hash type (sha1, sha256, md5...)|True|List|sha1|
|Names|List of names that identify the base64 strings. Typically filenames. List of names must contain the same quantity as the list of base64 strings.|False|String||
|Names Separator|A character to separate the list of names by.|True|String|,|
|Include Base64|Include the base64 input strings in the output.|False|Boolean|true|
|Base64 Separator|A character to separate the base64 strings by.|True|String|,|



#### Add Entity to File
This action will add the identifier of a target entity to a local file.  It will only add one occurance of the entity to the file and will return False if the entity already exists.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filename|The name of the file to write the entities to.|True|String|<filename.out>|



#### Create Archive
Creates an archive file from a list of provided files or a directories.  Supports: zip, tar, gztar, bztar, xtar.
Returns the location of the archive file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Archive Type|The type of archive to create.  Supports: zip,uncompressed tar-filegzip'ed tar-filebzip2'ed tar-filexz'ed tar-file|True|List|zip|
|Archive Base Name|The name of the archive file that will be created without the extension.|True|String|<filename>|
|Archive Input|Either a comma delimited list of files or a directory path.|True|String|<archive input>|



#### Count Files
The action counts files in a given folder path according to a specific file extension
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Extension|Count the files that include a specific file extension|False|String|*.txt|
|Folder|The folder path from which you would like to count the files|True|String|/tempFolder|
|Is Recursive|If enabled, this will recursively count all files in the directory.|False|Boolean|false|



#### Extract Archive
Extracts an archive file to a directory..  Supports: zip, tar, gztar, bztar, xtar.
Returns the extracted path and files.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Archive|The  path of the archive to be extracted.  Supports comma delimitedExample: /opt/siemplify/siemplify_server/Scripting/FileUtilities//file.zip|True|String|<archive file with path>|



#### Extract Zip Files
This action will extract files from a ZIP archive.  It has the ability to extract password protected files by either a supplied password or bruteforce. Requires FILENAME entity to have attachment_id attribute to download file from Case Wall.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Include Data In JSON Result|Include the data from the extracted files as base64 encoded values in the JSON result of the action.|False|Boolean|false|
|Create Entities|Create entities out of the extracted files.|False|Boolean|true|
|Zip File Password|If the zip file is password protected, use this password to extract.|False|String||
|BruteForce Password|When enabled, the action will attempt to brute force any password protected Zip files.|False|Boolean|false|
|Add to Case Wall|Add the extracted files to the case wall.|False|Boolean|true|
|Zip Password List Delimiter|This is character that separates multiple passwords in the Zip File Password parameter.|True|String|,|



#### Get Attachment
The actions gets an attachment from the case wall (the result is presented as a Base64)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Attachment Scope|The scope of the attachment that needs to be retrieved - case or alert|True|List|Alert|



#### Get Files as Base64
Converts local files to base64 strings.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Paths|A comma delimited list of files, including their path.|True|String|/path/file.exe|



#### Ping
Check connectivity
Timeout - 600 Seconds



#### Remove Entity from File
This action will remove the identifier of a target entity from a local file. It will return False if it failed to remove all entities or an entity does not exist.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filename|The name of the file to write the entities to.|True|String|<filename.out>|



#### Save Base64 to File
The action saves a base64 string to a file.  It supports comma separated lists for Filename and Base64 Input.  The optional File Extension parameter is used to add an extension to the output filename.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Extension|Optional: this will add the supplied extension to the filename.|False|String|None|
|Base64 Input|The base64 string that will be converted to a file.  Supports comma separation. |True|String|<base64_encoded_string>|
|Filename|The filename the base64 string will be saved as.|True|String||










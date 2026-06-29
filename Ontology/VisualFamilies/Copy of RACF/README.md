<p align="center">
<img src="./Copy of RACF.png" 
     alt="Copy of RACF" width="200"/></p>
     
# Copy of RACF

### Description
Mainframe resource access

### Rules
|Primary Source|Secondary Source|Third Source|Forth Source|Type|Primary Destination|Secondary Destination|Third Destination|Forth Destination|
|--------------|----------------|------------|------------|----|-------------------|---------------------|-----------------|-----------------|
|SourceUserName|DestinationProcessName|||Type|DestinationProcessName|FileName|SourceUserName||
|SourceUserName||||Linked|SourceProcessName||||
|DestinationProcessName||||Linked|FileName||||
Addon
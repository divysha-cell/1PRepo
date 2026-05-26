<p align="center">
<img src="./Copy of AV.png" 
     alt="Copy of AV" width="200"/></p>
     
# Copy of AV

### Description
Anti-virus alerts visualization

### Rules
|Primary Source|Secondary Source|Third Source|Forth Source|Type|Primary Destination|Secondary Destination|Third Destination|Forth Destination|
|--------------|----------------|------------|------------|----|-------------------|---------------------|-----------------|-----------------|
|DestinationHostName|DestinationAddress|||Type|DestinationHostName|DestinationAddress|||
|DestinationHostName||||Linked|DestinationAddress||||
|DestinationHostName|DestinationAddress|||Linked|DestinationUserName||||
|DestinationHostName|DestinationAddress|||Linked|FileName|FileHash|ThreatSignature||
|FileName||||Linked|FileHash||||
|FileName|FileHash|||Linked|ThreatSignature||||
|FileName|FileHash|||Linked|DestinationProcessName||||
This is a Readme Addon - An add-on is an optional software component, plugin, or extension that expands the capabilities of base software. It lets users personalize and automate their digital tools. Add-ons serve a variety of purposes, including ad-blocking in browsers, gameplay modifications, and workflow enhancements.
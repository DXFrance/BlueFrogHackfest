# BlueFrogHackfest

sample code and documentation for a HackFest with BlueFrog Robotics

Here is the description of the folders of this repo: 

- General: General info on Azure, how to automate it etc.
- BlobStorage: How to save and restore data to/from blob storage thru Shared Access Signatures
- MessageCollection: collect message such as log events, commands, monitoring etc. 
- ExportedSampleResourceGroup: ARM files exported from the portal, containing Azure resources 

## about the eventhubarchive branch

At the time of this writing (mid november 2016), Event Hub Archive is in preview. 
It is hard to find samples reading Avro files that were archived by the Event Hub.

At the time of this writing (mid november 2016, Azure Data Lake has just GAed), there is no Avro integration in U-SQL either.

We didn't have time to develop such samples. 

In the master branch, event hub archive is not used. 
A simpler archiving thru Azure Stream Analytics is used.

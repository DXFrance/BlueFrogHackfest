# sample data

The `05` file was extracted from Azure blob storage. It was copied from event hub by the archive feature.

Here is where it was in blob storage: 

![](img/sample-file-stored-by-eh.png)

Here is how the content of the file look like (approcimate encoding here):

```
Objavro.codecnullavro.schemaÞ{"type":"record","name":"EventData","namespace":"Microsoft.ServiceBus.Messaging","fields":[{"name":"SequenceNumber","type":"long"},{"name":"Offset","type":"string"},{"name":"EnqueuedTimeUtc","type":"string"},{"name":"SystemProperties","type":{"type":"map","values":["long","double","string","bytes"]}},{"name":"Properties","type":{"type":"map","values":["long","double","string","bytes"]}},{"name":"Body","type":["null","bytes"]}]} 4c-„I˜iC{cEJŒ>Â 0*11/16/2016 4:44:11 PMx-opt-publisherbuddy1234  P{"field1": "value1", "field2": "value2"}4c-„I˜iC{cEJŒ>
``` 

which could be reformatted as: 
```
Objavro.codecnullavro.schema
{
    "type":"record",
    "name":"EventData",
    "namespace":"Microsoft.ServiceBus.Messaging",
    "fields":
        [
            {
                "name":"SequenceNumber",
                "type":"long"
            },
            {
                "name":"Offset",
                "type":"string"
            },
            {
                "name":"EnqueuedTimeUtc",
                "type":"string"
            },
            {
                "name":"SystemProperties",
                "type": {
                    "type":"map",
                    "values":
                    [
                        "long","double",
                        "string","bytes"
                    ]
                }
            },
            {
                "name":"Properties",
                "type": {
                    "type":"map",
                    "values":
                    [
                        "long","double",
                        "string","bytes"
                    ]
                }
            },
            {
                "name":"Body",
                "type":["null","bytes"]
            }
        ]
    }
    
    { 0*11/16/2016 4:44:11 PMx-opt-publisherbuddy1234  
        P{"field1": "value1", "field2": "value2"}
    4c-„I˜iC{cEJŒ>
``` 

More in the `AzureDataLake` folder.
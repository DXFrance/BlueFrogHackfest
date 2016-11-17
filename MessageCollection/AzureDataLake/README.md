# Azure Data Lake

This folder is about data that was stored in Azure Blob storage by event hub.

Azure Data Lake Analytics can be used to read that data and transform it. 


At the time of this writing, Event Hub Archive is in preview. 
It is hard to find samples reading Avro files that were archived by the Event Hub.

The sample solution that was tried proived the following result so far:

```
System.Runtime.Serialization.SerializationException: Type 'Microsoft.ServiceBus.Messaging.EventData' is not supported by the resolver.
   at Microsoft.Hadoop.Avro.AvroDataContractResolver.ResolveType(Type type)
   at Microsoft.Hadoop.Avro.Schema.ReflectionSchemaBuilder.CreateSchema(Boolean forceNullable, Type type, Dictionary`2 schemas, UInt32 currentDepth)
   at Microsoft.Hadoop.Avro.Schema.ReflectionSchemaBuilder.BuildSchema(Type type)
   at Microsoft.Hadoop.Avro.AvroSerializer.CreateForCore[T](String writerSchema, AvroSerializerSettings settings)
   at Microsoft.Hadoop.Avro.AvroSerializer.Create[T](AvroSerializerSettings settings)
   at Microsoft.Hadoop.Avro.AvroSerializer.Create[T]()
   at AvroSample.Program.Main(String[] args) in C:\dev\_git\GitHub\BlueFrogHackfest\MessageCollection\AzureDataLake\DataLakeVSSolution\AvroSample\Program.cs:line 20
```

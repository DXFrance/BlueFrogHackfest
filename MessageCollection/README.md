# Message collection

## Introduction

Messages are sent thru HTTPS to Event Hubs. 

Event Hubs can store data to blob storage. It can also be read by services like Azure Stream Analytics.
Azure Stream Analytics can then send data to [Power BI](http://powerbi.com).

## Event Hubs

cf [Event Hub README](EventHub/README.md)

## Avro

info on Avro file format: 

- <http://avro.apache.org/docs/current/>
- <http://www.nuget.org/packages?q=avro>
- <https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-dotnet-avro-serialization>

info on Avro and Event hub
- <https://docs.microsoft.com/en-us/dotnet/api/microsoft.servicebus.messaging.eventdata>
- <https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-archive-overview>

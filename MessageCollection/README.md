# Message collection

## Introduction

Messages are sent thru HTTPS to Event Hubs. 

Event Hubs can store data to blob storage. It can also be read by services like Azure Stream Analytics.
Azure Stream Analytics can then send data to [Power BI](http://powerbi.com).

## Event Hubs

In order to deploy the event hub in an automated way in the `$resourceGroupName`, get the files in the EventHub folder below, 
change the values in `parameters.json` and issue a command like the following: 

```
resourceGroupName=tbrresgroup
templateFilePath=template.json
parametersFilePath=parameters.json
deploymentName=deployment-v161115a

az resource group create --name $resourceGroupName --location 'West Europe'

az resource group deployment create --name $deploymentName --resource-group $resourceGroupName \
    --template-file $templateFilePath --parameters @$parametersFilePath
```

It is interesting to have an automated way of creating the event hub because, in development, dropping it and crecreating it is the simplest / only way to empty it.

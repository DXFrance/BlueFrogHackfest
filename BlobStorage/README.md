# blob storage

This page provides info on how blob storage that is relevant for the project

## introduction

We'll use Azure blob storage, block blobs.
The access tier may be hot or cool. The difference between the two is cost.

- <https://azure.microsoft.com/en-us/documentation/articles/storage-introduction/>
- <https://azure.microsoft.com/en-us/documentation/articles/storage-create-storage-account/>
- <https://azure.microsoft.com/en-us/documentation/articles/storage-blob-storage-tiers/>

## create a storage account

Here is an example with a script: 

```
az resource group create --name tbrresgroup --location 'West Europe'
az storage account create --resource-group tbrresgroup \
    --access-tier Hot --name tbrmoncomptedesto --sku Standard_GRS \
    --location 'West Europe' --kind BlobStorage --encryption blob
```

An equivament ARM template would look like this

```
{
    "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "storageAccount_name": {
            "defaultValue": "tbrmoncomptedesto",
            "type": "String"
        }
    },
    "variables": {},
    "resources": [
        {
            "type": "Microsoft.Storage/storageAccounts",
            "sku": {
                "name": "Standard_GRS",
                "tier": "Standard"
            },
            "kind": "BlobStorage",
            "name": "[parameters('storageAccount_name')]",
            "apiVersion": "2016-01-01",
            "location": "westeurope",
            "tags": {},
            "properties": {
                "accessTier": "Hot",
                "encryption": {
                    "keySource": "Microsoft.Storage",
                    "services": {
                        "blob": {
                            "enabled": true
                        }
                    }
                }
            }
        }
    ]
}
```


## Shared Access Signature

- <https://azure.microsoft.com/en-us/documentation/articles/storage-dotnet-shared-access-signature-part-1/>

## Concurrency access

This could be done thru the Etag property.
Basically, the principle is to get the blob with its Etag. Then while updating, require an update for the blob with this Etag. 
If the same blob, and the its Etag wasn't changed by anybody else the update will succeed; else it will fail.

more at <https://azure.microsoft.com/en-us/blog/managing-concurrency-in-microsoft-azure-storage-2/>

## pricing

- <https://azure.microsoft.com/en-us/pricing/details/storage/blobs/>


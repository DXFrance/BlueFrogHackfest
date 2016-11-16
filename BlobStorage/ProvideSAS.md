# Provide Blob SAS

An Azure Function (named `tbrblobsasfunapp` in this example) is created (new function app in the [portal](https://portal.azure.com)) 
in which the following code is deployed.

The method in the Azure function is `SasTokenCSharp1`.

NB: this code is based on the sample provided by Azure Functions: 

![](img/new-function-blob-sas.png)

You can find it in the `ProvideSAS-code.cs` file.


App Settings contains the following value for the new key `datacollectionblobstoragecn`:
```
DefaultEndpointsProtocol=https;AccountName=tbrdatacollection;AccountKey=kjCcNxtjDMCaXLkDtl5MPyEYTfSaZm4YNGHnLGq8zx+KlB+NgCf/ivahtXGFm0QwjaulI3UuBUJjMUOKGFsxjw==
```

the function app has a code that protects the calls. 
This mechanism can be enhanced depending on how the robot manages its secrets.

Sample usage from the command line with sample result: 

```
curl --url 'https://tbrblobsasfunapp.azurewebsites.net/api/SasTokenCSharp1?code=FSlGrCgbwvKvIs6MSzMztO8m9kyCSY31TPB0Bb947gfSnxMtXojkhA==' \
    --request 'POST' \
    --header 'Content-Type: application/json' \
    --data '{"container": "configcontainer", "blobName": "folder1/folder2/1.png", "permissions": "Read,List"}'

$ curl --url 'https://tbrblobsasfunapp.azurewebsites.net/api/SasTokenCSharp1?code=FSlGrCgbwvKvIs6MSzMztO8m9kyCSY31TPB0Bb947gfSnxMtXojkhA==' \
>     --request 'POST' \
>     --header 'Content-Type: application/json' \
>     --data '{"container": "configcontainer", "blobName": "folder1/folder2/1.png", "permissions": "Read,List"}'
{"token":"?sv=2015-12-11&sr=b&sig=cEx%2F8l9NQgoGgnz4xaCfyblh3Wa3I7Ju8TM9uyqGpFE%3D&st=2016-11-16T13%3A48%3A58Z&se=2016-11-16T14%3A53%3A58Z&sp=rl","uri":"https://tbrdatacollection.blob.core.windows.net/configcontainer?sv=2015-12-11&sr=b&sig=cEx%2F8l9NQgoGgnz4xaCfyblh3Wa3I7Ju8TM9uyqGpFE%3D&st=2016-11-16T13%3A48%3A58Z&se=2016-11-16T14%3A53%3A58Z&sp=rl"}
```

more info: 
- <https://github.com/Azure/azure-webjobs-sdk-templates/blob/master/Templates/SasToken-CSharp/readme.md>
- <https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings>
- <http://stackoverflow.com/questions/38123708/use-cloud-app-settings-in-azure-functions>

another example that creates a blob, then reads it: 

```
curl --url 'https://tbrblobsasfunapp.azurewebsites.net/api/SasTokenCSharp1?code=FSlGrCgbwvKvIs6MSzMztO8m9kyCSY31TPB0Bb947gfSnxMtXojkhA==' \
    --request 'POST' \
    --header 'Content-Type: application/json' \
    --data '{"container": "configcontainer", "blobName": "folder1/folder2/test.txt", "permissions": "Write"}'

{"token":"?sv=2015-12-11&sr=b&sig=DPdpnQs3BX5OKU7kZiHy76p1UQuQjq4NCRiiMrrXIqk%3D&st=2016-11-16T15%3A20%3A43Z&se=2016-11-16T16%3A25%3A43Z&sp=w","uri":"https://tbrdatacollection.blob.core.windows.net/configcontainer?sv=2015-12-11&sr=b&sig=DPdpnQs3BX5OKU7kZiHy76p1UQuQjq4NCRiiMrrXIqk%3D&st=2016-11-16T15%3A20%3A43Z&se=2016-11-16T16%3A25%3A43Z&sp=w"}
	
curl --url 'https://tbrdatacollection.blob.core.windows.net/configcontainer/folder1/folder2/test.txt?sv=2015-12-11&sr=b&sig=DPdpnQs3BX5OKU7kZiHy76p1UQuQjq4NCRiiMrrXIqk%3D&st=2016-11-16T15%3A20%3A43Z&se=2016-11-16T16%3A25%3A43Z&sp=w' \
    --request 'PUT' \
    --header 'Content-Type: text/plain' \
	--header 'x-ms-blob-type: BlockBlob ' \
    --data 'toto est rigolo'

curl --url 'https://tbrblobsasfunapp.azurewebsites.net/api/SasTokenCSharp1?code=FSlGrCgbwvKvIs6MSzMztO8m9kyCSY31TPB0Bb947gfSnxMtXojkhA==' \
    --request 'POST' \
    --header 'Content-Type: application/json' \
    --data '{"container": "configcontainer", "blobName": "folder1/folder2/test.txt", "permissions": "Read"}'

{"token":"?sv=2015-12-11&sr=b&sig=HbbswWVl5o3mkNcuYg3cUIjYecmHOJ%2BFtQ5ptXER7ic%3D&st=2016-11-16T15%3A24%3A58Z&se=2016-11-16T16%3A29%3A58Z&sp=r","uri":"https://tbrdatacollection.blob.core.windows.net/configcontainer?sv=2015-12-11&sr=b&sig=HbbswWVl5o3mkNcuYg3cUIjYecmHOJ%2BFtQ5ptXER7ic%3D&st=2016-11-16T15%3A24%3A58Z&se=2016-11-16T16%3A29%3A58Z&sp=r"}
	
curl --url 'https://tbrdatacollection.blob.core.windows.net/configcontainer/folder1/folder2/test.txt?sv=2015-12-11&sr=b&sig=HbbswWVl5o3mkNcuYg3cUIjYecmHOJ%2BFtQ5ptXER7ic%3D&st=2016-11-16T15%3A24%3A58Z&se=2016-11-16T16%3A29%3A58Z&sp=r' \
    --request 'GET'
```

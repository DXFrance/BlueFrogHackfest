# Provide Shared Access Signature for Event Hub

An Azure Function (named `tbrblobsasfunapp` for bad reasons ;-) in this example) is created (new function app in the [portal](https://portal.azure.com)) 
in which the following code is deployed.

The method in the Azure function is `EventHubSasTokenCSharp`. 
It can be created from a `C#` `API & WebHooks` `HttpTriggerCSharp` template. 

You can find it in the `ProvideSAS-code.cs` file.

Basically, this Azure function works like the one for Blob storage.

The App Settings are: 

`EH_1_SAS_PolicyName` = `SendPolicy` 
`EH_1_SAS_Namespace` = `tbreventhubnamespace` 
`EH_1_SAS_HubName` = `tbrOurEventHub`
`EH_1_SAS_Key` = `clnIRs4nBh1Pb7VvOUkKDg74xWV8bC0gPElKq8jrUI0=`

sample call and its return: 

```
curl --url 'https://tbrblobsasfunapp.azurewebsites.net/api/EventHubSasTokenCSharp?code=4BfLzxllhuKph2REBO6c3lhikjPs17ITdRGLJjyOVHixkREe823HqQ==' \
    --request 'POST' \
    --header 'Content-Type: application/json' \
    --data '{"publisherName": "buddy356334", "tokenTimeToLive": "30"}'

"SharedAccessSignature sr=https%3a%2f%2ftbreventhubnamespace.servicebus.windows.net%2ftbrOurEventHub%2fpublishers%2fbuddy356334%2fmessages&sig=7pVP%2fk6y%2fg8EnOgXIxd4d974e9PwAhtaRWhXcf50RXo%3d&se=1479314946&skn=SendPolicy"
```

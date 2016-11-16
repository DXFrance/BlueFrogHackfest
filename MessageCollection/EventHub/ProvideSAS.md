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

sample calls (get the SAS, then use it): 

```
curl --url 'https://tbrblobsasfunapp.azurewebsites.net/api/EventHubSasTokenCSharp?code=4BfLzxllhuKph2REBO6c3lhikjPs17ITdRGLJjyOVHixkREe823HqQ==' \
    --request 'POST' \
    --header 'Content-Type: application/json' \
    --data '{"publisherName": "buddy356334", "tokenTimeToLive": "70"}'

"SharedAccessSignature sr=https%3a%2f%2ftbreventhubnamespace.servicebus.windows.net%2ftbrOurEventHub%2fpublishers%2fbuddy1234%2fmessages&sig=jRn7rfYFOOI5DbRtm7Vl%2fxEXxMe5IGZ2oT2tZtxEb94%3d&se=1479317809&skn=SendPolicy"
	
curl --url 'https://tbreventhubnamespace.servicebus.windows.net/tbrOurEventHub/publishers/buddy1234/messages' \
    --request 'POST' \
    --header 'Authorization: SharedAccessSignature sr=https%3a%2f%2ftbreventhubnamespace.servicebus.windows.net%2ftbrOurEventHub%2fpublishers%2fbuddy1234%2fmessages&sig=jRn7rfYFOOI5DbRtm7Vl%2fxEXxMe5IGZ2oT2tZtxEb94%3d&se=1479317809&skn=SendPolicy' \
    --header 'Content-Type: application/json' \
    --data '{"field1": "value1", "field2": "value2"}'
```

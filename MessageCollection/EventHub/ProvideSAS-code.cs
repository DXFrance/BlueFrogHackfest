#r "Microsoft.ServiceBus"

using System.Net;
using Microsoft.ServiceBus;
using System.Configuration;

public static async Task<HttpResponseMessage> Run(HttpRequestMessage req, TraceWriter log)
{
    
    log.Info("Generate Shared Access Signature for Event Hub");

    // parse query parameter

    string publisherName = req.GetQueryNameValuePairs()
        .FirstOrDefault(q => string.Compare(q.Key, "publisherName", true) == 0)
        .Value;

    string tokenTimeToLiveParam = req.GetQueryNameValuePairs()
        .FirstOrDefault(q => string.Compare(q.Key, "tokenTimeToLive", true) == 0)
        .Value;
        

    // Get request body
    dynamic data = await req.Content.ReadAsAsync<object>();

    // Set name to query string or body data
    publisherName = publisherName ?? data?.publisherName;
    tokenTimeToLiveParam = tokenTimeToLiveParam ?? data?.tokenTimeToLive;

    if( publisherName == null)
        return req.CreateResponse(HttpStatusCode.BadRequest, "Please pass a publisherName on the query string or in the request body");

    TimeSpan tokenTimeToLive;
    if( tokenTimeToLiveParam == null)
        {tokenTimeToLive = TimeSpan.FromMinutes(60);}
    else
        {tokenTimeToLive = TimeSpan.FromMinutes(double.Parse(tokenTimeToLiveParam));}

    var appSettings = ConfigurationManager.AppSettings;
    var sas = CreateForHttpSender(
                                appSettings["EH_1_SAS_PolicyName"],
                                appSettings["EH_1_SAS_Key"],
                                appSettings["EH_1_SAS_Namespace"], 
                                appSettings["EH_1_SAS_HubName"], 
                                publisherName, 
                                tokenTimeToLive);
    
    if (string.IsNullOrEmpty(sas))
       {return req.CreateResponse(HttpStatusCode.NoContent, "No SaS found!");}
        else
        {return req.CreateResponse(HttpStatusCode.OK, sas);}
   

}

public static string CreateForHttpSender(string senderKeyName, string senderKey, string serviceNamespace, string hubName, string publisherName, TimeSpan tokenTimeToLive)
{ 
            var serviceUri = ServiceBusEnvironment.CreateServiceUri("https", serviceNamespace, String.Format("{0}/publishers/{1}/messages", hubName, publisherName))
                .ToString()
                .Trim('/');
            return SharedAccessSignatureTokenProvider.GetSharedAccessSignature(senderKeyName, senderKey, serviceUri, tokenTimeToLive);
}

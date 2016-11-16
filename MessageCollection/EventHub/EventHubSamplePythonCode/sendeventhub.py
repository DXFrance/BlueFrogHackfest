#!/user/bin/python
import sys
import azure
import socket

from azure.servicebus import (
  _service_bus_error_handler
  )

from azure.servicebus.servicebusservice import (
  ServiceBusService,
  ServiceBusSASAuthentication
  )

from azure.http import (
  HTTPRequest,
  HTTPError
  )

from azure.http.httpclient import _HTTPClient

class EventHubClient(object):

  def sendMessage(self,body,partition_key):
    eventHubHost = "iot34ns.servicebus.windows.net"

    httpclient = _HTTPClient(service_instance=self)

    sasKeyName = "devices"
    sasKeyValue = "9DiC0UfzRn/EeQdg9+84UPyJLprQbXvhrqPzt9ayubo="
    eventhubname = "iotte"
    
    authentication = ServiceBusSASAuthentication(sasKeyName,sasKeyValue)

    request = HTTPRequest()
    request.method = "POST"
    request.host = eventHubHost
    request.protocol_override = "https"
    request.path = "/" + eventhubname + "/publishers/" + partition_key + "/messages?api-version=2014-01"
    request.body = _get_request_body(body)
    request.headers.append(('Content-Type', 'application/atom+xml;type=entry;charset=utf-8'))

    authentication.sign_request(request, httpclient)

    request.headers.append(('Content-Length', str(len(request.body))))

    status = 0

    try:
        resp = httpclient.perform_request(request)
        status = resp.status
    except HTTPError as ex:
        status = ex.status

    return status

class EventDataParser(object):

  def getMessage(self,payload,sensorId):
    host = socket.gethostname()
    body = "{ \"DeviceId\" : \"" + host + "\",\"SensorData\": [ "

    msgs = payload.split(",")
    first = True

    for msg in msgs:
    # print msg
      sensorType = msg.split(":")[0]
      sensorValue = msg.split(":")[1]
      if first == True:
        first = False
      else:
        body += ","

      body += "{ \"SensorId\" : \"" + sensorId + "\", \"SensorType\" : \"" + sensorType + "\", \"SensorValue\" : " + sensorValue + " }"
    body += "]}"

    return body

hubClient = EventHubClient()
parser = EventDataParser()
hostname = socket.gethostname()
sensor = sys.argv[2]

body = parser.getMessage(sys.argv[1],sensor)
print body
hubStatus = hubClient.sendMessage(body,hostname)
# return the HTTP status to the caller
print hubStatus
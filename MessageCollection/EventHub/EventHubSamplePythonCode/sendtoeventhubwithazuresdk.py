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

#from azure.http import (
#  HTTPRequest,
#  HTTPError
#  )

#from azure.http.httpclient import _HTTPClient


sbnamespace = "iot34ns"
sasKeyName = "devices"
sasKeyValue = "9DiC0UfzRn/EeQdg9+84UPyJLprQbXvhrqPzt9ayubo="
eventhubname = "iotte"
thisdevice = "onedevice"

sbs = ServiceBusService(service_namespace=sbnamespace, 
    shared_access_key_name=sasKeyName, 
    shared_access_key_value=sasKeyValue)

sbs.send_event(eventhubname, "testing", device_id=thisdevice)


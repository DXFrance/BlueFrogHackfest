import sys
import azure
import socket

from azure.servicebus import (
  _service_bus_error_handler
  )

from azure.servicebus.servicebusservice import (
  ServiceBusService
  )

"""configuration and secrets the module must know"""
root_sas_key_name="RootManageSharedAccessKey"
root_sas_key_value="OqX/WGIv/fGrVUaUgriDo1rgnxLaAYbPdj4M/VJNH00="

"""parameters from the command line"""
command=sys.argv[1]
hub_name=sys.argv[2]

print("command={}, hub={}"
      .format(command, hub_name))

sbs = ServiceBusService(service_namespace="IoT-FRTE-ns",
                        shared_access_key_name=root_sas_key_name,
                        shared_access_key_value=root_sas_key_value)

if command == "delete":
    sbs.delete_event_hub(hub_name)
    print("deleted {}".format(hub_name))
else:
    print("unknown command: {}".format(command))


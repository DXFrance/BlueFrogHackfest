import json
import urllib2
import sys

"""parameters from the command line"""
service_bus_namespace=sys.argv[1]
hub_name=sys.argv[2]
device_name=sys.argv[3]
protocol=sys.argv[4] # AMQPS or HTTPS

"""default values that could also be parameters"""
api_version="2014-01"

"""get sas token that was provided by the field gateway"""
with open("sas.txt", "r") as sas_file:
    sas=sas_file.read().replace('\n','')

"""main code"""
print("============================================================================")
print("service bus namespace='{}', hub='{}', device name='{}', protocol={}, api version='{}'"
      .format(service_bus_namespace, hub_name, device_name, protocol,
              api_version))
print("will sign with '{}'".format(sas))

if protocol!="HTTPS" and protocol!="AMQPS":
    print("unknown protocol: '{}'", protocol)
    sys.exit()

if protocol=="HTTPS":
    url = "https://{}.servicebus.windows.net/{}/publishers/{}/messages?api-version={}" \
        .format(service_bus_namespace, 
                hub_name, 
                device_name,
                api_version)
    headers={
        'Content-Type':'application/atom+xml;type=entry;charset=utf-8',
        'Authorization': sas}

    for i in range(60, 70, 2):
        data = { 
            "deviceId": "one sensor data",
            "temperature": i+1,
            "heartbeat": i}
        body= str.encode(json.dumps(data))
        request=urllib2.Request(url, body, headers)
        print("sending '{}'".format(body))
        try:
            response = urllib2.urlopen(request)
            result = response.read()
            print(result) 
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(error.read())
        print("---------------------------------------")
elif protocol=="AMQPS":
    #from qpid.messaging import *
    from proton import *
    sas="devices:9DiC0UfzRn/EeQdg9+84UPyJLprQbXvhrqPzt9ayubo="
    url = "amqps://{}@{}.servicebus.windows.net/{}" \
        .format(sas, service_bus_namespace, hub_name)

    # Create Proton objects
    messenger = Messenger()

    for i in range(60, 61, 2):
        temp = 'T:25_L:500'
        print temp

        # Create AMQP message
        message = Message()

        # Initialize properties
        message.properties = dict()
        message.properties[symbol("DeviceId")] = symbol(device_name)

        # Map string to list, symbolize, create dict and merge
        pairs=map(lambda x:x.split(':'), temp.split('_'))
        symbols = map(lambda x:(symbol(x[0]),int(x[1])), pairs)
        message.properties.update(dict(symbols))

        message.address = url
        messenger.put(message)
        messenger.send()

        #data = { 
        #    "deviceId": "one sensor data",
        #    "temperature": i+1,
        #    "heartbeat": i}
        #broker=url
        #address="amq.topic"
        #body= str.encode(json.dumps(data))
        #connection = Connection(broker)

        #try:
        #    connection.open()
        #    session = connection.session()

        #    sender = session.sender(device_name)
        #    receiver = session.receiver(hub_name)

        #    sender.send(Message(body));

        #    message = receiver.fetch()
        #    print message.content
        #    session.acknowledge()

        #except MessagingError,m:
        #    print m

        #connection.close()

        print("---------------------------------------")
     
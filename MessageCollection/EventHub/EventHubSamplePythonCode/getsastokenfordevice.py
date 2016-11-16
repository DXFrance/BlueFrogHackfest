import base64
import hashlib
import hmac
import time
from urllib2 import quote as url_quote
import socket
import sys

"""parameters from the command line"""
service_bus_namespace=sys.argv[1]
hub_name=sys.argv[2]
device_name=sys.argv[3]
sas_key_name=sys.argv[4]
sas_key_value=sys.argv[5]
protocol=sys.argv[6] # AMQPS or HTTPS

"""default values that could also be parameters"""
api_version="2014-01"
expiration_in_seconds=3600

"""
the following methods were copied from the azure sdk for python
and simplified by assuming Python 2.7 is used
"""
def _decode_base64_to_bytes(data):
    if isinstance(data, unicode):
        data = data.encode('utf-8')
    return base64.b64decode(data)

def _encode_base64(data):
    if isinstance(data, unicode):
        data = data.encode('utf-8')
    encoded = base64.b64encode(data)
    return encoded.decode('utf-8')

def _sign_string(key, string_to_sign, key_is_base64=True):
    if key_is_base64:
        key = _decode_base64_to_bytes(key)
    else:
        if isinstance(key, unicode):
            key = key.encode('utf-8')
    if isinstance(string_to_sign, unicode):
        string_to_sign = string_to_sign.encode('utf-8')
    signed_hmac_sha256 = hmac.HMAC(key, string_to_sign, hashlib.sha256)
    digest = signed_hmac_sha256.digest()
    encoded_digest = _encode_base64(digest)
    return encoded_digest

"""main code"""

if protocol == "HTTPS":
    device_path = "https://{}.servicebus.windows.net/{}/publishers/{}/messages?api-version={}" \
        .format(service_bus_namespace, 
                hub_name, 
                device_name,
                api_version)
elif protocol == "AMQPS":
    device_path = "sb://{}.servicebus.windows.net/{}/publishers/{}" \
        .format(service_bus_namespace, 
                hub_name, 
                device_name)
else:
    print("unknown protocol: '{}'".format(protocol))
    sys.exit()

uri = url_quote(device_path, '').lower()

"""Returns the UTC datetime, in seconds since Epoch, when this signed 
request expires ({expiration_in_seconds} seconds from now)."""
expiry = int(round(time.time() + expiration_in_seconds))

to_sign = "{}{}{}".format(uri, '\n', expiry)

signature = url_quote(_sign_string(sas_key_value, to_sign, False), '')

#requests will have to be signed by adding a header with a key of Authorization 
#and a value of:
if protocol == "HTTPS":
    print("SharedAccessSignature sig={}&se={}&skn={}&sr={}"
          .format(signature, expiry, sas_key_name, uri))
elif protocol == "AMQPS":
    print("SharedAccessSignature:sig={}&se={}&skn={}&sr={}"
          .format(signature, expiry, sas_key_name, uri))

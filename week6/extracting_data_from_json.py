import urllib.request, urllib.parse, urllib.error
import ssl
import json
import sys
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: 
    print('Failed to retrieved, input valid url')
else: 
    print('Retrieving: ' + address)
    uh = urllib.request.urlopen(address, context = ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        info = json.loads(data)
    except:
        info = None
        sys.exit("=== Failure to Retrieve ===")
Sum = 0
count = len(info["comments"])
for item in info["comments"]:
    Sum += item["count"]
print(f'Count: {count}')
print(f'Sum: {Sum}')


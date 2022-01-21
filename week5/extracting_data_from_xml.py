from urllib.request import urlopen 
import xml.etree.ElementTree as ET
import ssl 


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving: ' + url)
html = urlopen(url, context = ctx).read()

print(f'Retrieved {len(html)} characters')
tree = ET.fromstring(html)
counts = []
lst = tree.findall('comments/comment')
for item in lst:
    counts.append(int(item.find('count').text))
print(f'Count: {len(counts)}')
print(f'Sum: {sum(counts)}')
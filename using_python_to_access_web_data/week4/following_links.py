# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def crawling(urlLink, count, position):
    print("Retrieving: " + urlLink)


    html = urlopen(urlLink, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    link = tags[position].get('href', None)

    if (count == 0):
        return
    count = count - 1
    crawling(link, count, position)

url = input('Enter URL: ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

crawling(url, count, position - 1)

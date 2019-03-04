
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
posi=input('Enter position: ')
count=input('Enter count: ')

posi=int(posi)
count=int(count)
runtime=1
while runtime<=count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    runtime=runtime+1
    y=tags[posi-1]
    print(y.get('href',None))
    url=y.get('href',None)

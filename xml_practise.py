import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url='http://py4e-data.dr-chuck.net/comments_128455.xmls'


uh=urllib.request.urlopen(url)
data=uh.read()
tree = ET.fromstring(data)
counts=tree.findall('comments/comment')
print(len(counts))
sum=0
for item in counts:
    y=item.find('count').text
    y=int(y)
    sum=sum+y
print(sum)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


url = 'http://py4e-data.dr-chuck.net/comments_1685348.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
data = data.decode()
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')

count = 0

for item in lst:
    tmp = int(item.find('count').text)
    count += tmp


print(count)




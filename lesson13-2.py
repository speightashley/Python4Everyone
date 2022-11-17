import json
from urllib.request import urlopen

url = 'http://py4e-data.dr-chuck.net/comments_1685349.json'

data = urlopen(url)

data_json = json.loads(data.read())
print(json.dumps(data_json, indent=4))
total = 0

for x in range(len(data_json['comments'])):
    total += int(data_json['comments'][x]['count'])

print(total)
# comment for comments sake

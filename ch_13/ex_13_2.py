import json
import urllib.request, urllib.parse, urllib.error

url = input("URL: ")
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
print('User count:', len(info))

total = 0

for item in info['comments']:
    total += int(item['count'])

print(total)
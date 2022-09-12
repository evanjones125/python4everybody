import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

total = 0

url = input("URL: ")
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

# for count in counts:
#     total += int(count.text)

for child in tree[1]:
    total += int(child[1].text)

print(total)
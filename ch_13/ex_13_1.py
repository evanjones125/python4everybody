import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

nums = []
total = 0

url = input("URL: ")
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

for child in tree[1]:
    nums.append(int(child[1].text))

for num in nums:
    total += num

print(total)
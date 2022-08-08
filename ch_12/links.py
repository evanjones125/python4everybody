import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Count: ')
position = input('Position: ')
lst = []

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # print(tag.get('href', None))
    lst.append(tag.get('href', None))


for i in range(int(count) - 1):
    url = lst[int(position) - 1]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst = []
    for tag in tags:
        lst.append(tag.get('href', None))

print(lst[int(position) - 1])
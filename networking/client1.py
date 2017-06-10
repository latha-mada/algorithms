#!/usr/bin/python

import requests
url="http://localhost:7070/ls"
headers = {'Content-type': 'application/json', 'X-Header':'dddd'}
r=requests.get(url,headers=headers)
print dir(r)
print r.status_code
print r.content
print r.text
print r.headers

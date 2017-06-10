#!/usr/bin/python
import sys
from AutoLib import *
#import requests
#url="http://localhost:7070/ls"
#headers = {'Content-type': 'application/json', 'X-Header':'dddd'}
#r=requests.get(url,headers=headers)
#print dir(r)
#print r.status_code
#print r.content
##print r.text
#print r.headers

#initial conditions

flag=Check_Disk_Space_On_RM()
if flag == False:
   sys.exit(0)
flag=IsImpala_Running()
if flag == False:
   sys.exit(0)
flag=IsNameNodeRunning()
if flag == False:
   sys.exit(0)

# execution
flag=Copy_To_Hdfs()
if flag == False:
   sys.exit(0)

Check_Data_In_HDFS()
if flag == False:
   sys.exit(0)

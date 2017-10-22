#!/usr/bin/python
import requests
import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="localhost"
port=7070
s.connect((host,port))
data = s.recv(4096)
print data
time.sleep(20)
url="http://localhost:7070/Users/gummida/latha/python-code/networking/ls"
r=requests.get(url)
print r.text

s.send("thanks for accepting")
s.close()


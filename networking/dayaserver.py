#!/usr/bin/python

import socket
import select
from threading import Thread
import time
import os
import subprocess

connList=[]
server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="localhost"
port=7070
server_sock.bind((host,port))
server_sock.listen(50)

def Handle_ls():
    proc = subprocess.Popen(['ls','-lrt'],stdout=subprocess.PIPE,)
    stdout_value = proc.communicate()[0]
    print 'stdout_value',stdout_value   
    con_len=str(len(stdout_value))
    con_len_header='Content-Length: '+con_len 
    resp=['HTTP/1.1 200 OK','Date: Mon, 27 Jul 2009 12:28:53 GMT','Server: Apache/2.2.14 (Win32)','Content-type: application/json',con_len_header,'Connection: Closed']
    Resp=''
    for x in resp:
       Resp=Resp+x +'\r\n'
    Resp=Resp+'\r\n'
    Resp=Resp+stdout_value
    print Resp
    return Resp
    

class RestApi(Thread):
    def __init__(self, conn,addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr=addr 
        print 'self.conn',self.conn
        print 'self.addr',self.addr
    def Get_Url(self,buf):
        req=buf.split('\r\n')
        return req[0]
    def Get_Headers(self,buf):
        Hdr_Dict={}
        req=buf.split('\r\n')
        for header in range(1,len(req)-1):
            if len(req[header]) == 0:
               continue
            Hdr=req[header]
            Hdr_par=Hdr.split(':')
            Hdr_name=Hdr_par[0].strip(' ')
            Hdr_value=Hdr_par[1].strip(' ')
            Hdr_Dict[Hdr_name]=Hdr_value
        return Hdr_Dict
    def Get_Api_Name(self,url): 
        parse_url=url.split(' ')
        return parse_url[1].strip('/')
    def run(self):
        self.data=''
        print 'xx'
        time.sleep(2)
        print 'yy'
        while 1:
            buf=self.conn.recv(4096)
            print buf
            if len(buf) == 0:
               break
            flag_end=buf.find('\r\n\r\n')
            if flag_end != -1:
               print 'full request'
            self.data=buf
            url=self.Get_Url(self.data)
            api_name=self.Get_Api_Name(url)
            print 'api_name',api_name
            print 'url',url
            headers=self.Get_Headers(self.data)
            print headers
            if api_name == 'ls':
               resp=Handle_ls()
               self.conn.send(resp)
               self.conn.close()
            print 'existing thread'
            break
            


while True:
        conn,addr = server_sock.accept() 
        RestApi(conn,addr).start()




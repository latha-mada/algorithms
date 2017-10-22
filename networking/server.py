#!/usr/bin/python

import socket
import select
import os
connList=[]
server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="localhost"
port=7070
server_sock.bind((host,port))
server_sock.listen(5)
connList.append(server_sock)
while True:
   read_socket,write_socket,error_socket = select.select(connList,[],[])
   for sock in read_socket:
     if sock == server_sock:
        conn,addr = sock.accept() 
        connList.append(conn)   
        print " new connection from ",addr
        conn.send("200 OK")
        num = read_data(sock)
        print num
        sock.close()
   #conn.close()
     else:
      try:
        data = sock.recv(4096)
        #print data
        #data=os.listdir(".")
        #print data
        sock.send(data)
        sock.close()
        connList.remove(sock)

      except:
        print "connection lost with "
        #sock.send("closing connection")
        sock.close()
        connList.remove(sock)


def read_data(sock):
  data=sock.recv(4096)
  print data
  return 1
sock.close()



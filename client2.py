import socket
import sys
import os
def create_client():
    s=socket.socket()
    host=socket.gethostname()
    port=9090
    s.connect((host,port))
    while True:
        replyback=raw_input("Reply..")
        s.send(replyback)
        print s.recv(1024)
    s.close()

'''
while True:
    data=s.recv(1024)
    if(data[:2]=='cd'):
        os.chdir(data[3:].decode('utf-8'))

'''
create_client()

    

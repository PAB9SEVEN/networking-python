import socket
import threading
from queue import Queue
import sys
import os
import time
number_of_threads=2
job_number=[1,2]
queue=Queue()
all_address=[]
all_connections=[]
def create_socket():
    try:
        
        global host
        global port
        global s
        s=socket.socket() #FUNCTION TO CREATE THE SOCKET
        host=socket.gethostname()#INBUILT FUNCTION TO CREATE THE SOCKET
        port=9090
    except socket.error as msg:
        print msg
def bind_socket():
    try:
        global host
        global port
        global s
        #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((host,port))#USED TO BIND THE SOCKET
        s.listen(5)#SOCKET LISTENS OUT THE CONNECTIONS
    except socket.error as msg:
        print msg
        time.sleep(3)
        bind_socket()
    
    

def socket_accept():
    connections,address=s.accept()
    print "Accepted the conections from "+ str(address)
    while True:
        data=connections.recv(1024)
        print data
        mess=raw_input("enter the message")
        print "Waiting for the reply.."
        connections.sendall(mess)
    connections.close()

'''
def sendcommands(connections):
    while True:
        cmd==input()
        if cmd=='quit':
            connections.close()
            s.close()
            sys.exit()
        if len(str(encode(cmd))) >0:
            connections.send(str(encode(cmd)))
            client_response=str(connections.recv(1024),'utf-8')
            print (client_response)

'''
'''
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]
    while True:
        try:
                
            connect,addr=s.accept()
            connect.setblocking(1)
            all_connections.append(connect)
            all_address.append(addr)
            print "Receiced connection from the client"+addr[0]
        except:
            print "Error connecting the client"
##def start_turtle():
##    while True:
##        cmd=input('owl> ')
##        if cmd =='list':
##            listconnections()
##        elif 'select' in cmd:
##            conn=get_target(cmd)
##            if conn is not None:
##                send_commands(conn)
##        else:
##            print "Not recognized"

##def listconnections():
##    results=''
##    for i,conn in ennumerate(all_connections):
##        try:
##            conn.send(' ')
##            conn.recv(20480)
##        except:
##            del all_connections[i]
##            del all_address[i]
##            continue
##        results+=str(i)+ '    '+ str(all_address[i][0])+ '    ' +str(all_address[i][1])
##    print ('Clients------>'+'\n'+results)
##    
                                     


'''
        
        
    
def main():
    create_socket()
    bind_socket()
    socket_accept()
##    accept_connections()
##    start_turtle()
main()


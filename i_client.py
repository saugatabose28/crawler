import socket
import sys
from crawler import *
import string 
server_address = ('localhost', 10003)

# Create a TCP/IP socket
socks =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 

# Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
socks.connect(server_address)

x=1
data='aditya'
while x==1 :
    l=socks.recv(2)
    length=int(l)
    data = socks.recv(length)
    urls=crawler(data)
    length=len(urls)
    socks.send((chr)(length))
    socks.send(urls)
    print data
    x=2
socks.close()



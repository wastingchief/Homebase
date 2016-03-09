#! usr/bin/python3

import socket
import re 


#TCP Client 
#The basic points of this program are assuming
##We will always have a successful connection
###The server is always expecting us to send data first 
####The server is always sending data back in a timely fashion

# We will start asking who is our target
##target = input("What is your IPv4 target hostname?") 
##target_port = input("What port will you be connecting on?") 


#Example of input
target_host = "www.google.com"
target_port = 80
recv_port
#Creating a socket object 
#"how our data will be transmitted"
#AF_INET = We will be using a standard IPv4 address or hostname
#SOCK_STREAM = We will be using our reliable (TCP) protocol as a client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Connecting to the client 
client.connect((target_host, target_prot))


#Send your data[transmission]
#Example "Get HTTP version 1.1" 
#sending string in bytes format to ommit error ive recived 
send = client.send(bytes("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"))

#Recive a response 
response = client.recv(recv_port)

print(response)




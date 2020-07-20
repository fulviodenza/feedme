import socket
import sys
import os
from termcolor import colored

try:
    import requests
except ImportError:
    print ('Install required module')
    os.system('python -m pip install requests')
import requests

TRED =  '\033[31m'
TYELLOW = '\033[37m'
ENDC = '\033[m'
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)

print('connecting to server...')
sock.connect(server_address)
try:    
    # Send data
    inputQ = input("\nInsert query to search\n")

    print('sending ', inputQ)

    sock.sendto(inputQ.encode(), ('localhost', 10001))
    data = sock.recv(256)
    data_len = len(data)
    print(len(data))
    i = 0
    while data_len != 0:
        dataD = data.decode('utf-8')
        if not data:
            break
        print(TRED + '[]' + ENDC + dataD)
        data = sock.recv(256)
        print(len(dataD))
        data_len =- 100
        i += 1

finally:
    print('closing socket')
    sock.close()

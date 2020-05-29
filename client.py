import socket
import sys

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
    data = sock.recv(1024)
    data_len = len(data)
    print(len(data))
    i = 0
    while data_len != 0:
        dataD = data.decode('utf-8')
        if not data:
            break
        print('[', i, ']', dataD)
        print('\n')
        data = sock.recv(1024)
        print(len(dataD))
        data_len =- 100
        i += 1

finally:
    print('closing socket')
    sock.close()
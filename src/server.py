import socket as sk
import time

socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_address = ('localhost', 10000)
print('Starting up on porn %s \n', server_address)
socket.bind(server_address)

while True:
    print('Waiting to receive message...\n')
    data, address = socket.recvfrom(4096)

    print('Received %s bytes from %s', len(data), address)
    print(data.decode('utf8'))

    
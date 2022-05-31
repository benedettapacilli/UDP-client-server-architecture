import socket as sk
import time

socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_address = ('localhost', 10000)
print('Starting up on {server_address[0]}, port {server_address[1]}')
socket.bind(server_address)
print('Now listening...\n')

while True:
    print('Waiting to receive message...\n')
    data, address = socket.recvfrom(4096)

    print('Received %s bytes from %s' % (len(data), address))
    message = data.decode('utf8')

    
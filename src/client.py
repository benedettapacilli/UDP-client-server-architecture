import socket as sk
import time

socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_address = ('localhost', 10000)
message = input("Enter your message to the server: \n")

try:
    print('Sending "%s..."' % message)
    time.sleep(2)
    sent = socket.sendto(message.encode(), server_address)

    print('Waiting to receive...')
    data, server = socket.recvfrom(4096)
    time.sleep(2)
    print('Received message "%s"' % data.encode('utf8'))
except Exception as info:
    print(info)
finally:
    print('Closing socket...')
    socket.close
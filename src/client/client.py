import socket as sk
import time

socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_address = ('localhost', 10000)
message = input("Enter your message to the server: \n")

print(f"Sending {message}")
sent = socket.sendto(message.encode(), server_address)

print('Waiting to receive...')
data, server = socket.recvfrom(4096)
print(f"Received message {data.encode('utf8')}")

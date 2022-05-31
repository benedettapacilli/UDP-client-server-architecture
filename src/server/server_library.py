import socket
buffersize = 4096

def get():
    socket.recvfrom(buffersize)


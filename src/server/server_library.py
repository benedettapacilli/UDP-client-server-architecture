import socket
import os

BUFFERSIZE = 4096
EOF = b' /EOF/ \r\n/'
SERVER_FILES = './server_files'

def list(socket, server_address, op):
    """ Enlists all files in the server_files directory """
    if not os.path.isdir(SERVER_FILES):
        os.mkdir(SERVER_FILES)
    file_list = os.listdir(SERVER_FILES)
    socket.sendto(str(len(file_list)).encode(), server_address)
    for file in file_list:
        socket.sendto(file.encode(), server_address)

def send(socket, server_address, op):
    """ Sends a file to the client """
    file_name = op.split()[1]
    if os.path.exists(SERVER_FILES + '/' + file_name):
        socket.sendto('yes'.encode(), server_address)
        with open(SERVER_FILES + '/' + file_name, 'rb') as f:
            while True:
                data = f.read(BUFFERSIZE)
                if not data:
                    socket.sendto(EOF, server_address)
                    f.close()
                    break
                socket.sendto(data, server_address)
        print('\nFile sent')
    else:
        socket.sendto('no'.encode(), server_address)

def receive(socket, op):
    """ Receives a file from the client """
    if not os.path.isdir(SERVER_FILES):
            os.mkdir(SERVER_FILES)
    file_name = op.split()[1]
    with open(SERVER_FILES + '/' + file_name, 'wb') as f:
        while True:
            data, addr = socket.recvfrom(BUFFERSIZE)
            if data == EOF:
                f.close()
                break
            f.write(data)
    print('\nFile received')

def end_process(socket):
    """ Ends the server process """
    socket.close()
    print('\nExiting...')
    exit()
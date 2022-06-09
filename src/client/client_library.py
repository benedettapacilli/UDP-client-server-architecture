import socket 
import os

BUFFERSIZE = 4096
EOF = b' /EOF/ \r\n/'
CLIENT_FILES = './client_files/'

def list(socket, server_address, op):
    """ Enlists all files in the server_files directory """
    print('\nListing files...')
    socket.sendto(op.encode(), server_address)
    data, address = socket.recvfrom(BUFFERSIZE)
    file_num = int(data.decode())
    if file_num == 0:
        print('\nNo files found')
    for i in range(file_num):
        data, address = socket.recvfrom(BUFFERSIZE)
        print(data.decode())

def get(socket, server_address, op):
    """ Gets a file from the server """
    socket.sendto(op.encode(), server_address)
    data, address = socket.recvfrom(BUFFERSIZE)
    file_check = data.decode()
    if file_check == 'no':
        print('\nFile not found')
    else:
        file_name = op.split()[1]
        print('\nFile found, downloading...')
        if not os.path.isdir(CLIENT_FILES):
            os.mkdir(CLIENT_FILES)
        with open(CLIENT_FILES + file_name, 'wb') as f:
            while True:
                data, address = socket.recvfrom(BUFFERSIZE)
                if data == EOF:
                    f.close()
                    print('\nFile downloaded')
                    break
                f.write(data)

def put(socket, server_address, op):
    """ Sends a file to the server """
    file_name = op.split()[1]
    if os.path.exists(CLIENT_FILES + file_name):
        socket.sendto(op.encode(), server_address)
        print('\nFile found, uploading...')
        with open(CLIENT_FILES + file_name, 'rb') as f:
            while True:
                data = f.read(BUFFERSIZE)
                if not data:
                    socket.sendto(EOF, server_address)
                    f.close()
                    break
                socket.sendto(data, server_address)
        print('\nFile uploaded')
    else:
        print('\nFile not found')
    
def end_process(socket, server_address, op):
    """ Ends the client process """
    socket.sendto(op.encode(), server_address)
    socket.close()
    print('\nExiting...')
    exit()
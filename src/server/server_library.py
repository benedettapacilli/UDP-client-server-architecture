import socket
import os

BUFFERSIZE = 4096
EOF = b' /EOF/ \r\n/'

def list(socket, server_address, op):
    file_list = os.listdir('./server_files')
    socket.sendto(str(len(file_list)).encode(), server_address)
    for file in file_list:
        socket.sendto(file.encode(), server_address)

def send(socket, server_address, op):
    file_name = op.split()[1]
    if os.path.exists('./server_files/' + file_name):
        socket.sendto('yes'.encode(), server_address)
        with open('./server_files/' + file_name, 'rb') as f:
            while True:
                data = f.read(BUFFERSIZE)
                if not data:
                    socket.sendto(EOF, server_address)
                    f.close()
                    break
                socket.sendto(data, server_address)
        print('File sent')
    else:
        socket.sendto('no'.encode(), server_address)

def receive(socket, op):
    file_name = op.split()[1]
    with open('./server_files/' + file_name, 'wb') as f:
        while True:
            data, addr = socket.recvfrom(BUFFERSIZE)
            if data == EOF:
                f.close()
                break
            f.write(data)
    print('File received')

def end_process(socket):
    socket.close()
    print('Exiting...')
    exit()
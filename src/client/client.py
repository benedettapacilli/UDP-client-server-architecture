import socket as sk
import client_library as cl

socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
server_address = ('localhost', 10000)

while True:
    op = input('\nEnter the operation: ')

    if op == 'list':
        cl.list(socket, server_address, op)
    elif op.startswith('get'):
        cl.get(socket, server_address, op)
    elif op.startswith('put'):
        cl.put(socket, server_address, op)
    elif op == 'exit':
        cl.end_process(socket, server_address, op)
    elif op == 'help':
        print('list: list files\nget <file_name>: download file\nput <file_name>: upload file\nexit: exit the program')
    else:
        print('Invalid operation')

    print('')
    

import socket as sk
import server_library as sl
import threading

BUFFERSIZE = 4096

SOCKET = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
SERVER_ADDRESS = ('localhost', 10000)
print(f'Starting up on {SERVER_ADDRESS[0]}, port {SERVER_ADDRESS[1]}')

def handler(op, address):
    """ Handles the client request """
    if op == 'list':
        sl.list(SOCKET, address, op)
    elif op.startswith('get'):
        sl.send(SOCKET, address, op)
    elif op.startswith('put'):
        sl.receive(SOCKET, op)

    print('')

SOCKET.bind(SERVER_ADDRESS)
print('Now listening...\n')

while True:
    print('\nWaiting to receive message...\n')
    data, address = SOCKET.recvfrom(BUFFERSIZE)

    print(f"Received {len(data)} bytes from {address}")
    op = data.decode('utf8')

    if op == 'exit':
        sl.end_process(SOCKET)
        break

    thread = threading.Thread(target=handler, args=(op, address))
    thread.start()
    thread.join()
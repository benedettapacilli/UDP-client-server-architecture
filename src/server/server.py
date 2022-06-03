import socket as sk
import server_library as sl
import threading

BUFFERSIZE = 4096

SOCKET = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
SERVER_ADDRESS = ('localhost', 10000)

def handler(op, address):
    while True:
        if op == 'list':
            sl.list(SOCKET, address, op)
        elif op.startswith('get'):
            sl.send(SOCKET, address, op)
        elif op.startswith('put'):
            sl.receive(SOCKET, op)
        elif op == 'exit':
            sl.end_process(SOCKET)

        print('')

print(f'Starting up on {SERVER_ADDRESS[0]}, port {SERVER_ADDRESS[1]}')
SOCKET.bind(SERVER_ADDRESS)
print('Now listening...\n')

while True:
    print('\nWaiting to receive message...\n')
    data, address = SOCKET.recvfrom(BUFFERSIZE)

    print(f"Received {len(data)} bytes from {address}")
    op = data.decode('utf8')

    thread = threading.Thread(target=handler, args=(op, address))
    thread.start()
    thread.join()
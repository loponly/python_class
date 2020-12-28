import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.connect(('127.0.0.1', 3333))
    sc.sendall(b'send from client')
    data = sc.recv(1024)

print(f'The data is {data}')

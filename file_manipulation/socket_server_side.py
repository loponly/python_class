import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.bind(('127.0.0.1', 3333))
    sc.listen()
    conn, addr = sc.accept()
    with conn:
        print(f'Connection is estableshed with {addr}')
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(b'Sent from server')

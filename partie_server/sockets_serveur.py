

import socket

HOST_IP = '127.0.0.1'
HOST_PORT =32000
MAX_BYTE = 1024


s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connection sur {HOST_IP} avec le port {HOST_PORT}...")
connection_sockets, client_address = s.accept()
print(f"Connection établit avec client {client_address}")

while True :
    connection_sockets.sendall(input("Vous : ").encode())
    info_recu = connection_sockets.recv(MAX_BYTE)

    if info_recu.decode() == "bye":
        print("Le client a quitté la conversation")
        connection_sockets.close()
        s.close()
        break

    else:
        print(f"Reçu : {info_recu.decode()}")

    
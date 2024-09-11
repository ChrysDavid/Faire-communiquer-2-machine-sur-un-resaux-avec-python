

import socket

HOST_IP = '' # Entrer l'address ip du serveur qui attack ici
HOST_PORT =32000
MAX_BYTE = 1024



print(f"connection au serveur {HOST_IP} avec le port {HOST_PORT}...")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError :
        print("ERREUR : Impossible de connecter au serveur. Reconnection...")
    else:
        print("Connecter au seveur")
        break

# ...
while True:
    info_recu = s.recv(MAX_BYTE)
    if info_recu.decode() == "bye":
        print("Le serveur a quitté la conversation")
        s.close()
        break
    else:
        print(f"Reçu : {info_recu.decode()}")
        s.sendall(input("Vous : ").encode())

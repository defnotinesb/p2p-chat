import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start() #threading just in case of multiple clients


def send(msg):
    message = msg.encode(FORMAT)
    server.send(message)

def handle_client(conn,addr):
    connected = True
    while connected:
        msg = conn.recv(2048).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE: 
            connected = False
        if not msg: 
            break

        print(f"[{addr}]:{msg}")
        conn.send(input("You:").encode(FORMAT))
        

    conn.close()
        



print("server is starting...")
start()

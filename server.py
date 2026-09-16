import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=receive, args=(conn, addr))
        thread.start() #threading just in case of multiple clients

def send():
    while True:
        msg = input("You: ")
        send_message(msg)

def send_message(msg):
    message = msg.encode(FORMAT)
    server.send(message)

def receive(conn,addr):
    connected = True
    while connected:
        msg = conn.recv(2048).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE: 
            break
        if not msg: 
            break

        print(f"[{addr}]:{msg}")



print("server is starting...")
start()
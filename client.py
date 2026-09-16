import socket

PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.36" #here you should use the computer private ipv4 that u are using for the server
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



def send_message(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(f"[{SERVER}]:{client.recv(2048).decode(FORMAT)}")


while True:
    message = input("You: ")
    send_message(message)

    if message == DISCONNECT_MESSAGE:
        break

    


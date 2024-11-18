import socket as sc
import threading as tr 
import ssl 

# Define  host server port and IP
HOST = '127.0.0.1'
PORT = 12897

# create ssl context 
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')


# initialize the server socket
s_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
s_socket.bind((HOST, PORT))
s_socket.listen(5)

print(f"Secure server running on{HOST}:{PORT}")

# List to store the connections by the clients
clients = []


def client_handling(c_socket, c_address):
    print(f"New connection from {c_address}")

    while True:
        try:
            # receive a message from a client
            msg = c_socket.recv(1024).decode('utf-8')
            if msg:
                print(f'Message received from {c_address}:{msg}')  # type: ignore
                # Broadcast the message to all the connected clients
                broadcast(msg, c_socket)  # type: ignore
            else:
                clients.remove(c_socket)
                break
        except:
            break

    c_socket.close()
    print(f"Connection from {c_address} is closed.")


# function to broadcast message to other clients
def broadcast(msg, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(msg.encode('utf-8'))
            except:
                clients.remove(client)


# Accepting client connections
while True:
    c_socket, c_address = s_socket.accept()

    # wrap the client socket with ssl 
    secure_socket = context.wrap_socket(c_socket, server_side=True)
    clients.append(secure_socket)

    # start a new thread to handle the client's messages
    thread = tr.Thread(target=client_handling, args=(c_socket, c_address))
    thread.start()

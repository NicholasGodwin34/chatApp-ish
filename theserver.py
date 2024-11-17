import socket as sc 

# Create a socket
client_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))  # Connect to server

# Send data
client_socket.send("You're the server!".encode())

# Receive response
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Close socket
client_socket.close()
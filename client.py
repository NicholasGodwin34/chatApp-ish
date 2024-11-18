import socket

def send_request():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # the AF_INET is used to specify the address family (ipv4) telling the socket to use ipv4 addresses 
    # SOCK_STREAM specifies the socket type (tcp)
    # if one is to make a UDP socket they would use SOCK_DGRAM
    # if one is to make a socket that uses ipv6 addresses they'd use AF_INET6

    # Connect to the server
    host = "127.0.0.1"  # Localhost
    port = 8080         # Same port as the server
    client_socket.connect((host, port))
   
    
    
    # Build and send an HTTP GET request
    request = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n"
    client_socket.sendall(request.encode())
    
    # Receive and print the response
    response = b""
    while True:
        chunk = client_socket.recv(102400)
        if not chunk:
            break
        response += chunk
    
    print("Response:")
    print(response.decode())
    
    # Close the connection
    client_socket.close()

def send_post_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8080))

    # Send a POST request with some data in the body
    post_data = "name=JohnDoe&age=25"
    request = f"POST / HTTP/1.1\r\nHost: 127.0.0.1\r\nContent-Length: {len(post_data)}\r\nConnection: close\r\n\r\n{post_data}"

    client_socket.sendall(request.encode())

    # Receive the response from the server
    response = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        response += chunk

    print("Response:")
    print(response.decode())

    client_socket.close()



#send_post_request()

# Send a request
send_request()

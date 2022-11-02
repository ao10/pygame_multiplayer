import socket

HOST = "127.0.0.1" # localhost
PORT = 8080

# Create a socket object
# AF_INET is IPv4
# SOCK_STREAM is the socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # .bind() method is used to associate the socket with a specific network interface and port
    s.bind((HOST, PORT))
    s.listen()
    # accept returns a socket and we'll use it to communicate with the client
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

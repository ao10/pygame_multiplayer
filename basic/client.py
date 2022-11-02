import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    # This reads the server's reply so we can print it at the end
    data = s.recv(1024)

print(f"Receieved {data!r}")


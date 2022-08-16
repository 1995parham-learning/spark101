import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1378))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"we have a new connection from {addr}")
        conn.sendall("Hello World\n".encode())
        time.sleep(1)  # wait for 1 sec
        conn.sendall("I am Elahe Dastan\n".encode())

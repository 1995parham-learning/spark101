import socket
import time
import json
import datetime


class Message:
    def __init__(self, line: str):
        self.line = line
        self.timestamp = datetime.datetime.now()


class MessageEncoder(json.JSONEncoder):
    def default(self, m: Message) -> dict[str, str]:
        return {
            "line": m.line,
            "timestamp": m.timestamp.isoformat(sep=" ", timespec="seconds"),
        }


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1378))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"we have a new connection from {addr}")
        print(json.dumps(Message("Hello World"), cls=MessageEncoder))
        conn.sendall(
            json.dumps(Message("Hello World"), cls=MessageEncoder).encode()
        )
        conn.sendall(b"\n")
        time.sleep(1)  # wait for 1 sec
        print(json.dumps(Message("I am Elahe Dastan"), cls=MessageEncoder))
        conn.sendall(
            json.dumps(
                Message("I am Elahe Dastan"), cls=MessageEncoder
            ).encode()
        )
        conn.sendall(b"\n")

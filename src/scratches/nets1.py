import socket
import threading
import pickle

ip = socket.gethostbyname_ex(socket.getfqdn())[2][0]
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", port))
sock.listen(5)

def manage_relay(conn, addr):
    print(f"Connection {conn} from address {addr}")
    bounddata = conn.recv(4096)
    data = pickle.loads(bounddata)
    print(f"Data: {data} \n")
    command, *args = data
    print(f"Command: {command} \t Args: {args}")

print(f"Beacon listening on {ip}:{port}")

while True:
    conn, addr = sock.accept()
    print(f"Connection from {addr}")
    threading.Thread(target=manage_relay, args=(conn, addr)).start()





import socket
import  pickle


from src.chain.Blockchain import Blockchain

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',8080))
b = Blockchain()
b.add_block("data 1")
b.add_block("data 2")
b.add_block("data 3")

bc = ("MINT", b)
sock.send(pickle.dumps(bc))
print("sent")
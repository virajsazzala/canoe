import pickle
import socket
import threading

from src.Consts import *
from src.chain.Block import Block
from src.network.Node import Node
from src.network.Relay import Relay


class Beacon:
    def __init__(self, local: bool = True):
        self.id = 1
        self.sock = None
        self.ip = socket.gethostbyname_ex(socket.getfqdn())[2][0] if not local else ''
        self.port = 8080
        self.relays = []
        self.bc = None


    def activate(self):
        if self.sock:
            raise Exception("Beacon connection already active.")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(5)
        print(f"Beacon listening on {self.ip}:{self.port}")

        while True:
            conn, addr = self.sock.accept()
            print(f"Connection from {addr}")
            threading.Thread(target=self.manage_relay, args=(conn, addr)).start()

    def manage_relay(self, conn, addr):
        bounddata = conn.recv(1024).decode()
        data = pickle.loads(bounddata)
        signal, *args = data
        if signal == "REGISTER":
            self.register_relay(args)
        elif signal == "UPDATE":
            self.update_chain(args[0])

    def register_relay(self, args):
        for relay in args:
            if relay not in self.relays and relay != f"{self.ip}:{self.port}":
                self.relays.append(relay)

        self.sync_relays()

    def sync_relays(self):
        for relay in self.relays:
            try:
                self.sock.connect(tuple(relay.split(":")))
                bound_relays = pickle.dumps(("ADD", self.relays))
                self.sock.sendall(bound_relays)
                self.sock.close()
            except:
                self.relays.remove(relay)



    def broadcast(self, signal):
        if signal not in BEACON_SIGNALS:
            raise Exception("Incorrect signal")


        for relay in self.relays:
            try:
                self.sock.connect(tuple(relay.split(":")))
                bound_bc = pickle.dumps((signal, self.bc))
                self.sock.sendall(bound_bc)
                self.sock.close()
            except:
                print(f"Failed to connect to relay {relay}.")




    def update_chain(self, block : Block):
        if not self.bc:
            raise Exception("No chain to update.")

        self.bc.add_block(block)




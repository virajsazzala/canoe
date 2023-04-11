from src.chain.Block import Block
from src.network.Node import Node
from src.Consts import *

import socket
import pickle


class Relay(Node):
    def __init__(self):
        super().__init__()
        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.beacon = None

    def connect(self, server) -> bool:
        if self.beacon:
            return False

        self.sock.connect(server)
        return True

    def stream(self, mode, data):
        if mode not in STREAM_MODES:
            raise Exception("Incorrect mode")

        if not Relay.validate_stream_mode(mode, data):
            raise Exception("Data does not match mode.")

        package = (mode, data)
        self.sock.sendall(pickle.dumps(package))

    @staticmethod
    def validate_stream_mode(mode, data) -> bool:
        if (mode == "MINT" and isinstance(data, Block)) or (mode == "VALIDATE" and isinstance(data, bool)):
            return True

        return False

    def acquire(self):
        pass

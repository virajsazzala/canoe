'''
Server/Center -> host bc, send events
Clients -> wrapper of a node, recieve events and relay them back to server.
Figure out running clients locally as well as across a network.
'''

import socket

from src.network.Node import Node
from src.network.Relay import Relay


class Network:
    def __init__(self):
        relays = [Relay() for _ in range(10)]


    @staticmethod
    def register_node(self, node: Node):
        pass

    def broadcast(self):
        pass

    def update_chain(self):
        pass

    def recieve_event(self):
        pass

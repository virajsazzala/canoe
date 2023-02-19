import datetime as dt

from src.Utils import *

class Block:
    def __init__(self, id : int, timestamp, data, prevhash):
        self.id = id
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.hash = Utils.hashblock(self)

    @staticmethod
    def genesis():
        return Block(0,dt.datetime.now(), "Genesis", " ")

    @staticmethod
    def create_block(oldblock : Block, data):
        return Block(
            oldblock.id +1,
            dt.datetime.now(),
            data,
            oldblock.hash
        )


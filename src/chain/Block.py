import datetime as dt
import random

from src.Utils import *



class Block:
    """
    A representation of a Block.
    A new block is added to the blockchain every round.


    :param id        : Index ID of the block
    :param timestamp : Time at which block was created
    :param nonce     : Nonce value of the block, randomly generated
    :param data      : Data to be stored in the block
    :param prevhash  : Hash Value of the previous Block
    :param header    : Hashed value of the header of the block(id, timestamp, data, prevhash)
    :param hash      : Hashed value of the entire block including Nonce.

    """
    def __init__(self, id : int, timestamp, data, prevhash):
        self.id = id
        self.timestamp = timestamp
        self._nonce = 0
        self.data = data
        self.prevhash = prevhash
        self.header = Utils.hashblock(self,'header')
        self.hash = Utils.hashblock(self, 'nonce')

    @property
    def getnonce(self):
        return self._nonce

    @staticmethod
    def genesis():
        """
        Static Method to create Genesis Block

        :return : Block with Index 0
        """
        return Block(0,dt.datetime.now(), "Genesis", "0")

    @classmethod
    def create_block(cls, oldblock, data):
        """
        Create a new Block.

        :param oldblock : The previous Block
        :param data     : Data to be included in the block.

        :return         : Block dependent on oldblock
        """
        return cls(
            oldblock.id +1,
            dt.datetime.now(),
            data,
            oldblock.hash
        )

    def mine_block(self, difficulty):
        """
        Mine a block.
        
        :param difficulty : Specifies the number of places that should be filled with zeros
        """
        while(self.hash[:difficulty] != str('').zfill(difficulty)):
            self._nonce += 1
            self.hash = Utils.hashblock(self, 'nonce')
        
        print(f"Block mined and the hash is: {self.hash}")
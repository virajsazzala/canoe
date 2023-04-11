import hashlib
from src.Consts import *

class Utils:
    @staticmethod
    def hashblock(block, mode: str):
        if mode not in HASH_MODES:
            raise ValueError("Mode can be either header or nonce")
        enc = hashlib.sha256()

        enc.update(
            (str(block.id) +
            str(block.timestamp) +
            str(block.data) +
            str(block.prevhash)).encode()
        ) if mode == "header" else enc.update(
            (str(block.id) +
            str(block.timestamp) +
            str(block.data) +
            str(block.prevhash) +
            str(block.getnonce)).encode()
        )

        return enc.hexdigest()

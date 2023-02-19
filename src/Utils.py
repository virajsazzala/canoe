import hashlib
from src.Block import Block

class Utils:
    @staticmethod
    def hashblock(block: Block):
        enc = hashlib.sha256()
        enc.update(
            str(block.id) +
            str(block.timestamp) +
            str(block.data) +
            str(block.prevhash)
        )

        return enc.hexdigest()

from src.chain.Block import Block
from src.Utils import Utils


class Blockchain:
    def __init__(self):
        self.genesis = Block.genesis()
        self.chain = [self.genesis]
        self.height = len(self.chain)
        self.difficulty = 4


    @property
    def epoch(self):
        return self.height


    @property
    def lastblock(self):
        return self.chain[-1]


    def getBlock(self, index: int):
        return self.chain[index]


    def add_block(self, data):
        newBlock = Block.create_block(self.lastblock, data)
        newBlock.mine_block(self.difficulty)
        self.chain.append(newBlock)

    @property
    def getChain(self):
        return self.chain

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr_block = self.chain[i]
            prev_block = self.chain[i-1]
            
            if (curr_block.hash != Utils.hashblock(curr_block, "nonce")):
                print("Invalid Block!")
                return False
            
            if (curr_block.prevhash != prev_block.hash):
                print("Invalid Chain!")
                return False
        
        return True


    def print_chain(self):
        for i in self.chain:
            print(f"{i.id} : {i.data} : {i.hash} : {i.prevhash}\n")


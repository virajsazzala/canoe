from src.Block import Block

class Blockchain:
    def __init__(self):
        self.genesis = Block.genesis()
        self.chain = [self.genesis]
        self.height = len(self.chain)


    @property
    def epoch(self):
        return self.height


    @property
    def lastblock(self):
        return self.chain[-1]


    def getBlock(self, index: int):
        return self.chain[index]


    def add_block(self, data):
        self.chain.append(
            Block.create_block(self.lastblock, data)
        )

    @property
    def getChain(self):
        return self.chain

    def print_chain(self):
        for i in self.chain:
            print(f"{i.id} : {i.data} : {i.hash} : {i.prevhash}\n")


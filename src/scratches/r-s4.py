import pickle

from src.chain.Block import Block
from src.chain.Blockchain import Blockchain

bc = Blockchain()
bc.add_block(f"data 1")
bc.add_block(f"data 2")
bc.add_block(f"data 3")


d = ("MINT", bc.getBlock(1))


pd = pickle.dumps(d)

print(pd)

unpd = pickle.loads(pd)

print(unpd)
newb = unpd[1]
print(newb)

print(vars(newb))
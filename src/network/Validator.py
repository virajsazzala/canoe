from src.network.Node import Node
import random
class Validator(Node):
    """
    A Validator can vote when a block is broadcasted.
    Validator inherits from Node.
    """
    # In CANOE, a node is a validator by default if it is new.
    def __init__(self, isNew=False):
        super().__init__(isNew)
        
    def vote(self):
        """
        Validates the broadcasted block.

        :return : a boolean value
        """
        value = random.randint(0, 100)
        return value < self.error_prob
        
        

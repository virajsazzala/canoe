import random
from src.Utils import Utils
from src.network.Node import Node

class ProofOfStake:
    '''
    A selection process that uses Coin Age selection.

    :param nodes : The list of participating nodes.
    '''
    def __init__(self, nodes):
        self.nodes = nodes
    
    def get_staked_time(self):
        """
        The total amount of time for which the coins were staked.
        :TODO: now, the staked_time is random, later calc it using epoch(checkpoints).
        """
        return random.randint(1, 5)
    
    def get_coin_age(self, node):
        """
        Generate coin_age for each node, where coin_age = stake * staked_time

        :param node : A single node from the participating nodes.

        :return : the coin age of the node.
        """
        return node.stake * self.get_staked_time()
    
    def set_coin_age(self):
        """
        Assigns coin age for all the participating nodes.
        """
        for node in self.nodes:
            node.coin_age = self.get_coin_age(node)


    def choose_validator_node(self):
        """
        Chooses a random node but the higher the coin age, the higher the chance of getting picked.

        :return : a list of validator nodes.
        """
        sorted_nodes = self.nodes

        self.set_coin_age()
        total_coin_ages = sum(node.coin_age for node in self.nodes)
        r_num = random.uniform(0, total_coin_ages)
        for node in self.nodes:
            if r_num <= node.coin_age:
                return node
            r_num -= node.coin_age
        return self.nodes
        
    # for simulation
    def get_avg_error_prob(self):
        sum = 0
        for node in self.nodes:
            sum += node.error_prob
        
        return sum/len(self.nodes)
    
    
import random
import datetime as dt


class Node:
    """
    A representation of a Node.
    A node can be a part of the Validators class if all the requirements are met.

    :param joined_on        : the data and time of the creation of Node
    :param rank             : the rank of the node on the rank chart
    :param error_prob       : the probability of invalidation (%)
    :param last_validation  : the time of the most recent validation
    :param processed_blocks : a list of all the previously validated blocks
    """
    def __init__(self, isNew=False):
        self.joined_on = dt.datetime.now()
        self.rank = 0
        self.processed_blocks = []
        self.stake = random.randint(0, 1000)
        self.coin_age = 0
        self.error_prob = 0 if isNew else random.randint(0, 100)

    def validation_frequency(self, blockchain):
        """
        A node has higher frequency if a node participates regularly in the validation process.
        
        :param blockchain : the main blockchain's chain

        :return : an integer representing the average distance between all processed blocks 

        Note: smaller return value == Higher frequency
        """

        # main chain
        chain = blockchain.getChain

        # check only the last 10 processed blocks or under
        if len(self.processed_blocks) > 10:
            recent_validations = self.processed_blocks[-10:]
        else:
            recent_validations = self.processed_blocks[:]
        
        # calculate the distance between each processed block, by referring to main chain
        distances = []
        for i in range(len(recent_validations) - 1):
            block_index = chain.index(recent_validations[i])
            next_block_index = chain.index(recent_validations[i+1])
            distances.append(next_block_index - block_index)
        
        # average of the distances to find the frequency
        frequency = sum(distances) / len(distances)

        return frequency

    def update_rank(self, rank):
        """
        :param rank : new updated rank
        """
        self.rank = rank

    def add_processed_block(self, processed_block):
        """
        add newly processed blocks by the node

        :param processed_block : the block that has been processed by the node
        """
        self.processed_blocks.append(processed_block)
        
    def is_eligible(self, criteria):
        """
        a node is eligible if they have a specified min rank or
        if they are new to the network

        :param criteria : a dictionary of eligible criteria with keys - min_rank
        
        :return : a boolean value True or False 
        """
        return self.rank > criteria["min_rank"] or self.rank == 0

    def print_node(self):
        print(f"Joined On: {self.joined_on}\nRank: {self.rank}\nProbability Of Error: {self.error_prob}\nCoin Age: {self.coin_age}\nStake: {self.stake}\nProcessed Block: {self.processed_blocks}")
        
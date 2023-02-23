import random
import datetime as dt

class Node:
    """
    A representation of a Node
    A node can be a part of the Validators class if all the requirements are met

    :param joined_on       : the data and time of the creation of Node
    :param rank            : the rank of the node on the rank chart
    :param error_prob      : the probability of invalidation
    :param last_validation : the time of the most recent validation
    """
    def __init__(self, rank: int, last_validation):
        self.joined_on = dt.now()
        self.rank = rank
        self.error_prob = random.randint(0, 100)
        self.stake = random.randint(0, 1000)
        self.last_validation = last_validation
        
    def is_eligible():
            pass     
        
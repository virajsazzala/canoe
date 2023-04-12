class ProofOfPotential:
    def __init__(self, nodes, blockchain):
        self.nodes = nodes
        self.blockchain = blockchain

    def rank_nodes(self):
        """
        Each Node is sorted based on its importance. Here, error_prob has the highest importance,
        followed by regularity and then stake.

        :return : a list of ranked nodes.
        """

        # sorting nodes based on importance.
        sorted_nodes = sorted(self.nodes, key=lambda node: (node.error_prob, node.validation_frequency(self.blockchain), -node.stake))

        # assign ranks to nodes (if regularity == 0, assign high score to rank last)
        rank = 1
        for i in range(len(sorted_nodes)):
            node = sorted_nodes[i]
            if node.validation_frequency(self.blockchain) == 0:
                regularity_score = 99999
            node.rank = rank
            rank += 1

        return sorted_nodes
    
    def select_top_n_nodes(self, best_perc, new_perc):
        """
        The ranked nodes are split into two categories:
            1. New nodes - The new nodes in the network (regularity = 0)
            2. Best nodes - The highest ranked nodes (regularity > 0)
        
        Then, a certain percentage of these nodes are selected for the final validation process

        :param best_perc : the percentage of nodes selected from the best nodes category.
        :param new_perc  : the percentage of node selected from the new nodes category.

        :return : a list of nodes selected for validation process. 
        """

        nodes = self.rank_nodes()

        # calculate the number of nodes to be selected based on given percentage
        num_of_best = int((best_perc / 100) * len(nodes))
        num_of_new = int((new_perc / 100) * len(nodes))
        
        # get the list of new nodes
        new_nodes = []
        for node in nodes:
            if node.validation_frequency(self.blockchain) == 0:
                new_nodes.append(node)
                nodes.remove(node)
        
        # sort based on ranks
        best_nodes = sorted(nodes, key=lambda node: (node.rank))[:num_of_best]
        new_nodes = sorted(new_nodes, key=lambda node: (node.rank))[:num_of_new]

        best_nodes.extend(new_nodes)

        # reassign ranks
        rank = 1
        for node in best_nodes:
            node.rank = rank
            rank += 1
        
        return best_nodes


        


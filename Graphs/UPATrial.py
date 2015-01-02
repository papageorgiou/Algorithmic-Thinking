# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 13:36:35 2014

@author: Alex
"""

"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list 
     for each trial.
    """

    def __init__(self, num_nodes_m):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes_m = num_nodes_m
        self._node_numbers_ratio = [node for node in range(num_nodes_m) for dummy_idx in range(num_nodes_m)]


    def run_trial(self, m_new_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """ 
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(m_new_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers_ratio))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers_ratio.append(self._num_nodes_m)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers_ratio.append(self._num_nodes_m)
        self._node_numbers_ratio.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes_m += 1
        return new_node_neighbors

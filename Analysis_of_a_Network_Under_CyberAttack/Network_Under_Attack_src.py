# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 10:16:43 2014 @author: Alex

Algorithmic Thinking -"Analysis of a computer network: Computing the resilience of a network 
under cyber-attack"
"""
import random

def ER_undir(num_nodes, prob):
    '''
    Generates random undirected graphs (ER algorithm). 
    Takes as input: 
    -an integer for the number of nodes
    -a float for the probability of a node to node connection.
    
    Return: a dictionary where each node is linked to its adjacent nodes
    '''
    
    graph={}     
    nodes_list=range(num_nodes)

    for node in nodes_list:
        for  possible_neighbor in range(node + 1, num_nodes):                                                           
            if random.random() < prob:                                
                try:
                    graph[node].append(possible_neighbor)
                except KeyError:
                    graph[node]=[]
                    graph[node].append(possible_neighbor)
                try:
                    graph[possible_neighbor].append(node)
                except KeyError:
                    graph[possible_neighbor]=[]
                    graph[possible_neighbor].append(node)
                
        
    return graph
#ER_undir(6,0.5)


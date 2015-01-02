# -*- coding: utf-8 -*-

import random

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
    
    Returns: a dictionary where each node is linked to its adjacent nodes
    '''
    
    graph={}     
    nodes_list=range(num_nodes)

    for node in nodes_list:
        for  potential_neighbor in range(node + 1, num_nodes):                                                           
            if random.random() < prob:                                
                try:
                    graph[node].append(potential_neighbor)
                except KeyError:
                    graph[node]=[]
                    graph[node].append(potential_neighbor)
                try:
                    graph[potential_neighbor].append(node)
                except KeyError:
                    graph[potential_neighbor]=[]
                    graph[potential_neighbor].append(node)
                
        
    return graph

def ER_undir2 (num_nodes, prob):
    '''
    Generates random undirected graphs (ER algorithm). 
    Takes as input: 
    -an integer for the number of nodes
    -a float for the probability of a node to node connection.
    
    Returns: a dictionary where each node is linked to its adjacent nodes
    '''
    
    graph={}     
    nodes_list=range(num_nodes)

    for node in nodes_list:
        for  potential_neighbor in range(node + 1, num_nodes):                                                           
            if random.random() < prob:                                
                try:
                    graph[node].add(potential_neighbor)
                except KeyError:
                    graph[node]=set([])
                    graph[node].add(potential_neighbor)
                try:
                    graph[potential_neighbor].add(node)
                except KeyError:
                    graph[potential_neighbor]=set([])
                    graph[potential_neighbor].add(node)
                
        
    return graph
    
def ER_undir3(num_nodes, prob):
    '''
    Generates random undirected graphs (ER algorithm). 
    Takes as input: 
    -an integer for the number of nodes
    -a float for the probability of a node to node connection.
    
    Returns: a dictionary where each node is linked to its adjacent nodes
    '''
    
   
    nodes={node for node in range(num_nodes)}
    ugraph={node:set() for node in nodes}
   
    for node_i in nodes:
        for node_j in nodes:
            if node_i!= node_j:
                probability=random.random()
                if probability<prob:
                    ugraph[node_i].add(node_j)
                    ugraph[node_j].add(node_i)
                   
    return ugraph   


            
def ER_undir4(num_nodes, prob):
    '''
    Generates random undirected graphs (ER algorithm). 
    Takes as input: 
    -an integer for the number of nodes
    -a float for the probability of a node to node connection.
    
    Returns: a dictionary where each node is linked to its adjacent nodes
    '''       
#    graph={}     
#    nodes_list=range(num_nodes)
    nodes_list=range(num_nodes)
    graph={node:set() for node in nodes_list}

    for node in nodes_list:
        for  potential_neighbor in range(node + 1, num_nodes):                                                           
            if random.random() < prob:                                
                graph[node].add(potential_neighbor)
                graph[potential_neighbor].add(node)
    return graph
    
        
    


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

def UPAgraph(final_node_nbr, exist_nodes_conn):
    
    graph=make_complete_graph(exist_nodes_conn)
     
    m=exist_nodes_conn
    n=final_node_nbr
    
    for node_id in range(m,n):
        graph[node_id]=set([])
        
    UPA=UPATrial(m)
    
    for node in range(m, n):
        nodes_to_con=UPA.run_trial(m)
        graph[node]=nodes_to_con
        for old_node in nodes_to_con:
            graph[old_node].add(node)
        
    return graph 

def make_complete_graph(num_nodes): 

    '''
    Takes the number of nodes, returns a dictionary
    corresponding to a complete directed graph with the specified number of nodes. 
    
    A complete graph contains all possible edges subject to the restriction that self-loops are not allowed. 
    The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive. Otherwise, the function 
    returns a dictionary corresponding to the empty graph. 
    '''
    
    dict2g={}
    nodes=[]
    if num_nodes<=0:
        return dict2g
    else: 
        for nod in range(num_nodes):
            nodes.append(nod)
    for nod in nodes:
        nodes2=nodes[:]
        nodes2.remove(nod)
        dict2g[nod]=set(nodes2)
    return dict2g

# Code for loading computer network graph
# general imports

import urllib2
import random
import time
import math

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

#GR1300=load_graph(NETWORK_URL)

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph
    
def  load_offline(graph_file):
    
    ugraph={}
    
    graph=open(graph_file, 'r')
    for line in graph.readlines():
        line= line[:-1]
        neighbors= line.split(' ')
        node=int(neighbors[0])
        ugraph[node] = set([])
        for neighbor in neighbors[1 : -1]:
                ugraph[node].add(int(neighbor))

    return ugraph           
            
    
def random_order(ugraph):
    '''
    takes as input an undirected graph and returns a list of the nodes in the 
    graph in some random order
    '''
    all_nodes= ugraph.keys()   
    random.shuffle(all_nodes)
    return all_nodes
    


from collections import deque
    

def bfs_visited(ugraph, start_node):
    '''
    Takes the undirected graph ugraph 
    and the node start_node and returns the set consisting of all nodes
    that are visited by a breadth-first search that starts at start_node
     '''
    
    queue=deque([start_node])
    visited=set([start_node])
    while queue: 
        jay_node=queue.popleft()
        for neighbor in ugraph[jay_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


import random 



def cc_visited(ugraph):
    
    '''
    Takes the undirected graph ugraph and returns
    a list of sets, where each set consists of all the nodes 
    in a connected component, and there is exactly one set in the list 
    for each connected component in ugraph and nothing else.
    

    '''
    nd_remain=ugraph.keys() 
    con_comp=[]   
    while nd_remain:
        rand_i=random.choice(nd_remain)
        setw=bfs_visited(ugraph, rand_i)
        con_comp.append(setw)
        for node in setw:      
            nd_remain.remove(node)
    return con_comp 
    


def largest_cc_size(ugraph):
    
    '''
    Takes the undirected graph ugraph and returns the size 
    (an integer) of the largest connected component in ugraph.
    '''
    
    cc_setslist=cc_visited(ugraph)
    lengths=[len(cc_set) for cc_set in cc_setslist]
    if len(lengths)>0:
        return max(lengths)
    else:
        return 0
    



def compute_resilience(ugraph, attack_order):
    '''
    Takes the undirected graph ugraph,
    a list of nodes attack_order and iterates through the nodes in attack_order. 
    For each node in the list, the function removes the given node and its edges 
    from the graph and then computes the size of the largest connected component 
    for the resulting graph.
    The function should return a list whose k+1th entry is the size of the largest
    connected component in the graph after the removal of the first k nodes in attack_order. The first entry (indexed by zero) is the size of the largest connected component in the original graph.

    '''
    size_full=largest_cc_size(ugraph)
    list_sizes=[size_full]
    for node in attack_order:
        
        for star in ugraph:
            ugraph[star]=ugraph[star] - set([node])
        try:
            del ugraph[node]
        except KeyError: continue
        list_sizes.append(largest_cc_size(ugraph))
    return list_sizes
    
def compute_resilience2(ugraph, attack_order):
    """
    Input:
        an undirected graph
        a list of nodes attack_order
    Output:
        a list of connected components
    """
    components = []
    components.append(largest_cc_size(ugraph))
    for node in attack_order:
        if node in ugraph.keys():
            for edge in ugraph[node]:
                ugraph[edge].remove(node)
            ugraph.pop(node)
            components.append(largest_cc_size(ugraph))

    return components
    
###resilience_of_graphs:
    
    ER=ER_undir4(1347, 0.0035)
    UPA=UPAgraph(1347, 2)
    GR1300=load_graph(NETWORK_URL)
    
    GR1300=load_offline("alg_rf7.txt")

    
    resER=compute_resilience(ER, random_order(ER))
    resUPA=compute_resilience(UPA, random_order(UPA))
    resGR=compute_resilience(GR1300, random_order(GR1300))
####

import matplotlib.pyplot as plt

def compute_edges(ugraph):
    '''
    computed edges of undirected graph
    '''
    counter=0
    for node_set in ugraph.values():
        counter+=len(node_set)
    res=counter/2
    return res
        


def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph       


def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

def  fast_targeted_order1(ugraph):
    '''
    Compute a targeted attack order consisting of
    nodes of maximal degree.
    
    '''
    degree_set=[]
    for i in range(len(ugraph)):
        degree_set.insert(i, set([]))
    for node in ugraph:
        degree_set[len(ugraph[node])].add(node)
    order_list=[]
    count=0
    for k in range(len(ugraph)-1,-1, -1):
        while degree_set[k]:
            u=random.choice(list(degree_set[k]))
            degree_set[k].remove(u)
            for neighbor in ugraph[u]:
                    d=len(ugraph[neighbor])
                    degree_set[d-1].add(neighbor)
            order_list.insert(count,u)
            count=count+1
            
            delete_node(ugraph, u)
    
    return order_list       
    

def plot_graphs():
    """
    Plot an example with two curves with legends
    """
    xvals = range(1348)
    yvals1 = resER
    yvals2 = resUPA
    yvals3 = resGR
    
    plt.plot(xvals, yvals1, '-b', label='ER with p=0.0035')
    plt.plot(xvals, yvals2, '-r', label='UPA with m=2')
    plt.plot(xvals, yvals3, '-g', label='GR')
    plt.legend(loc='upper right')
    plt.show()    


    


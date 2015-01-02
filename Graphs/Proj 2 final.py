"""
Created on Thu Sep 11 13:13:28 2014

@author: Alex
"""

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

#GRAPH5 = {0: { 2, 3, 4},
# 1: {},
# 2: {0, 3, 4},
# 3: {0, 2, 4},
# 4: {0, 2, 3}}
##
#bfs_visited(GRAPH5, 2)

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
        del ugraph[node]
        list_sizes.append(largest_cc_size(ugraph))
    return list_sizes


#   ...max arg error
#cc_visited(GRAPH5) 
#
#GRAPH5 = {0: { 2, 4,5},
# 2: {0, 5, 4},
# 5: {0, 2, 4},
# 4: {0, 2, 5}}   
#   
#bfs_visited(GRAPH5, 4)
#cc_visited(GRAPH5)
#largest_cc_size(GRAPH5)
#compute_resilience(GRAPH5, [2,4]) 
#largest_cc_size(GRAPH5)

    
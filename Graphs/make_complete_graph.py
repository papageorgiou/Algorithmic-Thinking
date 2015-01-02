'''
project 1
'''

def make_complete_graph(num_nodes): 

    '''
    Takes the number of nodes, returns a dictionary
    corresponding to a complete directed graph with the specified number of nodes. 
    
    A complete graph contains all possible edges subject to the restriction that self-loops are not allowed. 
    The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive. Otherwise, the function 
    returns a dictionary corresponding to the empty graph. 
    '''
    
    graph={}
    nodes_list=[]
    if num_nodes<=0:
        return graph
        
    else: 
        for nod in range(num_nodes):
            nodes_list.append(nod)
    for nod in nodes_list:
        nodes2list=nodes_list[:]
        nodes2list.remove(nod)
        graph[nod]=set(nodes2list) 
    return graph
          
   
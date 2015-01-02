from UPATrial import*
from make_complete_graph import*

#add an indirected edge to the ups wherever you added a directed to the dpa

def UPAgraph(final_node_nbr, exist_nodes_conn):
    
    graph=make_complete_graph(exist_nodes_conn)
     
    m=exist_nodes_conn
    n=final_node_nbr
    
    for node_id in range(m,n):
        graph[node_id]=set([])
        
    UPA=UPATrial(m)
    
    for node in range(m, n):
        #DPA=DPATrial(node)
        nodes_to_con=UPA.run_trial(m)
        graph[node]=nodes_to_con
        for old_node in nodes_to_con:
            graph[old_node].add(node)
        
    return graph 
        
#    
#UPAgraph(10, 3)   
#
#L={1:[2,3], 4:[5,6]}
#G={2.3, 2.4}
#
#L[1].extend(G)
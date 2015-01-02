import random


def ER(n, p):
    
    graph={}     
    V=range(n)
           
    for i in V:
        graph[i]=[]
         
        for j in V:
            if i!=j:
                                
                a=random.random()                                
                if a < p:
                    graph[i].append(j)                                            
    return graph         

import random
            
                    
def ER_undir(n,p):
    graph={}     
    V=range(n)

    for i in V:
        for  j in range((i+1), len(V)):                                                           
            if random.random() < p:                
                
                try:
                    graph[i].append(j)
                except KeyError:
                    graph[i]=[]
                    graph[i].append(j)
                try:
                    graph[j].append(i)
                except KeyError:
                    graph[j]=[]
                    graph[j].append(i)
                
        
    return graph
    
C=ER_undir(6,0.5)
    

    
import itertools

L=[1,2,3,4]
C=itertools.combinations(L, 2)
itertools.combinations([1,2,3], 2)   



range(6)  

L=[1,2,3,4]
type(L)

def itera(List):
    K=[]
    for i in List:
        for j in range(i+1, len(List)):
            
            K.append({i,j})
            
    return K
itera(L)

V=range(10)
V
len(V)

range(1, 10)





        
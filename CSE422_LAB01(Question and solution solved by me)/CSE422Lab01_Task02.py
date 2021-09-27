# -*- coding: utf-8 -*-
"""


@author: Simon Biswas
"""

f=open('input2.txt',mode='r')
f=f.readlines()
edge=int(f[1]) # total connections
w=len(f)
lara=int(f[w-1]) # position of lina
nora=int(f[w-2]) # position of nora
lina=int(f[w-3]) # position of lina

graph={}
for i in range(2,2+edge):
    p=f[i].strip().split()
    p1,p2=p
    p3=int(p1)
    p4=int(p2)
    if p3 not in graph.keys():
        graph[p3]=list()
    graph[p3].append(p4)




def bfs_modified(graph, start, end):
    visited = []     
    queue = [[start]] #sub-graph
    
    if start == end:
     
        return start
    
    while queue:
        p = queue.pop(0) # slicing sub-graph/queue
        con = p[-1] # connected nodes of start node  ; con=connected
        
        if con not in visited:
            n = graph[con] # getting connected edged-nodes of con family

            for i in n:
                new_p = list(p)
                new_p.append(i)
                queue.append(new_p)
                
 
                if i == end:
                    
                    return len(new_p)-1
                  
            visited.append(con)

nora_move=bfs_modified(graph,nora,lina) # total moves of Nora
lara_move=bfs_modified(graph,lara,lina) # total moves of Lara

if nora_move<lara_move:  print("Winner:","Nora")
elif nora_move>lara_move: print("Winner:","Lara")
else: print("Both reached at the same time")


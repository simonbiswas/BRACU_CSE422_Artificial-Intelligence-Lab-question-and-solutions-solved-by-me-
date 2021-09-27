# -*- coding: utf-8 -*-
"""


@author: Simon Biswas 
"""

f=open('input3.txt',mode='r')
f=f.readlines()
c=int(f[0])
edge=int(f[1]) # total connections
w=len(f)
lina=int(f[2+edge-1])
participants=int(f[2+edge])
k=list()
for i in range(2+edge+1,w):
    k.append(int(f[i]))

graph={}
for i in range(2,2+edge-1):
    p=f[i].strip().split()
    p1,p2=p
    p3=int(p1)
    p4=int(p2)
    if p4 not in graph.keys():
        graph[p4]=list()
    graph[p4].append(p3)

m=list()

def bfs_modified(graph, start,k):
    for i in k:
       visited = []     
       queue = [[start]] #sub-graph
    
    
       while queue:
           p = queue.pop(0) # slicing sub-graph/queue
           con = p[-1] # connected nodes of start node  ; con=connected
        
        
           if con not in visited :
               n = graph[con] # getting connected edged-nodes of con family

               for j in n:
                  new_p = list(p)
                  new_p.append(j)
                  queue.append(new_p)
                
                  if i == j:

                   
                      m.append(len(new_p)-1)
                      visited.clear()
                      queue.clear()
                      new_p.clear()
                      
   
bfs_modified(graph, lina,k) # bfs_modified method has been called only once
print(min(m))
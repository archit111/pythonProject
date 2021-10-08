from collections import  defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addedge (self, u , v):
        self.graph[u].append(v)

    def transpose (self):
        for i in self.graph:
            for j in self.graph[i]:
                print (j , "-->", i)

    def bfs (self,v,visited,q):
        q.append(v)
        visited[v]=True
        while (len(q)>0):
            x=q.pop()
            print (x,end=" ")
            for i in self.graph[x]:
                if visited[i]==False:
                    visited[i]=True
                    q.append(i)

    def dfs(self,v,visited):
        print(v,end=" ")
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                visited[i]=True
                self.dfs(i,visited)

    def adjacent_edges(self):
        for i in self.graph:
            for j in self.graph[i]:
                print (i,"-->",j)




g=Graph(4)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,3)
g.addedge(3,2)
g.addedge(2,1)

'''g.transpose()'''
q=[]
visited=[False]*4
'''g.bfs(0,visited,q)'''
'''g.dfs(0,visited)'''
g.transpose()


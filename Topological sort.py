from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def indegree(self,s,indegree):
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j]=indegree[j]+1

    def topologicalsort(self,indegree,q):
        for i in range (self.v):
            if indegree[i]==0:
                q.append(i)
        li=[]

        while (q):
            x=q.pop(0)
            li.append(x)
            for i in self.graph[x]:
                indegree[i]=indegree[i]-1
                if indegree[i]==0:
                    q.append(i)
        return li


g=Graph(5)
g.addedge(0,2)
g.addedge(0,3)
g.addedge(1,3)
g.addedge(1,4)
g.addedge(2,3)

indegree=[0]*5
g.indegree(0,indegree)
q=[]
print(g.topologicalsort(indegree,q))

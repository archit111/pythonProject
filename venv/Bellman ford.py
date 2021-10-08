from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    def addedge(self,u,v,w):
        self.graph.append([u,v,w])

    def bellmanford(self,s):
        dis=[float("inf")]*self.V
        dis[s]=0
        for i in range (self.V-1):
            for u,v,w in self.graph:
                if dis[u]!=float("inf") and dis[v]>dis[u]+w:
                    dis[v]=dis[u]+w


        self.printgraph(dis)
    def printgraph(self,dis):
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dis[i]))




g=Graph(4)
g.addedge(0,1,1)
g.addedge(0,2,4)
g.addedge(1,2,-3)
g.addedge(1,3,2)
g.addedge(2,3,3)

g.bellmanford(0)

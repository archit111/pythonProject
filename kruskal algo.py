from collections import defaultdict
class Graph:

    def __init__(self,vertices):
        self.v=vertices
        self.graph=[]
    def addedges(self,u,v,w):
        self.graph.append([u,v,w])

    def findpath(self,parent,i):
        if parent[i]==i:
            return i
        else:
            return self.findpath(parent,parent[i])
    def union(self,parent,x,y):
        xroot=self.findpath(parent,x)
        yroot=self.findpath(parent,y)

        parent[xroot]=yroot

    def Kruskal_MST(self):
        self.graph=sorted(self.graph,key=lambda x:x[2])
        parent=[]
        result=[]
        rank=[]
        for node in range (self.v):
            parent.append(node)
            rank.append(0)
        e=self.v-1
        c=0
        i=0

        while (c<e):
            u, v, w = self.graph[i]
            i = i + 1
            x=self.findpath(parent,u)
            y=self.findpath(parent,v)

            if x!=y:
                c=c+1
                result.append([u,v,w])
                self.union(parent,x,y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)

    # Driver code
g = Graph(4)
g.addedges(0, 1, 10)
g.addedges(0, 2, 6)
g.addedges(0, 3, 5)
g.addedges(1, 3, 15)
g.addedges(2, 3, 4)

# Function call
g.Kruskal_MST()
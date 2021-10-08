import sys
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph = [[0 for column in range(v)]
                      for row in range(v)]

    def printMST(self,parent):
        print("Edge \tWeight")
        for i in range(1, self.v):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])



    def minkey(self,key,mstset):

        min=sys.maxsize
        for v in range (self.v):
            if key[v]<min and mstset[v]==False:
                min=key[v]
                min_index=v
        return min_index

    def primMST(self):

        key=[sys.maxsize]*self.v
        key[0]=0
        parent=[None] * self.v
        mstset=[False]*self.v
        parent[0]=-1
        for c in range(self.v):
            u=self.minkey(key,mstset)
            mstset[u]=True
            for v in range (self.v):
                if self.graph[u][v]>0 and mstset[v]==False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u

        self.printMST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.primMST();
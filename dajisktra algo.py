import sys
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for columns in range(vertices)]for rows in range (vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.v):
            print(node, "\t", dist[node])

    def minDistance(self,dist,sptSet):
        min = sys.maxsize

        for v in range (self.v):
            if min>dist[v] and sptSet[v]==False:
                min=dist[v]
                min_index =v
        return min_index


    def dajikstra(self,src):

        dist = [sys.maxsize] * self.v
        dist[src] = 0
        sptSet = [False] * self.v

        for i in range (self.v):

            u=self.minDistance(dist,sptSet)
            sptSet[u]=True
            for v in range(self.v):
                if self.graph[u][v]>1 and dist[v]>self.graph[u][v]+dist[u] and sptSet[v]==False:
                    dist[v]=self.graph[u][v]+dist[u]
        self.printSolution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]];

g.dajikstra(0);
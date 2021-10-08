class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[[0 for column in range(V)] \
                                for row in range(V)]

    def bipartite(self,src):
        colorArr=[-1]*self.V

        colorArr[src]=1
        queue=[]
        queue.append(src)

        while(queue):
            u=queue.pop(0)
            if self.graph[u][u]==1:
                return False

            for v in range(self.V):

                if self.graph[u][v]==1 and colorArr[v]==-1:
                    colorArr[u]=colorArr[v]+1
                    queue.append(v)

                if self.graph[u][v]==1 and colorArr[u]==colorArr[v]:
                    return False

        return True
g=Graph(4)
g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
            ]
if g.bipartite(0):
    print("Yes")
else:
    print("No")





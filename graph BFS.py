from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:

            s=queue.pop(0)
            print(s,end=" ")

            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

    def DFSUtil(self,s,visited):

        visited.append(s)
        print (s,end=" ")

        for i in self.graph[s]:
            if i not in visited:
                self.DFSUtil(i,visited)

    def DFS(self,s):

        visited=[]
        self.DFSUtil(s,visited)

g=Graph()
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,0)
g.add_edge(3,0)
g.add_edge(1,4)
g.add_edge(4,1)
g.add_edge(3,4)
g.add_edge(4,3)
g.add_edge(1,2)
g.add_edge(2,1)

#g.BFS(0)
g.DFS(0)


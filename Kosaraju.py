from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def fillorder(self,v,visited,st):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.fillorder(i,visited,st)
        st=st.append(v)

    def transpose (self):
        g=Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addedge(j,i)
        return g

    def defutil(self,x,visited):
        visited[x]=True
        print (x,end=" ")
        for i in self.graph[x]:
            if visited[i]==False:
                self.defutil(i,visited)

    def printSSC(self):
        visited=[False]*self.V
        stack=[]
        for i in range (self.V):
            if (visited[i]==False):
                self.fillorder(i,visited,stack)
        gr=self.transpose()

        visited=[False]*self.V
        while stack:
            x=stack.pop()
            if visited[x]==False:
                gr.defutil(x,visited)
                print(" ")


g=Graph(5)
g.addedge(1, 0)
g.addedge(0, 2)
g.addedge(2, 1)
g.addedge(0, 3)
g.addedge(3, 4)


g.printSSC()
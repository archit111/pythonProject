def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def isBipartite(adj,v,visited,color):

    for u in adj[v]:
        if (visited[u]==False):
            visited[u]=True

            color[u]=not color[v]
            if (not isBipartite(adj,u,visited,color)):
                return  False

        elif color[u]==color[v]:
            return False

    return True






if __name__=='__main__':

    N = 6

    # To maintain the adjacency list of graph
    adj = [[] for i in range(N + 1)]

    # To keep a check on whether
    # a node is discovered or not
    visited = [0 for i in range(N + 1)]

    # To color the vertices
    # of graph with 2 color
    color = [0 for i in range(N + 1)]

    # Adding edges to the graph
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 6)
    addEdge(adj, 6, 1)

    # Marking the source node as visited
    visited[1] = True

    # Marking the source node with a color
    color[1] = 0

    # Function to check if the graph
    # is Bipartite or not
    if (isBipartite(adj, 1, visited, color)):
        print("Graph is Bipartite")
    else:
        print("Graph is not Bipartite")


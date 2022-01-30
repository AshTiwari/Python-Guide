# connected components in undirected graphs.

def initalizeVertex():
    n = int(input('Enter the no. of vertices.\n'))
    for i in range(n):
        Vertex.append(i)
        adjacent[i] = []

def initalizeUndirectedEdges():
    n = int(input("Enter the no. of edges.\n"))
    print("Enter the space seperated edges.")
    for i in range(n):
        a,b = map(int,input().split())
        adjacent[a].append(b)
        adjacent[b].append(a) 

def showVertex():
    print('The vertexes are: ')
    print(vertex)
    print('\n')

def showEdges():
    print('The dictionary of edges are: ')
    print(adjacent)
    print('\n')

def dfs(s, connectedId):
    for neighbour in adjacent[s]:
        if visited[neighbour] == 0:
            visited[neighbour] = 1
            connectedComponents[neighbour] = connectedId
            dfs(neighbour, connectedId)
            

if __name__ == "__main__":
    adjacent = {}
    Vertex = []
    initalizeVertex()    
    initalizeUndirectedEdges()
    connectedComponents = [-1 for i in range(len(Vertex))]
    visited = [0 for i in range(len(Vertex))]
    connectedId = -1
    
    for v in Vertex:
        if visited[v] == 0:
            connectedId += 1
            visited[v] = 1
            connectedComponents[v] = connectedId
            dfs(v, connectedId)
    print('Connected Components Id is: {}'.format(connectedComponents))


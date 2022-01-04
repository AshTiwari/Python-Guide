#depth first search.

def initalizeVertex():
    n = int(input('Enter the no. of vertices.\n'))
    print("Enter the vertexes.")
    for i in range(n):
        vertex = input()
        Vertex.append(vertex)
        adjacent[vertex] = []

def initalizeUndirectedEdges():
    n = int(input("Enter the no. of edges.\n"))
    print("Enter the space seperated edges.")
    for i in range(n):
        a,b = input().split()
        adjacent[a].append(b)
        adjacent[b].append(a)

def initalizeDirectedEdges():
    n = int(input("Enter the no. of edges.\n"))
    print("Enter the space seperated edges.")
    for i in range(n):
        a,b = input().split()
        adjacent[a].append(b)    

def showVertex():
    print('The vertexes are: ')
    print(vertex)
    print('\n')

def showEdges():
    print('The dictionary of edges are: ')
    print(adjacent)
    print('\n')

def dfsRecursion(adjacent, parent, dfsOrder, start):
    for neighbour in adjacent.get(start, []):
        if neighbour not in parent.keys():
            parent[neighbour] = start
            dfsOrder.append(neighbour)
            dfsRecursion(adjacent, parent, dfsOrder, neighbour)
            
def dfs(adjacent, Vertex):   
    dfsOrder = []
    parent = {} 

    for v in Vertex:
        if v not in parent.keys():
            parent[v] = None
            dfsOrder.append(v)
            dfsRecursion(adjacent, parent, dfsOrder, v)
    return dfsOrder

if __name__ == "__main__":
    adjacent = {}
    Vertex = []
    initalizeVertex()
    initalizeUndirectedEdges()
    dfsOrder = dfs(adjacent, Vertex)
    print('DFS order is: ')
    print(dfsOrder)

# breadth first search.

def initalizeVertex():
    n = int(input('Enter the no. of vertices.\n'))
    for vertex in range(n):
        Vertex.append(vertex)
        adjacent[vertex] = []

def initalizeUndirectedEdges():
    n = int(input("Enter the no. of edges.\n"))
    print("Enter the space seperated edges.")
    for i in range(n):
        a,b = map(int,input().split())
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
    print(Vertex)
    print('\n')

def showEdges():
    print('The dictionary of edges are: ')
    print(adjacent)
    print('\n')

def bfs(root):
    frontier = [root]
    parent[root] = None
    level[root] = 0
    traversal = []
    while(len(frontier)):
        neighbour = []
        for parentVertex in frontier:
            for childVertex in adjacent[parentVertex]:
                if parent.get(childVertex) == None:
                    parent[childVertex] = parentVertex
                    level[childVertex] = level[parentVertex] + 1
                    neighbour.extend(adjacent[childVertex])
            traversal.append(parentVertex)
        frontier = neighbour.copy()

    print(traversal)
    print(parent)
    print(level)
    
if __name__ == "__main__":
    adjacent = {}
    Vertex = []
    level = {}
    parent = {}
    initalizeVertex()
    initalizeUndirectedEdges()
    bfs(0)


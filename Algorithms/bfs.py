# breadth first search.

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
    print(Vertex)
    print('\n')

def showEdges():
    print('The dictionary of edges are: ')
    print(adjacent)
    print('\n')

def bfs(adjacent, start = '0'):
    #start = str(start)
    current_level_nodes = []
    next_level_nodes = []
    level = {}
    parent = {}
    level[start] = 0
    parent[start] = None
    level_no = 1
    current_level_nodes.append(start)

    while current_level_nodes:
        next_level_nodes = []
        for u in current_level_nodes:
            for v in adjacent.get(u, []):
                if v not in level.keys():
                    level[v] = level_no
                    parent[v] = u
                    next_level_nodes.append(v)
        current_level_nodes = next_level_nodes.copy()
        level_no +=1    
    return level

if __name__ == "__main__":
    adjacent = {}
    Vertex = []
    initalizeVertex()
    initalizeUndirectedEdges()
    print('Implementing BFS.')
    level = bfs(adjacent)
    print(level)

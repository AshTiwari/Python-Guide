# topological sort

def initalizeVertex():
    n = int(input('Enter the no. of vertices.\n'))
    print("Enter the vertexes.")
    for i in range(n):
        vertex = input()
        Vertex.append(vertex)
        adjacent[vertex] = []

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

def t_sort(s, adjacent):
    global visited
    global topological_sort
    for neighbour in adjacent[s]:
        if neighbour not in visited.keys():
            visited[neighbour] = 1
            t_sort(neighbour, adjacent)
    topological_sort.append(s)      

def topologicalSort(adjacent):
    global visited
    global topological_sort
    topological_sort = []
    visited = {}
    for v in adjacent.keys():
        if v not in visited.keys():
            visited[v] = 1
            t_sort(v, adjacent)
    return topological_sort[::-1]


if __name__ == "__main__":
    adjacent = {'c':['a','b'], 'a':['d'], 'b':['d'], 'e':['a','d','f'], 'd':['h','g'], 'f':['j','k'], 'g':['i'], 'h':['i','j'],'k':['j'],'i':['l'], 'j':['m'], 'l':[], 'm':[]}
    top_sort = topologicalSort(adjacent)
    print('Topological sort order is: ')
    print(top_sort)


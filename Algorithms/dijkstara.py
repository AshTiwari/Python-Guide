#dijkstra algorithm

n = int(input('Enter the no. of vertices.\n'))
#a x-y pair represent a edge from x to y.
weight = [[0 for i in range(n+1)]for i in range(n+1)]

#stores the list of vertex.
Vertex = [i for i in range(n)]

#a key-value pair represent a vertex and all it's outward edges.
adjacent = {}
for i in range(n+1):
    adjacent[i] = []

def initalizeDirectedEdges():
    n = int(input("Enter the no. of edges.\n"))
    print("Enter the space seperated edges and weight.")
    for i in range(n):
        a,b,wht = map(int,input().split())
        weight[a][b] = wht
        adjacent[a].append(b)

def showVertex():
    print('The vertexes are: ')
    print(Vertex)
    print('\n')

def showEdges():
    print('The edges are: ')
    print(' ',end=' ')
    for i in range(n+1):
        print(str(i)+ ' ',end=' ')
    print('\n')
    for i in range(n+1):
        print(str(i) + ' ' + str(weight[i]))
    print('\n')

initalizeDirectedEdges()
showEdges()

# initalize data array with stores distance from source.
# each vertex is initalized at distance infinity:
data = [1000 for i in range(n)]
data[0]=0

q = [1000 for i in range(n)]
q[0]=0
# shortes path list:
shortest_path = []

for _ in range(n):
    u = q.index(min(q))
    q[u] = 1000
    shortest_path.append(u+1)
    for v in adjacent[u+1]:
        if data[v-1] > data[u]+weight[u+1][v]:
            data[v-1] = data[u] + weight[u+1][v]
            q[v-1] = data[v-1]


print(data)

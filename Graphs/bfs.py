# breadth first search

def initalizeVertex(Vertex, node_adjacency):
    n = int(input('Enter the no. of vertices.\n'))
    for vertex in range(n):
        Vertex.append(vertex)
        node_adjacency[vertex] = []

def initalizeUndirectedEdges(node_adjacency):
    n = int(input("Enter the no. of edges.\n"))
    print("Enter the space seperated edges.")
    for i in range(n):
        a,b = map(int,input().split())
        node_adjacency[a].append(b)
        node_adjacency[b].append(a)

def initalizeDirectedEdges(node_adjacency):
    n = int(input("Enter the no. of edges.\n"))
    print("Enter the space seperated edges.")
    for i in range(n):
        a,b = input().split()
        node_adjacency[a].append(b)    

def showVertex():
    print('The vertexes are: ')
    print(Vertex)
    print('\n')

def showEdges():
    print('The dictionary of edges are: ')
    print(node_adjacency)
    print('\n')

def bfs(node_adjacency, root):
    node_parent = {root:None}
    node_level = {root:0}
    current_level_nodes = [root]
    next_level_nodes = []
    current_level = 1
    while(current_level_nodes):
        for current_node in current_level_nodes:
            for child_node in node_adjacency[current_node]:
                if node_parent.get(child_node, -1) == -1:
                   node_parent[child_node] = current_node
                   next_level_nodes.append(child_node)
                   node_level[child_node] = current_level
        current_level_nodes = [node for node in next_level_nodes]
        next_level_nodes = []
        current_level += 1
    return node_level, node_parent

if __name__ == "__main__":
    Vertex = []
    node_adjacency = {}

    initalizeVertex(Vertex, node_adjacency)
    initalizeUndirectedEdges(node_adjacency)

    node_level, node_parent = bfs(node_adjacency, 0)
    print(f"Node Levels: {node_level}")
    print(f"Node Parent: {node_parent}")
    

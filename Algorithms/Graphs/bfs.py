# breadth first search.

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def addVertex(self, u):
        self.adjacency_list[u] = []

    def addUndirectedEdges(self, a, b):
        self.adjacency_list[a].append(b)
        self.adjacency_list[b].append(a)

    def addDirectedEdges(self, a, b):
        self.adjacency_list[a].append(b)    

    def showVertex(self):
        return self.adjacency_list.keys()

    def showEdges(self):
        return self.adjacency_list
           
    def bfs(self, start):
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
                for v in self.adjacency_list.get(u, []):
                    if v not in level.keys():
                        level[v] = level_no
                        parent[v] = u
                        next_level_nodes.append(v)
            current_level_nodes = next_level_nodes.copy()
            level_no +=1    
        return level, parent

if __name__ == "__main__":
    graph = Graph()
    graph.addVertex(0)
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addUndirectedEdges(0,1)
    graph.addUndirectedEdges(1,2)
    graph.addUndirectedEdges(1,3)
    graph.addUndirectedEdges(2,4)
    graph.addUndirectedEdges(3,4)
    print(graph.bfs(0))

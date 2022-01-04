# topological sort with breadth first search: Kahn's Algorithm.

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def addVertex(self, u):
        self.adjacency_list[u] = []

    def addDirectedEdges(self, a, b):
        self.adjacency_list[a].append(b)    

    def showVertex(self):
        return self.adjacency_list.keys()

    def showEdges(self):
        return self.adjacency_list
           
    def topBfs(self):
        V = len(self.adjacency_list)
        indegree = [0 for i in range(V)]
        for lst in self.adjacency_list.values():
            for vertex in lst:
                indegree[vertex] += 1 
        print(f'Indegree List: {indegree}')

        top_sort = [vertex for vertex, indeg_val in enumerate(indegree) if indeg_val == 0]
        next_level_nodes = []

        for i in range(V):
            # next line will give error if graph is not DAG.
            # for some i, top_sort[i] will give list index out of range.
            # can be avoided with tow data structure: a queue and top_sort_list.
            for neighbour in self.adjacency_list[top_sort[i]]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    top_sort.append(neighbour)
               
        return top_sort

if __name__ == "__main__":
    graph = Graph()
    graph.addVertex(0)
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addDirectedEdges(0,1)
    graph.addDirectedEdges(3,2)
    graph.addDirectedEdges(0,2)
    graph.addDirectedEdges(2,4)
    print(graph.topBfs())   

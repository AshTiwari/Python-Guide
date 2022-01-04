# shortest path on DAG
# handles negative edges.

from topological_sort import topologicalSort

def shortestPath(adjacent, edge_weight):
    topological_sort = topologicalSort(adjacent)
    start = topological_sort[0]
    distance = [float("inf") for i in range(len(adjacent))]
    distance[start] = 0
    parent = {start:None}
    for node in topological_sort:
        for neighbour in adjacent[node]:
            if distance[neighbour] > distance[node] + edge_weight[node][neighbour]:
                parent[neighbour] = node
                distance[neighbour] = distance[node] + edge_weight[node][neighbour]            
    return distance, parent

if __name__ == "__main__":
    adjacent = {0:[1,2], 1:[2,3,4], 2:[3,6], 3:[4,5,6], 4:[7], 5:[7], 6:[7], 7:[]}
    edge_weight = [[0,3,6,0,0,0,0],[0,0,4,4,11,0,0,0],[0,0,0,8,0,0,11,0],[0,0,0,0,-4,5,2,0],[0,0,0,0,0,0,0,9],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,0]]
    print(shortestPath(adjacent, edge_weight))

# Bellman Ford Single Source Shortest path.

def bellmanFordSP(adjacent, weight, V):
    shortest_dist = [float("inf") for i in range(V)]
    shortest_dist[0] = 0
    parent = {0: None}

    for iteration in range(V-1):
        for vertex in adjacent.keys():
            for neighbour in adjacent[vertex]:
                if shortest_dist[neighbour] > shortest_dist[vertex] + weight[vertex][neighbour]:
                    shortest_dist[neighbour] = shortest_dist[vertex] + weight[vertex][neighbour]
                    parent[neighbour] = vertex

    negCycleVertex = []
    for vertex in adjacent.keys():
        for neighbour in adjacent[vertex]:
            if shortest_dist[neighbour] > shortest_dist[vertex] + weight[vertex][neighbour]:
                shortest_dist[neighbour] = shortest_dist[vertex] + weight[vertex][neighbour]
                parent[neighbour] = vertex
                negCycleVertex.append(neighbour)
            
    for element in negCycleVertex:
        shortest_dist[element] = float("inf")
        
    return shortest_dist, parent

def bellmanFordNegCycle(adjacent, weight, V):
    shortest_dist = [float("inf") for i in range(V)]
    shortest_dist[0] = 0
    negCycle = False
    
    for iteration in range(V-1):
        for vertex in adjacent.keys():
            for neighbour in adjacent[vertex]:
                if shortest_dist[neighbour] > shortest_dist[vertex] + weight[vertex][neighbour]:
                    shortest_dist[neighbour] = shortest_dist[vertex] + weight[vertex][neighbour]

    for vertex in adjacent.keys():
        for neighbour in adjacent[vertex]:
            if shortest_dist[neighbour] > shortest_dist[vertex] + weight[vertex][neighbour]:
                negCycle = True
                break
                    
    return negCycle

if __name__ == "__main__":
    adjacent = {0:[1,6], 1:[1,2], 2:[3,4], 3:[5], 4:[5], 6:[4]}
    V = 7
    inf = float("inf")
    weight1 = [[inf,4,inf,inf,inf,inf,2], [inf,-1,3,inf,inf,inf,inf], [inf,inf,inf,3,1,inf,inf], [inf,inf,inf,inf,inf,-2,inf]]
    weight2 = [[inf,inf,inf,inf,inf,2,inf], [inf,inf,inf,inf,inf,inf], [inf,inf,inf,inf,2,inf,inf]]
    weight1.extend(weight2)
    weight = weight1
    shortest_dist, parent = bellmanFordSP(adjacent, weight, V)
    print(f"Shortest Distance: {shortest_dist}")
    print(f"Parent: {parent}")
    print("Check if Negative Cycle Exist.")
    print(bellmanFordNegCycle(adjacent, weight, V))
    

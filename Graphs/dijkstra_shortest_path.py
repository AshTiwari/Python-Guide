# Dijkstra's Algorithm

class Heap():
    def __init__(self, root):
        self.heap = [None]
        self.heap.append(root)
        self.lastIndex = 1		
    def push(self, element):
        self.heap.append(element)
        self.lastIndex += 1
        self.moveUp(self.lastIndex)
    def pop(self):
        if self.lastIndex < 1:
            return False
        highest = self.heap[1]
        self.heap[1] = self.heap[self.lastIndex]
        self.heap.pop()
        self.lastIndex -= 1 
        self.moveDown(1)
        return highest		

class MinHeap(Heap):
    def moveUp(self, index):
        if self.lastIndex < index:
            return False
        parent = index//2
        while parent > 0 and self.heap[parent][1] > self.heap[index][1]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            parent = index//2
        return True

    def moveDown(self, index):
        left = 2 * index 
        right = left + 1
        if self.lastIndex < left:
            return False
        elif self.lastIndex >= right:
            minimum = left if self.heap[left][1] < self.heap[right][1] else right
        elif self.lastIndex >= left:
            minimum = left
        if self.heap[index][1] > self.heap[minimum][1]:
            self.heap[index], self.heap[minimum] = self.heap[minimum], self.heap[index]
            self.moveDown(minimum)
        return True

def dijkstraWithArray(adjacent, weight, start):
    n = len(adjacent)
    shortest_dist = [float("inf") for i in range(n)]
    shortest_dist[0] = 0
    priority_queue = [(start,0)]
    parent = {start: None}
       
    while(priority_queue): #O(V)
        minimum_index = -1
        minimum_value = float("inf")
        for index,pair in enumerate(priority_queue): # Find minimum: O(V)
            if pair[1] < minimum_value:
                minimum_index = index
                minimum_value = pair[1]
        current_node = priority_queue[minimum_index][0]
        current_node_dist = priority_queue[minimum_index][1]
        priority_queue.pop(minimum_index)
        for node in adjacent[current_node]:         # append new pairs: O(E)
            if shortest_dist[node] > current_node_dist + weight[current_node][node]:
                parent[node] = current_node
                shortest_dist[node] = current_node_dist + weight[current_node][node]
                priority_queue.append((node, shortest_dist[node]))

    return(shortest_dist, parent)

def dijkstraWithHeap(adjacent, weight, start):
    n = len(adjacent)
    shortest_dist = [float("inf") for i in range(n)]
    shortest_dist[0] = 0
    minHeap = MinHeap((start,0))
    parent = {start:None}
       
    while(minHeap.lastIndex >= 1): 
        pair = minHeap.pop()                # V vertexes * lg(v) complexity = O(V*lg(V))
        current_node = pair[0]
        current_node_dist = pair[1]
        if shortest_dist[current_node] < current_node_dist:continue # skips outdated minDistance  
        for node in adjacent[current_node]:         # append new pairs: O(E)
            if shortest_dist[node] > current_node_dist + weight[current_node][node]:
                parent[node] = current_node
                shortest_dist[node] = current_node_dist + weight[current_node][node]
                minHeap.push((node, shortest_dist[node]))  # O(lg(V))

    return(shortest_dist, parent)

def dijkstraShortestPath(adjacent, weight, start, end):
    shortest_dist, parent = dijkstraWithHeap(adjacent, weight, start)
    current_node = end
    path = [current_node]
    total_dist = 0
    while(parent[current_node] != None):
        path.append(parent[current_node])
        current_node = parent[current_node]
    return path[::-1], shortest_dist[end]

if __name__ == "__main__":
    adjacent = {0:[1,2], 1:[2,3], 2:[1,3,4], 3:[4], 4:[3]}
    inf = float("inf")
    weight = [[inf,10,3,inf,inf],[inf,inf,1,2,inf],[inf,4,inf,8,2,inf],[inf,inf,inf,inf,7],[inf,inf,inf,9,inf]]
    dijkstraWithArray(adjacent, weight, 0)
    dijkstraWithHeap(adjacent, weight, 0)
    for i in range(1,5):
        path, dist = dijkstraShortestPath(adjacent, weight, 0, i)
        print(f"Path: {path}")
        print(f"Shortest Distance: {dist}")
        

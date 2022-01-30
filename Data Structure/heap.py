# implementing heap
from math import log

class Heap():
    def __init__(self, root):
        self.heap = [None]
        self.heap.append(root)
        self.lastIndex = 1
        
    def push(self, element):
        self.heap.append(element)
        self.lastIndex += 1
        self.moveUp(self.lastIndex)

    def peek(self, element):
        if self.lastIndex < 1:
            return None
        else:
            return self.heap[1]

    def pop(self):
        if self.lastIndex < 1:
            return False
        highest = self.heap[1]
        self.heap[1] = self.heap[self.lastIndex]
        self.heap.pop()
        self.lastIndex -= 1 
        self.moveDown(1)
        return highest      

    def printHeap(self):
        print(self.heap[1:])    

    def returnHeap(self):
        return self.heap[1:]

class MaxHeap(Heap):
    def moveUp(self, index):
        if self.lastIndex < index:
            return False
        parent = index//2
        while parent > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            parent = index//2
        return True

    def moveDown(self, index):
        left = 2 * index 
        right = left + 1
        if self.lastIndex < left:
            return False
        elif self.lastIndex >= right:
            maximum = left if self.heap[left] > self.heap[right] else right
        elif self.lastIndex >= left:
            maximum = left
        if self.heap[index] < self.heap[maximum]:
            self.heap[index], self.heap[maximum] = self.heap[maximum], self.heap[index]
            self.moveDown(maximum)
        return True


class MinHeap(Heap):
    def moveUp(self, index):
        if self.lastIndex < index:
            return False
        parent = index//2
        while parent > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            parent = index//2
        return True

    def moveDown(self, index):
        left = 2 * index 
        right = left + 1
        if self.lastIndex < left:
            return False
        elif self.lastIndex >= right:
            minimum = left if self.heap[left] < self.heap[right] else right
        elif self.lastIndex >= left:
            minimum = left
        if self.heap[index] > self.heap[minimum]:
            self.heap[index], self.heap[minimum] = self.heap[minimum], self.heap[index]
            self.moveDown(minimum)
        return True



    
if __name__ == "__main__":
    minheap = MinHeap(1)
    maxheap = MaxHeap(1)
    for i in [2,3,4,8,7,6,5]:
        minheap.push(i)
        maxheap.push(i)
    minheap.printHeap()
    maxheap.printHeap()
    for i in range(11):
        if i % 5 == 0:
            minheap.printHeap()
            maxheap.printHeap()
        minheap.pop()
        maxheap.pop()

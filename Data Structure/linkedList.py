# implement linked list.

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self):
		self.root = Node("Start")
		self.end = Node("None")
		self.root.next = self.end
		self.end.next = None	
		self.length = 0

	def addElementByNumber(self,number,data):
		if number <=0 or number>self.length+1:
			return 0
		newNode = Node(data)
		current_node = self.root.next
		previous_node = self.root
		i = 1
		while(number != i):
			previous_node = current_node
			current_node = current_node.next
			i = i + 1
		previous_node.next = newNode
		newNode.next = current_node		
		self.length +=1
		return 1
		

	def addElementToLeft(self,data):
		self.addElementByNumber(1,data)
		return 1

	def addElementToRight(self,data):
		self.addElementByNumber(self.length+1,data)
		return 1

# this function assumes that the element already exist.
	def deleteElementByData(self,data):
		if self.length == 0:
			return 0
		self.length =self.length - 1
		current_node = self.root.next
		previous_node = self.root
		while(current_node.data != data):
			previous_node = current_node
			current_node = current_node.next
		previous_node.next = current_node.next
		return 1
 		
	def deleteElementByNumber(self,number):
		if self.length == 0 or number <=0 or number>self.length:
			return 0
		current_node = self.root.next
		previous_node = self.root
		i = 1
		while(i != number):
			previous_node = current_node
			current_node = current_node.next
			i = i + 1
		previous_node.next = current_node.next		
		self.length -=1
		return 1

	def deleteFirstElement(self):
		self.deleteElementByNumber(1)
		return 1

	def deleteLastElement(self):
		self.deleteElementByNumber(self.length)
		return 1

	def traverseList(self):
		current_node = self.root
		while(current_node.next != None):
			print(f"{current_node.data} -> ",end = " ")
			current_node = current_node.next
		print("None")
		return 1

	def getLength(self):
#		print(f"Length = {self.length}")
		return self.length		

if __name__ == "__main__":
	linked_list = linkedList()
	for i in range(1,8):
		linked_list.addElementToLeft(i)
	linked_list.addElementToRight(0)
	linked_list.traverseList()
	linked_list.deleteElementByData(5)
	linked_list.traverseList()
	linked_list.deleteElementByNumber(3)
	linked_list.traverseList()
	linked_list.deleteFirstElement()
	linked_list.traverseList()
	linked_list.deleteLastElement()
	linked_list.traverseList()
	linked_list.addElementByNumber(1,7)
	linked_list.addElementByNumber(3,5)
	linked_list.addElementByNumber(4,4)
	linked_list.traverseList()
# Binary Search Tree

class bst:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class bstOpertaions:
    def insert(self, root, element):
        if root is None:
            return bst(element)
        if root.val == element:
            return root
        elif element < root.val:
            if root.left is None:
                root.left = bst(element)
                return bst(element)
            else:
                return self.insert(root.left, element)
        elif element > root.val:
            if root.right is None:
                root.right = bst(element)
                return root.right
            else:
                return self.insert(root.right, element)
            
    def search(self, root, element):
        if root is None:
            return None
        if root.val == element:
            return root
        elif element < root.val:
            return self.search(root.left, element)
        elif element > root.val:
            return self.search(root.right, element)

    def delete(self, root, element):
        if root == None:
            return None
        if root.val == element:
            print(1)
            if root.left == root.right == None:
                print(element,1)
                root = None
                return element
            elif root.left == None:
                print(element,2)
                root = root.right
                return element
            elif root.right == None:
                print(element,3)
                root = root.left
            elif root.right and root.left:
                print(element,4)
                successorNode = root.right
                while(successorNode.left):
                    successorNode = successorNode.left
                #print(successorNode.val)
                root.val = successorNode.val
                successorNode = None
                return element
        elif element < root.val:
            return self.delete(root.left, element)
        elif element > root.val:
            return self.delete(root.right, element)

    def inOrder(self, root):
        self.inOrderArray = []
        self.inOrderUtility(root)
        return self.inOrderArray
    
    def inOrderUtility(self, root):
        if root == None:
            return None
        self.inOrderUtility(root.left)
        self.inOrderArray.append(root.val)
        self.inOrderUtility(root.right)
        
    def preOrder(self, root):
        self.preOrderArray = []
        self.preOrderUtility(root)
        return self.preOrderArray
    
    def preOrderUtility(self, root):
        if root == None:
            return None
        self.preOrderArray.append(root.val)
        self.preOrderUtility(root.left)
        self.preOrderUtility(root.right)

    def postOrder(self, root):
        self.postOrderArray = []
        self.postOrderUtility(root)
        return self.postOrderArray
    
    def postOrderUtility(self, root):
        if root == None:
            return None
        self.postOrderUtility(root.left)
        self.postOrderUtility(root.right)
        self.postOrderArray.append(root.val)        

if __name__ == "__main__":
    bst1 = bst(50)
    opern = bstOpertaions()

    insertArray = [20, 30, 10, 0, 80, 60, 90, 40, 70]
    for i in insertArray:
        opern.insert(bst1, i)

    print(opern.inOrder(bst1))
    print(opern.preOrder(bst1))
    print(opern.postOrder(bst1))

    searchArray = [50, 0, 90, 40, 100]
    for i in searchArray:
        print(opern.search(bst1, i))
        
    deleteArray = [30, 0, 20, 900]
    for i in deleteArray:
        opern.delete(bst1, i)

    print(opern.inOrder(bst1))
    print(opern.preOrder(bst1))
    print(opern.postOrder(bst1))
    

''' Binary Search Tree
* Binary Search Tree are Binary Tree that have the following property
    * Values that are less than the parent are found in the left subtree
    * Values that are greater than the parent are found in the right subtree
    * This is known as the BST property
* Binary Search Trees are also one way to implement a MAP Abstract data type
    * Unique keys define where in the BST strucutre a Node gets inserted
    * And each node has a corresponding field value
    * Similar to how Python dicitionaries work on a high level, but the underlying implementation between a Python dicitonary
    and BST are different (each with pros/cons)
* Order of insertion matters as it affect the strucutre of the tree
'''

# Implmenting tree node
class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild # Python considers None value as False
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.rightChild and self.leftChild)
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    
# Implementing Binary Search Tree

class BinarySearchTree:
	def __init__(self):
		self.root = None # A BST just needs a reference to the root node
		self.size = 0 # Keeps track of number of nodes

	def length(self):
		return self.size

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root = TreeNode(key,val)
		self.size = self.size + 1

	# helper method to recursively walk down the tree
	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key,val,parent=currentNode)


	def get(self,key): # returns payload for key if it exists
		if self.root:
			res = self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	# helper method to recursively walk down the tree
	def _get(self,key,currentNode): 
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNode.rightChild)


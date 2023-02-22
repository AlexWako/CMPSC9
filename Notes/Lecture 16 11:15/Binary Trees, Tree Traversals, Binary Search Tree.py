''' Binary Tree Implementation
* So far, we've talked about binary trees on a conceptual level when analyzing sorting algorithms such as mergesort and quicksort
* We've talked about Binary heaps that can be conceptualized as a COMPLETE binary tree
* Nodes and References
    * Similar to our Linked List representation, we can expand upon this concept using nodes and references to construct our tree
    * Each node can be represented as an object
        * And each node will have references to other nodes in the tree
'''

# Binary Tree Implementation
class BinaryTreeNode:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        # Case 1: Node does not have a left child
        if self.leftChild == None:
            self.leftChild = BinaryTreeNode(newNode)
        else: # Case2: Node has a left child
            t = BinaryTreeNode(newNode)
            # links the left subtree
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        # Case 1: Node does not have a right child
        if self.rightChild == None:
            self.rightChild = BinaryTreeNode(newNode)
        else: # Case2: Node has a right child
            t = BinaryTreeNode(newNode)
            # links the right subtree
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key

# pytest
def test_createNode():
    node = BinaryTreeNode("A")
    assert node.getRootValue() == "A"
    assert node.getLeftChild() == None
    assert node.getRightChild() == None

def test_leftNode():
    node = BinaryTreeNode("A")
    node.insertLeft("B") # Case 1
    assert node.getLeftChild().getRootValue() == "B"
    assert node.getRootValue() == "A"
    assert node.getRightChild() == None
    assert node.getLeftChild().getRightChild() == None
    assert node.getLeftChild().getLeftChild() == None

def test_insertLeft():
    node = BinaryTreeNode("A")
    node.insertLeft("B")
    node.insertLeft("C")
    node.insertLeft("D")

    temp = node
    s = ""
    while temp != None:
        s = s + temp.getRootValue()
        temp = temp.getLeftChild()
    assert s == "ADCB"

''' Tree Traversals
* Sometimes we would want to vist all nodes in a tree 
* We can do this in various ways, and the order of visiting nodes may vary
* There are three common recursive ways to traverse nodes in a tree
    * Preorder
        * Visit the node first, then recursively go down the left subtree, then recursively go down the right subtree
    * Inorder
        * Recursively go down the left subtree, visit the node, then recursively go down the right subtree
    * Postorder
        * Recursively go down the left subtree, then recursively go down the right subtree, then visit the node
'''

# Implementation of preorder traversals
def preorder(tree):
    ret = ""
    if tree != None:
        ret += tree.getRootValue() # visit the node
        ret += preorder(tree.getLeftChild()) # go left
        ret += preorder(tree.getRightChild()) # go right
    return ret

# Implementation of inorder traversals
def inorder(tree):
    ret = ""
    if tree != None:
        ret += preorder(tree.getLeftChild()) # go left
        ret += tree.getRootValue() # visit the node
        ret += preorder(tree.getRightChild()) # go right
    return ret

# Implementations of postorder traversals
def postorder(tree):
    ret = ""
    if tree != None:
        ret += preorder(tree.getLeftChild()) # go left
        ret += preorder(tree.getRightChild()) # go right
        ret += tree.getRootValue() # visit the node
    return ret

# pytest
def test_preorder():
    # Create the tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.getLeftChild().insertRight("E")
    root.insertRight("C")
    root.insertRight("F")
    print(preorder(root))
def test_inorder():
    # Create the tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.getLeftChild().insertRight("E")
    root.insertRight("C")
    root.insertRight("F")
    print(inorder(root))
def test_postorder():
    # Create the tree
    root = BinaryTreeNode("A")
    root.insertLeft("B")
    root.getLeftChild().insertLeft("D")
    root.getLeftChild().insertRight("E")
    root.insertRight("C")
    root.insertRight("F")
    print(postorder(root))

''' Binary Search Tree
* Binary Search Trees are Binary Trees that have the following property
    * Values that are less than the parent are found in the left subtree
    * Values that are greater than the parent are found in the right subtree
    * This is known as the Binary Search Tree (BST) property
'''

test_preorder()
test_inorder()
test_postorder()

from LinkedList import *

# Testing the linked list implementation
def test_NodeCreation():
	n = Node(20)
	assert n.getData() == 20
	assert n.getNext() == None

def test_NodeSetData():
	n = Node(20)
	n.setData(200)
	assert n.getData() == 200

def test_NodeSetNext():
	n = Node(20)
	n2 = Node(10)
	n.setNext(n2)
	assert n.getNext() == n2

def test_createList():
	ll = LinkedList()
	assert ll.isEmpty() == True

def test_addingNodesToList():
	ll = LinkedList()
	assert ll.isEmpty() == True
	ll.addToFront(10)
	ll.addToFront("Gaucho")
	ll.addToFront(False)
	assert ll.isEmpty() == False
	assert ll.length() == 3
	assert ll.search(10) == True
	assert ll.search("Gaucho") == True
	assert ll.search(False) == True
	assert ll.search("CS9") == False

def test_removeNodesFromList():
	ll = LinkedList()
	ll.addToFront(10)
	ll.addToFront("Gaucho")
	ll.addToFront(False)
	ll.addToFront("CS9")
	assert ll.length() == 4
	assert ll.search(10) == True
	ll.remove(10)
	assert ll.search(10) == False
	assert ll.search("Gaucho") == True
	assert ll.search(False) == True
	assert ll.search("CS9") == True
	assert ll.length() == 3
	ll.remove(False)
	assert ll.search(False) == False
	assert ll.search("Gaucho") == True
	assert ll.search("CS9") == True
	assert ll.length() == 2
	assert ll.isEmpty() == False
	ll.remove("Gaucho")
	ll.remove("CS9")
	ll.isEmpty() == True
	ll.length() == 0

''' Ordered Linked List
* Similar to an unordered Linked List except the nodes in the list are ordered with respect to each other
* The implementation of both are similar, except we have to maintain the ordered property of the nodes when we manage the list
    * Most methods can be the same, but adding the node requires us to put a node in the correct position (instead of simply 
    adding to the front of the list)
    * Consider two cases:
        * Adding to the front of the Linked List
        * Adding to the middle / end of the Linked List 
'''

# Test to check if adding elements maintain order
def test_insertIntoOrderedList():
	ll = LinkedList()
	ll.add(35)
	ll.add(50)
	ll.add(10)
	ll.add(40)
	ll.add(20)
	ll.add(30)
	assert ll.getList() == \
		"10 20 30 35 40 50"
	ll.add(5)
	assert ll.getList() == \
		"5 10 20 30 35 40 50"
	ll.add(60)
	assert ll.getList() == \
		"5 10 20 30 35 40 50 60"

''' Variations of Linked Lists
* Linked Lists with head and tail reference keep track of the front and back of the list
* Double-Linked Lists also adds references to the node before it
* Circular-Linked Lists is a infinite loop of nodes
'''

''' Quadratic Sorting Algorithm
* Bubble Sort
    * Idea: It will make several passes through the list and swap adjacent elements to ensure the largest elements ends up at
    the end of the list (assuming we're sorting in ascending order)
    * The algorithm is O(n^2)
'''

# Creating a bubble sort algorithm
def bubbleSort(aList):
	for passnum in range(len(aList)-1,0,-1):
		for i in range(passnum):
			if aList[i] > aList[i+1]:
				# swap (bubble up!)
				temp = aList[i]
				aList[i] = aList[i+1]
				aList[i+1] = temp
		print(aList)
# Bubble sort pytest
def test_bubbleSort():
	list1 = [1,2,3,4,5,6]
	list2 = [2,2,2,2,2,2]
	list3 = []
	list4 = [6,7,5,3,1]
	bubbleSort(list1)
	assert list1 == [1,2,3,4,5,6]
	bubbleSort(list2)
	assert list2 == [2,2,2,2,2,2]
	bubbleSort(list3)
	assert list3 == []
	bubbleSort(list4)
	assert list4 == [1,3,5,6,7]





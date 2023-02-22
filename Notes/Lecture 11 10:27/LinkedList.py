''' Linked Lists
* Python lists are just one way to implement a List type strucutre
* The underlying strucutre of a Python List stores information in
CONTIGUOUS memory
* There is another way to implement a List type strucutre that performs
better in certain operations (and worse in others)
    * This doesn't organize data in contiguous memory, so maintaining the 
    list structure doesn't need to shift elements around
* LINKED LISTS are a List strucutre that is not atored in CONTIGUOUS memory
    * But Linked Lists still provide relative positioning of the data in
    the list

Linked List
* Object that manages and maintains the chain of nodes as a collection
* Contains a HEAD reference to the first node in the Linked List
    * As long as we know where the first element is, we can "walk"
    down the Linked List and visit every node in the structure
    * Methods in the Linked List class should maintain the links between
    the nodes.
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext

class LinkedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def addToFront(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def length(self):
		temp = self.head
		count = 0
		while temp != None:
			count = count + 1
			temp = temp.getNext()
		return count

	def search(self, item):
		temp = self.head
		found = False
		while temp != None and not found:
			if temp.getData() == item:
				found = True
			else:
				temp = temp.getNext()
		return found

	def remove(self, item):
		current = self.head
		
		if current == None: # empty list, nothing to do
			return

		previous = None
		found = False
		while not found: #Find the element
			if current == None:
				return
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		# Case 1: remove 1st element
		if found == True and previous == None:
			self.head = current.getNext()
		
		# Case 2: remove not 1st element
		if found == True and previous != None:
			previous.setNext(current.getNext())

# add method to maintain an Ordered Linked List
	def add(self, item):
		current = self.head
		previous = None
		stop = False

		# find the correct place in the list to add
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()

		# create Node with item to add
		temp = Node(item)

		# Case 1: insert at the front of the list
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else: # Case 2: insert not at front of list
			temp.setNext(current)
			previous.setNext(temp)

	# Method to get the items from front to back
	def getList(self):
		current = self.head
		output = ""
		while current != None:
			output += str(current.getData()) + " "
			current = current.getNext()
		output = output[:len(output)-1] # remove end space
		return output
''' Selection Sort
* Idea: Similar to bubble sort, we make passes through the list and find the largest element. We then swamp the largest element
in the correct place (each iteration will place the largest element at the end of the list assuming we’re sorting in ascending 
order).
    * Don't have to swamp with adjacent numbers
    * Think of it as “selecting” the largest element and then placing it in the correct place
* Similar to Bubble Sort, we have to make n-1 comparisons during the first iteration through the list
    * Then n-2 comparisons during the 2nd iteration, etc.
* If we count the number of comparisons in this algorithm, we have
    * n-1 + n-2 + … + 2 + 1 = n(n+1)/2
    * O(n2)
'''

# Creating a Selection Sort
def selectionSort(aList):
	for fillslot in range(len(aList)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if aList[location]>aList[positionOfMax]:
				positionOfMax = location

		# swap largest element in correct place
		temp = aList[fillslot]
		aList[fillslot] = aList[positionOfMax]
		aList[positionOfMax] = temp
		print(aList)

def test_selectionSort():
	list1 = [1,2,3,4,5,6]
	list2 = [2,2,2,2,2,2]
	list3 = []
	list4 = [6,7,5,3,1]
	selectionSort(list1)
	assert list1 == [1,2,3,4,5,6]
	selectionSort(list2)
	assert list2 == [2,2,2,2,2,2]
	selectionSort(list3)
	assert list3 == []
	selectionSort(list4)
	assert list4 == [1,3,5,6,7]

''' Insertion Sort
* Idea: We want to work left-to-right and insert unsorted elements into the sorted 
    * Similar to how one might sort a deck of cards * Work left-to-right, take a card and “insert” it into the correct position 
    on the left portion of the sorted deck
* When we check where to insert an element, we do up to 1 swap on the first iteration in order to make room for the element to be
inserted in the sorted left portion of the list
    * Then we do up to two swaps on the second iteration
    * Then up to three swaps on the third iteration, etc.
    * So we get: 1 + 2 + … + n-2 + n-1 swaps
    * O(n2)
* Let’s also look at the BEST case scenario (the list is already sorted)
    * Here, we still go through n elements, but no swaps occur because each position is in the correct place
    * So in the best case scenario, we have O(n)
'''

# Creating an insertion sort
def insertionSort(aList):
	for index in range(1,len(aList)):

		currentvalue = aList[index]
		position = index

		# shift elements over by one
		while position > 0 and aList[position-1] > currentvalue:
			aList[position] = aList[position-1]
			position = position-1

		# insert element in appropriate place
		aList[position] = currentvalue
		print(aList)

def test_insertionSort():
	list1 = [1,2,3,4,5,6]
	list2 = [2,2,2,2,2,2]
	list3 = []
	list4 = [6,7,5,3,1]
	insertionSort(list1)
	assert list1 == [1,2,3,4,5,6]
	insertionSort(list2)
	assert list2 == [2,2,2,2,2,2]
	insertionSort(list3)
	assert list3 == []
	insertionSort(list4)
	assert list4 == [1,3,5,6,7]


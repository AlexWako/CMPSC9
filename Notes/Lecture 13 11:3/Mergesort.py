''' Divide and Conqueror Alogrithm
* Subdivide a large problem into smaller problems
* Solve each smaller part
* Combine the solution of smaller sub problems back into the larger problem

Merge Sort
* Idea: Break a list into sublists where the size == 1
    * A sublist with one element is considered sorted
    * Merge each small sorted sublist together to form a sorted larger list
    * Continue to merge sublists back into the original lists
* Code breaks the code into two equal parts per recursive iteration
* If each split is considered a new level, then the highest level is log n
    * Each level needs to compare n elements
    * Therefore each merge sort is O(nlogn) since log n is done for n times
* One disadvantage of Merge Sort is it requires O(n) additional space when creating the left and right sublist
    * Can be problematic for extremely large lists
'''

# Implementation of merge sort
def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist) // 2

		# uses additional space to create the left / right
		# halves
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		# recursively sort the lefthalf, then righthalf
		mergeSort(lefthalf)
		mergeSort(righthalf)

		# merge two sorted sublists (left / right halves)
		# into the original list (alist)
		i = 0 # index for lefthalf sublist
		j = 0 # index for righthalf sublist
		k = 0 # index for alist

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				alist[k] = lefthalf[i]
				i = i + 1
			else:
				alist[k] = righthalf[j]
				j = j + 1
			k = k + 1

		# put the remaining lefthalf elements (if any) into
		# alist
		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		# put the remaining righthalf elements (if any) into
		# alist
		while j < len(righthalf):
			alist[k] = righthalf[j]
			j = j + 1
			k = k + 1

def testMergeSort():
    numList1 = [9,8,7,6,5,4,3,2,1]
    numList2 = [1,2,3,4,5,6,7,8,9]
    numList3 = []
    numList4 = [1,9,2,8,3,7,4,6,5]
    numList5 = [5,4,6,3,7,2,8,1,9]
    mergeSort(numList1)
    mergeSort(numList2)
    mergeSort(numList3)
    mergeSort(numList4)
    mergeSort(numList5)

    assert numList1 == [1,2,3,4,5,6,7,8,9]
    assert numList2 == [1,2,3,4,5,6,7,8,9]
    assert numList3 == []
    assert numList4 == [1,2,3,4,5,6,7,8,9]
    assert numList5 == [1,2,3,4,5,6,7,8,9]

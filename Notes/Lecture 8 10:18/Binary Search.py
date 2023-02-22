''' Python Lists
* Python lists store items in CONTIGUOUS memory (one item right next to each
other)
'''
# Slower since it finds the index then inserts
def f1(n):
    l = []
    for i in range(n):
        l.insert(0, i)
    return

# Faster since it only needs to insert 
def f2(n):
    l = []
    for i in range(n):
        l.append(i)
    return

''' Binary Search Algorithm
* A useful and performant algorithm to search for an item in a list
IF THE ITEMS ARE IN SORTED ORDER
* Eliminate half the search space FOR EACH iteration
    * Run in 0(log n) time.
    * Note, base 2 isn't traditionally denoted (unless the base is something
    other than 2).
'''

# iterative
def iterativebinarySearch(intList, item):
    first = 0
    last = len(intList) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if intList[mid] == item:
            found = True
        else:
            if item < intList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

# recursive
def recursivebinarySearch(intList, item):
    # base case
    if len(intList) == 0:
        return False

    mid = len(intList) // 2
    if intList[mid] == item:
        return True
    elif item < intList[mid]:
        return recursivebinarySearch(intList[:mid], item)
    else:
        return recursivebinarySearch(intList[mid+1:], item)

# tests
def test_binarySearchNormal():
    assert binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == True
    assert binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1) == False
    assert binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == False
    assert binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == True
    assert binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == True

def test_binarySearchDuplicates():
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 0) == True
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 2) == False
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], 4) == True
    assert binarySearch([-10, -5, 0, 1, 1, 4, 4, 7, 8], -5) == True

def test_binarySearchEmptyList():
    assert binarySearch([], 0) == False

def test_binarySearchSameValues():
    assert binarySearch([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 5) == True
    assert binarySearch([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 0) == False


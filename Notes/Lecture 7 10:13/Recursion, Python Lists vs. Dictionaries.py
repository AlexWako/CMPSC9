''' Recursion
* Recursion is when a function contains a call to itself.
* Recursive solutions are useful when the result is dependent on the result of
sub-parts of the problem.
* We're mostly familiar with writing code in an iterative (one statement after
the other)

Three laws of recursion:
* A recursive algorithm must have a BASE CASE
* A recursive alogrith must change its state and move towards the base case
* A recursive alogrithm must call itself, recursively
'''

''' Factorial
* N! = N * (N-1) * ... * 2 * 1
* N! = N * (N-1)!
* 0! = 1
'''

def factorial(n):
    if n==0: # Base case
        return 1
    return n * factorial(n-1)

print(factorial(3))

'''
* Pythons works by first in, last out
* Think of this reasoning with recursions
'''
# Step 3
def double(n):
    return 2 * n # Step 4

# Step 2
def triple(n):
    return n + double(n) # Step 5

# Step 1
print(triple(5)) # Step 6

''' Fibonacci
f(n) = f(n-1) + f(n-2)
f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, f(4) = 3, ...
'''

def fibonacci(n):
    # Base case
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

''' Lists vs. Dictionaries
* Python lists are efficient if we know the index of the item we're looking for
    * The reason why adding to the front of the list is costly is because lists
    have to "make room" for the element to be at index 0
        * All existing elemnts of the list need to shift one index up in order
        for the inserted elemnt to be placed at index 0
    * Adding to the end of the lists is not nearly as costly because no shifting
    of existing elemnts needs to occur
* Python dictionaries are efficient when looking up a key value
    * Dictionary values are actually stored in an underlying list
    * Keys are converted into a numerical value, which is passed into a hash
    function
        * The purpose of the hash function is to output the index for the
        underlying list based on the key value
        * We do not have to scan the underlying list strucutre since a key will
        always be placed into a specific location in the underlying list
'''

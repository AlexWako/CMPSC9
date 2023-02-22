from lab04 import solveMaze
from Stack import Stack

# Test 1
maze = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
assert solveMaze(maze, 4, 4) == True
assert maze == [
['+', '+', '+', '+', 'G', '+'],
['+', 8, '+', 11, 12, '+'],
['+', 7, 9, 10, '+', '+'],
['+', 6, '+', '+', 2, '+'],
['+', 5, 4, 3, 1, '+'],
['+', '+', '+', '+', '+', '+'] ]

# Test 2
maze = [
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',],
['+', 'G', ' ', '+', '+', '+', ' ', '+', '+', '+', '+',],
['+', ' ', ' ', '+', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', ' ', ' ', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', ' ', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', ' ', ' ', ' ', ' ', ' ', '+', '+',],
['+', ' ', ' ', '+', ' ', '+', ' ', ' ', ' ', ' ', '+',],
['+', ' ', ' ', '+', '+', '+', '+', '+', '+', '+', '+',],
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',]
]
assert solveMaze(maze, 8, 9) == True
assert maze == [
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',],
['+', 'G', 26, '+', '+', '+', 11, '+', '+', '+', '+',],
['+', ' ', 25, '+', '+', '+', 10, 9, '+', '+', '+',],
['+', ' ', 24, 23, '+', '+', 12, 8, '+', '+', '+',],
['+', ' ', '+', 22, '+', '+', 13, 7, '+', '+', '+',],
['+', ' ', '+', 21, '+', '+', 14, 6, '+', '+', '+',],
['+', ' ', '+', 20, 19, '+', 15, 5, '+', '+', '+',],
['+', ' ', '+', ' ', 18, 17, 16, 4, 3, '+', '+',],
['+', ' ', ' ', '+', ' ', '+', ' ', ' ', 2, 1, '+',],
['+', ' ', ' ', '+', '+', '+', '+', '+', '+', '+', '+',],
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',]
]

# Test 3
maze = [
['G', '+', '+'],
['+', ' ', '+'],
['+', '+', '+']
]
assert solveMaze(maze, 1, 1) == False
assert maze == [
['G', '+', '+'],
['+', 1, '+'],
['+', '+', '+']
]

# Test 4
maze = [
['+', '+', '+', '+'],
['+', '+', ' ', '+'],
['+', '+', ' ', '+'],
['+', '+', ' ', '+'],
['+', '+', ' ', '+'],
['+', '+', ' ', '+'],
['+', '+', ' ', '+'],
['+', '+', ' ', '+'],
['+', '+', ' ', '+'],
['+', 'G', ' ', '+'],
['+', '+', '+', '+']
]
assert solveMaze(maze, 9, 2) == True
assert maze == [
['+', '+', '+', '+'],
['+', '+', 9, '+'],
['+', '+', 8, '+'],
['+', '+', 7, '+'],
['+', '+', 6, '+'],
['+', '+', 5, '+'],
['+', '+', 4, '+'],
['+', '+', 3, '+'],
['+', '+', 2, '+'],
['+', 'G', 1, '+'],
['+', '+', '+', '+']
]

# Test 5
maze = [
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',],
['+', ' ', ' ', '+', '+', '+', ' ', '+', '+', '+', '+',],
['+', ' ', ' ', '+', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', ' ', ' ', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', '+', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', ' ', '+', ' ', ' ', '+', '+', '+',],
['+', ' ', '+', ' ', ' ', ' ', ' ', ' ', ' ', '+', '+',],
['+', ' ', ' ', '+', ' ', '+', ' ', ' ', ' ', 'G', '+',],
['+', ' ', ' ', '+', '+', '+', '+', '+', '+', '+', '+',],
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',]
]
assert solveMaze(maze, 1, 1) == True
assert maze == [
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',],
['+', 1, 14, '+', '+', '+', 30, '+', '+', '+', '+',],
['+', 2, 13, '+', '+', '+', 29, 31, '+', '+', '+',],
['+', 3, 12, 15, '+', '+', 28, 32, '+', '+', '+',],
['+', 4, '+', 16, '+', '+', 27, 33, '+', '+', '+',],
['+', 5, '+', 17, '+', '+', 26, 34, '+', '+', '+',],
['+', 6, '+', 18, 21, '+', 25, 35, '+', '+', '+',],
['+', 7, '+', 19, 20, 23, 24, 36, 40, '+', '+',],
['+', 8, 11, '+', 22, '+', 38, 37, 39, 'G', '+',],
['+', 9, 10, '+', '+', '+', '+', '+', '+', '+', '+',],
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+',]
]
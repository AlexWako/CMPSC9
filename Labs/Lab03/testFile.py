from lab03 import *

# tests for multiply
assert multiply(5, 3) == 15
assert multiply(10, 0) == 0
assert multiply(0 , 15) == 0
assert multiply(5, -1) == -5
assert multiply(-2, 7) == -14

# tests for collectMultiples
assert collectMultiples([1, 2, 3, 4, 5], 2) == [2, 4]
assert collectMultiples([], 3) == []
assert collectMultiples([-1, -2, -3, -4, -5], 2) == [-2, -4]
assert collectMultiples([3, 5, 7, 9, 3, 5, 7], 3) == [3, 9, 3]

# tests for countVowels
assert countVowels('Alex') == 2
assert countVowels('Computer Science') == 6
assert countVowels('') == 0
assert countVowels('HeLlO') == 2

# tests for reverseVowels
assert reverseVowels('Alex') == 'eA'
assert reverseVowels('Supercalifragilisticexpialidocious') == 'uoioiaieiiiaiaeu'
assert reverseVowels('This is for Lab03') == 'aoii'
assert reverseVowels('') == ''

# tests for removeSubString
assert removeSubString('This is for Lab03', 'is') == 'Th  for Lab03'
assert removeSubString('Helloellolloloo', 'lo') == 'Helel'
assert removeSubString('Halloween is in 13 days', 'Halloween is in 13 days') == ''
assert removeSubString('Alex', '') == 'Alex'

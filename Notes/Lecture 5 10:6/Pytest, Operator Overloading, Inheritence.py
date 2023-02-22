'''When pytest is imported, pytest can run through all functions starting with
test_ in the command terminal. Pytest gives valuable information and tells what
assert statement failed.
'''

def biggestInt(a, b, c, d):
    biggest = 0
    if a >= b and a >= c and a >= d:
        return a
    if b >= a and b >= c and b >= d:
        return b
    if c >= a and c >= b and c >= d:
        return c
    else:
        return d
    
def test_biggestInt1():
    assert biggestInt(1, 2, 3, 4) == 4
    assert biggestInt(1, 2, 4, 3) == 4
    assert biggestInt(1, 4, 2, 3) == 4
    assert biggestInt(4, 1, 2, 3) == 4

def test_biggestInt2():
    assert biggestInt(5, 5, 5, 5) == 5

def test_biggestInt3():
    assert biggestInt(-5, -10, -12, -100) == -5
    assert biggestInt(-100, 1, 1000, 0) == 1000

''' Operator Overloading
* Operator Overloading allows object that usually cannot use certain
operators to use those operator
* This can be done by creating a method when creating a new object
'''
from student import Student

s1 = Student("Jane", 5555555)
s2 = Student("Gaucho", 1234567)

students = s1 + s2
# Returns a list since the student file has a method that turns two
# student objects adding in to a list
print(type(students))

''' Inheritence
* a way of extending the functionality and properties of an existing class
    * allows us to add new features
    * allows us to replace existing features
'''

from Animal import Animal
from Cow import Cow

# Showing Cow class inherited the Animal class methods
c = Cow("Cow", "Betsy")
print(c.getAttributes())

''' Shallow vs. Deep Equality
* Python allows us to check for equality using the == operator for our objects
* By default, Python uses the memory address (not the values) to determine if
two objects are the same.
    * This is known as SHALLOW EQUALITY
* Comparing values (instead of memory addresses) is called DEEP EQUALITY
'''
from student import Student
from courses import Courses

s1 = Student("Jane", 1234567)
s2 = Student("Jane", 1234567)

print(s1 == s2)
''' The print statement returns false because the memory address of the two
variables are not equal
'''

''' Syntax vs. Run Time Errors
* Syntax errors occur before the program runs
* Run time error occurs while the program is running
'''

''' Exceptions
* Exeeption are errors that occur DURING program execution

Handeling Exceptions
* The general rule of expection is:
    * If an exception was raised in a program and nobody catches the exception
    error, then the program will terminate
* But we can handle exceptions with a general structure referred to as
try / except

Flow of Execution
* Everything within a try block is executed normally
* If an exception occurs in the try block, execution halts and an exception is
raised to the corresponding except block
* The except vlock tries to catch a certain exception type (not that Exception
catches ALL types of Exceptions (NameError, TypeError, ...)
* If there is a matching type then the first-matching except block is
executed
* Once done, program execution resumes past the except block
'''

def divide(numerator, denominator):
    if denominator == 0:
        # Creates an error without actually having to run the code fully
        raise ZeroDivisionError()
    return numerator/denominator

try:
    print(divide(1,1))
    print(divide(1,0))
    print(divide(2,2))
except ZeroDivisionError:
    print("Error: cannot divide by 0")

print("Resuming execution")

# Example of try / except
while True:
    try:
        x = int(input("Enter an int: "))
        print(x/0)
        break
    # Only one except block runs, done by top down
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception:
        print("Input was not an int")
    print("Let's try again")
print("Done")

''' Complete Test
* Testing every possible path through the code in every possible situation
* Generally Infeasible
* Ex: Test a combination of four integer and return the largest

Unit Testing: Testing individual pieces (units) of a program to ensure correct
behavior
'''

''' Test Driven Development
1. Write test cases that describe what the intended behavior of a unit of
software should be
2. Implement the dtails of the functionality with the intention of passing tests
3. Repeat until tests pass
'''

''' PYTHON OBJECTS
* Objects are a way for programmers to define their own Python types and create
abstractions of things with the programming language
* Each object may have a certain state that gets modified throughout program
execution
* Object oriented programming is the way programs use and manipulate
objects to solve problems and model of real-world properties
    * Object oriented programming is not required
    * It's more of a way to organize, read, maintain, test and debug software in
    a manageable way
'''

# Importing files into code
from Student import Student
from Courses import Courses

s1 = Student("Jane", 1234567)
s2 = Student("Joe", 7654321)
s3 = Student("Jill", 3333333)

UCSB = Courses()

UCSB.addStudent(s1, "CS8")
UCSB.addStudent(s2, "CS9")
UCSB.addStudent(s3, "CS16")
UCSB.printCourses()

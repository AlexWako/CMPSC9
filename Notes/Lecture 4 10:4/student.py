# student.py

# Creates new self-made object and methods
class Student:

    # Constuctors initializes values for a new object
    # Think of self as the current object using the method
    def __init__(self, name=None, perm=None):
        self.name = name
        self.perm = perm

    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("Student name: {}, perm: {}".format(self.name, self.perm))

    def getName(self):
        return self.name

    def getPerm(self):
        return self.perm

    # Runs when == operator is used (and applies deep equality)
    def __eq__(self, rhs):
        return self.perm == rhs.perm

'''
s = Student() # Initializing an instance of an object
s.setName("Name")
s.setPerm(1234567)
s.printAttributes()

# Creating multiple student objects
s1 = Student("Name1", 1234568)
s2 = Student("Name2", 1234569)
s3 = Student("Name3", 1234560)
student_list = [s1, s2, s3]
for s in student_list:
    s.printAttributes()
'''

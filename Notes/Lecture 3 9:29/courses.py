# courses.py

class Courses:
    ''' Class representing a collection of courses organized by a dictionay
        where the key is the course num and the value is a list of Students
    '''

    def __init__(self):
        self.courses = {}

    def addStudent(self, student, courseNum):
        # If the course doesn't exist
        if self.courses.get(courseNum) == None:
            self.courses[courseNum] = [student]

        elif not student in self.courses.get(courseNum):
            self.courses[courseNum].append(student)

    def printCourses(self):
        for courseNum in self.courses:
            print("CourseNum: ", courseNum)
            for student in self.courses[courseNum]:
                student.printAttributes()
            print("---")

class Student:
        def __init__(self, firstname="", lastname="", tnumber="", courselist=[]):
            self.firstname = firstname
            self.lastname = lastname
            self.tnumber = tnumber
            self.courses = courselist
class StudentList:
    def __init__(self, studentlist=[]):
        self.studentlist = studentlist  
    def add_student(self, Student):
        self.studentlist.append(Student)
    def find_student(self, studenttofind):
        for i in range(len(self.studentlist)):
            if self.studentlist[i].tnumber == studenttofind:
                return self.studentlist[i]
    def print_student_list(self):
        print(f'{"First Name":^10} {"Last Name":10} {"ID Number":10} {"Course":9} {"Name":42} {"Room":10} {"Meeting Times":15}')
        for i in range(len(self.studentlist)):
            print(f'{self.studentlist[i].firstname:10} {self.studentlist[i].lastname:10} {self.studentlist[i].tnumber:10}')
            for j in range(len(self.studentlist[i].courses)):
                print(f'{" "*34}{self.studentlist[i].courses[j].dept:4} {self.studentlist[i].courses[j].num:4} {self.studentlist[i].courses[j].name:42} {self.studentlist[i].courses[j].room:10} {self.studentlist[i].courses[j].time:15}')
    def add_student_from_file(self, filename):
        with open(filename) as lines:
            array = []
            for line in lines:
                row = line.split(",")
                for i in range(len(row)):
                    row[i] = row[i].strip()
                array.append(row)
            for i in range(len(array)):
                newstudent = Student(array[i][0], array[i][1], array[i][2])
                self.add_student(newstudent)
    def __getitem__(self, index):
        return self.studentlist[index]
class Course:
        def __init__(self, department="", number="", name="", room="", meetingtimes=""):
            self.dept = department
            self.num = number
            self.name = name
            self.room = room
            self.time = meetingtimes
class Courselist:
    def __init__(self, courselist=[]):
        self.courselist = courselist
    def add_course(self, Course):
        self.courselist.append(Course)
    def find_course(self, departmenttofind, numbertofind):
        for i in range(len(self.courselist)):
            if self.courselist[i].num == numbertofind and self.courselist[i].dept == departmenttofind:
                return self.courselist[i]
    def add_course_from_file(self, filename):
        with open(filename) as lines:
            array = []
            for line in lines:
                row = line.split(",")
                for i in range(len(row)):
                    row[i] = row[i].strip()
                array.append(row)
            for i in range(len(array)):
                newcourse = Course(array[i][0], array[i][1], array[i][2], array[i][3], array[i][4])
                self.add_course(newcourse)
    def __getitem__(self, index):
        return self.courselist[index]

mycourses = Courselist()
mycourses.add_course_from_file("11.03 Courses.txt")
students = StudentList()
students.add_student_from_file("11.03 Students.txt")

with open("11.03 Registration.txt") as lines:
    array = []
    for line in lines:
        row = line.split(",")
        for i in range(len(row)):
            row[i] = row[i].strip()
        array.append(row)
    for i in range(len(array)):
        student = students.find_student(array[i][0])
        enrolled = mycourses.find_course(array[i][1], array[i][2])
        student.courses.append(enrolled)
    students.print_student_list()
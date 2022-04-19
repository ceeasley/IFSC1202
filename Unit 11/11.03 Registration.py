class Student:
    def __init__(self, firstname, lastname, tnumber, grades):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.grades = grades
class StudentList:
    def __init__(self):
        self = []
    def add_student(self, firstname, lastname, tnumber):
        self = self.append(firstname, lastname, tnumber)
    def find_student(self, studenttofind):
        index = -1
        for i in range(len(self)):
            if self[i].tnumber == studenttofind.tnumber:
                index = i
        return index
    def print_student_list(self):
        print(f'{"First Name":^10} {"Last Name":^10} {"ID Number":^10}')
        for i in range(len(self)):
            print(f'{self[i].firstname:^10} {self[i].lastname:^10} {self[i].tnumber:^10}')
    def add_student_from_file(self, filename):
        
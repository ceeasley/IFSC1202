class Student:
    def __init__(self, firstname, lastname, tnumber, grades):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.grades = grades
    def RunningAverage(self):
        score = 0
        count = len(self.grades)
        for i in range(len(self.grades)):
            if self.grades[i] == "":
                count -= 1
            if self.grades[i] != "":
                score += int(self.grades[i])
        avg = score/count
        return avg
    def TotalAverage(self):
        score = 0
        for i in range(len(self.grades)):
            if self.grades[i] == "":
                self.grades[i] = 0
            score += int(self.grades[i])
        avg = score/len(self.grades)
        return avg
    def LetterGrade(self):
        if self.TotalAverage() >= 90:
            letter = "A"
        if 90 > self.TotalAverage() >= 80:
            letter = "B"
        if 80 > self.TotalAverage() >= 70:
            letter = "C"
        if 70 > self.TotalAverage() >= 60:
            letter = "D"
        if 60 > self.TotalAverage():
            letter = "F"
        return letter
with open("10.04 StudentScores.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            line = line.replace(" ","")
            row = line.split(",")
            array.append(row)
    print(f'{"First Name":^10} {"Last Name":^10} {"ID Number":^10} {"Running Average":^16} {"Semester Average":^16} {"Letter Grade":^12}')
    for i in range(len(array)):
        grades = []
        for j in range(3,len(array[i])):
            grades.append(array[i][j])
        newstudent = Student(array[i][0], array[i][1], array[i][2], grades)
        print(f'{newstudent.firstname:^10} {newstudent.lastname:^10} {newstudent.tnumber:^10} {newstudent.RunningAverage():^16.2f} {newstudent.TotalAverage():^16.2f} {newstudent.LetterGrade():^12}')
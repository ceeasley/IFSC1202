class Employee:
    def __init__(self, FirstName, LastName, IDNumber, HoursWorked, Wage):
        self.fname = FirstName
        self.lname = LastName
        self.id = IDNumber
        self.worked = HoursWorked
        self.wage = Wage
    def WeeklyPay(self):
        hours = float(self.worked)
        rate = float(self.wage)
        if hours > 40:
            pay = (rate*40) + ((hours - 40)*(1.5*rate))
        else:
            pay = rate*hours
        return pay
with open("10.06 Payroll.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            line = line.replace(" ","")
            line = line.replace("\n","")
            row = line.split(",")
            array.append(row)
    print(f'{"First Name":15} {"Last Name":15} {"ID Number":15} {"Hours Worked":15} {"Hourly Wage":15} {"Pay":15}')
    for i in range(len(array)):
        newemployee = Employee(array[i][0], array[i][1], array[i][2], array[i][3], array[i][4])
        print(f'{newemployee.fname:<15} {newemployee.lname:<15} {newemployee.id:<15} {newemployee.worked:<15} ${newemployee.wage:<14} ${newemployee.WeeklyPay():<14.2f}')
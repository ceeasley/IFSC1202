class Employee:
    def __init__(self, FirstName, LastName, IDNumber, Wage, HoursWorked=0):
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
def find_employee(list1, ID):
    index = -1
    for i in range(len(list1)):
        if list1[i][0] == ID:
            index = i
    return index
with open ("11.02 Employees.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            line = line.replace(" ","")
            line = line.replace("\n","")
            row = line.split(",")
            array.append(row)
    print(f'{"First Name":15} {"Last Name":15} {"ID Number":15} {"Hours Worked":15} {"Hourly Wage":15} {"Pay":15}')
    employees = []
    for i in range(len(array)):
        newemployee = Employee(array[i][0], array[i][1], array[i][2], array[i][3])
        employees.append(newemployee)
    with open ("11.02 Hours.txt") as updates:
        newhours = []
        for update in updates:
            if update != "\n":
                update = update.replace(",","")
                row = update.split()
                newhours.append(row)
        for i in range(len(employees)):
            index = find_employee(newhours, employees[i].id)
            if index != -1:
                employees[i].worked = int(newhours[index][1])
            print(f'{employees[i].fname:<15} {employees[i].lname:<15} {employees[i].id:<15} {employees[i].worked:<15} ${employees[i].wage:<14} ${employees[i].WeeklyPay():<14.2f}')
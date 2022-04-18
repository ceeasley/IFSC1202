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
        
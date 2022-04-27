class House:
    def __init__(self, address, sqft, price):
        self.address = address
        self.sqft = sqft
        self.price = price
    def costpersqft(self):
        cost = self.price/self.sqft
        return cost
    def payment(self,ar,ny):
        nm = ny*12
        mr = ar/12
        payment = self.price*(((mr*(1+mr)**nm))/(((1+mr)**nm)-1))
        return payment

with open ("Exam Three Houses.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            row = line.split(",")
            for i in range(len(row)):
                row[i] = row[i].strip()
            array.append(row)
    houselist = []
    for i in range(len(array)):
        newhouse = House(array[i][0],int(array[i][1]),int(array[i][2]))
        houselist.append(newhouse)
    rate = (float(input("Enter Interest Rate (%): ")))/100
    term = float(input("Enter Years for Mortgage (years): "))
    print(f'{"Address":^15} {"SqFt":^8} {"SqFt Cost":^8} {"Price":^10} {"Payment":^10}')
    for i in range(len(houselist)):
        print(f'{houselist[i].address:<15} {houselist[i].sqft:>8} {houselist[i].costpersqft():>8.2f} {houselist[i].price:>10} {houselist[i].payment(rate,term):>10.2f}')
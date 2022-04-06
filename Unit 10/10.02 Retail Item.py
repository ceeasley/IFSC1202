class RetailItem:
    def __init__(self, description="", UnitsOnHand=0, Price=0):
        self.description = description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price
    def inval(self):
        invval = float(self.UnitsOnHand) * float(self.Price)
        return invval    

print(f'{"Description":15} {"Units On Hand":15} {"Price":10} {"Inventory Value":15}')
with open ("10.02 Inventory.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            line = line.replace(",","")
            row = line.split()
            array.append(row)
    for i in range(len(array)):
        newitem = RetailItem(array[i][0],array[i][1],array[i][2])
        newinval = newitem.inval()
        print(f'{newitem.description:15} {newitem.UnitsOnHand:15} {newitem.Price:10} {newinval:15.2f}')
class RetailItem:
    def __init__(self, description="", UnitsOnHand=0, Price=0):
        self.description = description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price
    def inval(self):
        invval = float(self.UnitsOnHand) * float(self.Price)
        return invval
def print_inventory(x):
    print(f'{"Description":15} {"Units On Hand":15} {"Price":10} {"Inventory Value":15}')
    for i in range(len(x)):
        newitem = x[i]
        newinval = newitem.inval()
        print(f'{newitem.description:15} {newitem.UnitsOnHand:15} {newitem.Price:<10} {newinval:15.2f}')
def find_inventory(list1, item):
    index = -1
    for i in range(len(list1)):
        if list1[i][0] == item:
            index = i
    return index
with open ("11.01 Inventory.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            line = line.replace(",","")
            row = line.split()
            array.append(row)
    inventory = []
    for i in range(len(array)):
        newitem = RetailItem(array[i][0],array[i][1],array[i][2])
        inventory.append(newitem)
    print_inventory(inventory)
    with open ("11.01 InventoryUpdate.txt") as updates:
        newprice = []
        for update in updates:
            if update != "\n":
                update = update.replace(",","")
                row = update.split()
                newprice.append(row)
        for i in range(len(inventory)):
            index = find_inventory(newprice, inventory[i].description)
            if index != -1:
                inventory[i].Price = float(newprice[index][1])
        print_inventory(inventory)
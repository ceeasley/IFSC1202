with open("CarSales.txt") as sales:
    array = []
    count = 0
    salesum = 0
    salecount = 0
    for sale in sales:
        sale = sales.readline()
        sale = sale.strip()
        saledata = sale.split(",")
        array.append(saledata)
        salecount += 1
        # salecount consistently stops at 500 in spite of repeatedly checking the copy/pasted file and also deleting and uploading a downloaded copy, reloading Gitpod, etc.
for i in range(len(array)):
    count += 1
    salesum += int(array[i][1])
saleavg = int(salesum/count)
print(f'{count} total cars - Average Price: ${saleavg}')
make = input("Enter Car Make: ")
if make != "":
    make = make.upper()
    makecount = 0
    makesale = 0
    for i in range(len(array)):
        match = array[i][0].upper()
        if make == match:
            makecount += 1
            makesale += int(array[i][1])
    if makecount == 0:
        print("Car Make Not Found")
    if makecount != 0:
        makeavg = int(makesale/makecount)
        diff = (makeavg-saleavg)/saleavg
        print(f'{makecount:>6} Cars Sold\n${makeavg} Average Price\n{diff:>6.2%} Above/Below Average')

with open("08.11 USPopulation.txt") as uspop:
    uspoplist = uspop.read().splitlines()
    
    def multiply(mylist):
        for i in range(len(mylist)):
            product = int(mylist[i])*1000
            mylist[i] = product
        return mylist
    def change(mylist):
        newlist = []
        for y in range(1,len(mylist)):
            x = y-1
            z = int(mylist[y])-int(mylist[x])
            newlist += [z]
        return newlist
    def percent(mylist):
        newlist = []
        for y in range(1,len(mylist)):
            x = y-1
            z = ((int(mylist[y])-int(mylist[x]))/int(mylist[x]))
            newlist += [z]
        return newlist
    def average(mylist):
        listsum = 0
        leng = 0
        for i in range(len(mylist)):
            listsum += int(mylist[i])
            leng += 1
        avg = listsum/leng
        return avg
    
    poplist = multiply(uspoplist)
    changelist = change(poplist)
    percentlist = percent(poplist)
    avgchange = average(changelist)
    year = 1950
    minimum = 999999999999
    maximum = 0

    print(f"{'Year':6} {'Population':12} {'Change':10} {'Percent Change':14}")
    for i in range(len(poplist)):
        if i == 0:
            print(f"{year:<6} {poplist[0]:<12} {'N/A':10} {'N/A':14}")
        if i > 0:
            print(f"{year:<6} {poplist[i]:<12} {changelist[i-1]:<10} {percentlist[i-1]:<14.2%}")
        year +=1
        if i < len(changelist):
            if int(changelist[i]) < minimum:
                minimum = int(changelist[i])
                minyear = year
            if int(changelist[i]) > maximum:
                maximum = int(changelist[i])
                maxyear = year    
    print(f"Average Change = {avgchange}\nMinimum Change = {minimum} ({minyear})\nMaximum Change = {maximum} ({maxyear})")
print("Welcome! First, I need some information from you.")
fname = lower(input("Please enter your first name: "))
mname = lower(input("Please enter your middle name (leave blank if you don't have one): "))
lname = lower(input("Please enter your last name: "))
mdate = input("Please enter your birth month (MM): ")
ddate = input("Please enter your birth day (DD): ")
ydate = input("Please enter your birth year (YYYY): ")

f_name = ''.join(filter(str.isalpha,fname))
m_name = ''.join(filter(str.isalpha,mname))
l_name = ''.join(filter(str.isalpha,lname))

while True:
    if str.isnumeric(mdate) is False:
        print("Error: Please enter a number for your birth month.")
        mdate = input("Birth month (MM): ")
    if str.isnumeric(ddate) is False:
        print("Error: Please enter a number for your birth day.")
        ddate = input("Birth day (DD): ")
    if str.isnumeric(ydate) is False:
        print("Error: Please enter a number for your birth year.")
        ydate = input("Birth year (YYYY): ")

compdate = ''.join(ddate,mdate,ydate)
compname = ''.join(f_name,m_name,l_name)

def lifepath(month,day,year):
    lifepathm = 0
    lifepathd = 0
    lifepathy = 0
    x = 0
    for i in range(0,len(month)):
        lifepathm += i
        if lifepathm > 9:
            for i in range(0,len(lifepathm)):
                x += i
                lifepathm = x
            x = 0
        return lifepathm
    for i in range(0,len(day)):
        lifepathd += i
        if lifepathd > 9:
            for i in range(0,len(lifepathd)):
                x += i
                lifepathd = x
            x = 0
        return lifepathd
    for i in range(0,len(year)):
        lifepathy += i
        if lifepathy > 9:
            for i in range(0,len(lifepathy)):
                x += i
                lifepathy = x
            x = 0
        return lifepathy
    lifepath = lifepathd + lifepathm + lifepathy
    return lifepath

def destinynumber(first, mid, last):
    for i in range(0,len(first)):
        sumf = 0
        if i == "a" or i == "j" or i == "s":
            sumf += 1
        if i == "b" or i == "k" or i == "t":
            sumf += 2
        if i == "c" or i == "l" or i == "u":
            sumf += 3
        if i == "d" or i == "m" or i == "v":
            sumf += 4
        if i == "e" or i == "n" or i == "w":
            sumf += 5
        if i == "f" or i == "o" or i == "x":
            sumf += 6
        if i == "g" or i == "p" or i == "y":
            sumf += 7
        if i == "h" or i == "q" or i == "z":
            sumf += 8
        if i == "i" or i == "r":
            sumf += 9
    for i in range(0,len(mid)):
        summ = 0
        if i == "a" or i == "j" or i == "s":
            summ += 1
        if i == "b" or i == "k" or i == "t":
            summ += 2
        if i == "c" or i == "l" or i == "u":
            summ += 3
        if i == "d" or i == "m" or i == "v":
            summ += 4
        if i == "e" or i == "n" or i == "w":
            summ += 5
        if i == "f" or i == "o" or i == "x":
            summ += 6
        if i == "g" or i == "p" or i == "y":
            summ += 7
        if i == "h" or i == "q" or i == "z":
            summ += 8
        if i == "i" or i == "r":
            summ += 9
    for i in range(0,len(last)):
        suml = 0
        if i == "a" or i == "j" or i == "s":
            suml += 1
        if i == "b" or i == "k" or i == "t":
            suml += 2
        if i == "c" or i == "l" or i == "u":
            suml += 3
        if i == "d" or i == "m" or i == "v":
            suml += 4
        if i == "e" or i == "n" or i == "w":
            suml += 5
        if i == "f" or i == "o" or i == "x":
            suml += 6
        if i == "g" or i == "p" or i == "y":
            suml += 7
        if i == "h" or i == "q" or i == "z":
            suml += 8
        if i == "i" or i == "r":
            suml += 9
    destiny = sumf + summ + suml

    
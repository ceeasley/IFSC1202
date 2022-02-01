#Prompt for a 4 digit year'
#If the year is a leap year, print "LEAP YEAR", otherwise print "COMMON YEAR".
#The rules in Gregorian calendar are as follows:
#    A year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
#    A year is always a leap year if its number is exactly divisible by 400

x = int(input("Enter a year (YYYY): "))

if (x%4) == 0:
    if x%400 == 0:
        print("LEAP YEAR")
    elif x%100 != 0:
        print("LEAP YEAR")
    else:
        print("COMMON YEAR")
else:
    print("COMMON YEAR")
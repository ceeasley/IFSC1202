#Given a month - an integer from 1 (January) to 12 (December), print the number of days in the month.
#Assume that it is a non-leap year.

x = int(input("Enter a month (1-12): "))

if 0 < x <= 12:
    if x == 2:
        print("28 days")
    elif x == 4 or x == 6 or x == 9 or x == 11:
        print("30 days")
    else:
        print("31 days")
else:
    print("Please enter a number between 1 (Jan) and 12 (Dec).")
#Prompt for a month (an integer from 1 to 12) and a day in the month (an integer from 1 to 31) in a common year (not a leap year).
#Print the month and the day of the next day after it.
#    The first test corresponds to March 30 - next day is March 31
#    The second test corresponds to March 31 - next day is April 1
#    The third test corresponds to December 31 - next day is January 1

x = int(input("Enter a month (1-12): "))
y = int(input("Enter a day (1-31): "))

if 0 < x <= 12:
    if 0 < y <= 31:
        if x == 2:
            if y <=27:
                month = February
                day = y + 1
                print("The next day is {} {}.".format(month, day))
            elif y == 28:
                month = March
                day = 1
                print("The next day is {} {}.".format(month, day))
            else:
                print("Error: Please check your month and day values.")
        elif x == 4 or x == 6 or x == 9 or x == 11:
            if y <= 29:
                if x == 4:
                    month = "April"
                elif x == 6:
                    month = "June"
                elif x == 9:
                    month = "September"
                elif x == 11:
                    month = "November"
                day = y + 1
                print("The next day is {} {}.".format(month, day))
            elif y == 30:
                if x == 4:
                    month = "May"
                elif x == 6:
                    month = "July"
                elif x == 9:
                    month = "October"
                elif x == 11:
                    month = "December"
                day = 1
                print("The next day is {} {}.".format(month, day))
            else:
                print("Error: Please check your month and day values.")
        elif x <= 12:
            if y <= 30: 
                if x == 1:
                    month = "January"
                elif x == 3:
                    month = "March"
                elif x == 5: 
                    month = "May"
                elif x == 7:
                    month = "July"
                elif x == 8:
                    month = "August"
                elif x == 10:
                    month = "October"
                elif x == 12:
                    month = "December"
                day = y + 1
                print("The next day is {} {}.".format(month, day))
            elif y == 31:
                if x == 1:
                    month = "February"
                elif x == 3:
                    month = "April"
                elif x == 5: 
                    month = "June"
                elif x == 7:
                    month = "August"
                elif x == 8:
                    month = "September"
                elif x == 10:
                    month = "November"
                elif x == 12:
                    month = "January"
                day = 1
                print("The next day is {} {}.".format(month, day))
            else:
                print("Error: Please check your month and day values.")
    else:
        print("Please enter a day between 1 and 31.")
else:
    print("Please enter a month between 1 (Jan) and 12 (Dec).")
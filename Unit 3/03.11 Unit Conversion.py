#Create a python program that performs unit conversions. You code should do the following:
#    Prompt for a floating point number (FromValue). Your prompt should display "Enter From Value: "
#    Prompt for the unit to convert from (FromUnit). Your prompt should display "Enter From Unit (in, ft, yd, mi):"
#    Using an if statement make sure that the from unit is one of the following: in, ft, yd, mi. If not, display "FromUnit is not valid" and then exit the program
#    Prompt for the unit to convert to (ToUnit). Your prompt should display "Enter From Unit (in, ft, yd, mi):"
#    Using an if statement make sure that the to unit is one of the following: in, ft, yd, mi. If not, display "ToUnit is not valid" and then exit the program
#    Using a series of if statements, determine the value of multiplier needed to convert the value using the FromUnit to the ToUnit. You will need 16 of them. If a user enters the same FromUnit and ToUnit, then the multiplier is 1.0 (See http://www.unit-conversion.info/length.html)
#    if FromUnit == "ft" and ToUnit == "yd": multiplier = 0.3333333333

#    Finally, multiply the multiplier times the FromValue to get the ToValue (Use the round function to round to 7 digits)
#    Display the FromValue, FromUnit, ToValue and ToUnit as shown

FromValue = float(input("Enter From Value: "))
FromUnit = input("Enter From Unit (in, ft, yd, mi): ")

if FromUnit == "in":
    pass
elif FromUnit == "ft":
    pass
elif FromUnit == "yd":
    pass
elif FromUnit == "mi":
    pass
else:
    print("FromUnit is not valid.")
    exit

ToUnit = input("Enter To Unit (in, ft, yd, mi): ")

if ToUnit == "in":
    pass
elif FromUnit == "ft":
    pass
elif FromUnit == "yd":
    pass
elif FromUnit == "mi":
    pass
else:
    print("ToUnit is not valid.")
    exit

if FromUnit == ToUnit:
    x = 1
elif FromUnit == "in":
    if ToUnit == "ft":
        x = (1/12)
    elif ToUnit == "yd":
        x = (1/36)
    elif ToUnit == "mi":
        x = (1/63360)
elif FromUnit == "ft":
    if ToUnit == "in":
        x = 12
    elif ToUnit == "yd":
        x = (1/3)
    elif ToUnit == "mi":
        x = (1/5280)
elif FromUnit == "yd":
    if ToUnit == "ft":
        x = 3
    elif ToUnit == "in":
        x = 36
    elif ToUnit == "mi":
        x = (1/1760)
elif FromUnit == "mi":
    if ToUnit == "ft":
        x = 5280
    elif ToUnit == "yd":
        x = 1760
    elif ToUnit == "in":
        x = 63360

ToValue = round((x * FromValue), 7)

print("{} {} => {} {}".format(FromValue, FromUnit, ToValue, ToUnit))
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
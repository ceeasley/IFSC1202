#Write a program that prompts for the number of kilometers.
#Calculate and display the number of miles in the kilometers.
#Hint: Use the float() function to convert your input to an floating number.
#Hint: There are 1.61 kilometers in a mile.

km = float(input("Kilometers to convert: "))

miles = km/1.61

print(str(km)+" kilometers are equivalent to "+str(miles)+" miles.")
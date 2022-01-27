#Prompt for a positive real number
#Print the first digit to the right of the decimal point.
#Use only math for your solution; do no use any string functions.

x = float(input("Enter a positive real number: "))

deci = int((x-int(x))*10)

print("{}".format(deci))
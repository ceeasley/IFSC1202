#Enter a number greater than zero and print the value its last two digits.
#Be sure to use to .format method to create your output. You will have to use leading zeros.
#Use only math for your solution; do no use any string functions.

x = int(input("Enter a number: "))

digits = x%100

print("{:02d}".format(digits))
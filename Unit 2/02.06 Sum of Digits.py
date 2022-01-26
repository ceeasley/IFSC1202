#Enter a three digit number and print the sum of the digits.
#Be sure to use the .format method to create your output.
#Use only math for your solution; do no use any string functions.

x = int(input("Enter a three digit number: "))

hundred = x//100
tens = (x%100)//10
ones = x%10

total = hundred + tens + ones

print("The sum of these digits is {}".format(total))
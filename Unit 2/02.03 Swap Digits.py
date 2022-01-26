#Enter a two digit number and swap their digits and create a new two digit number.
#Be sure to use the .format method to create your output.
#Use only math for your solution; do no use any string functions.

x = int(input("Enter a two digit number: "))

tens = x//10
ones = x%10

print("{}{}".format(ones,tens))
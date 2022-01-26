#Enter a two digit number and print out its digits separately.
#Be sure to use to .format method to create your output.
#Use only math for your solution; do no use any string functions.

x = int(input("Enter a two digit number: "))

tens = x//10
ones = x%10

print("The tens digit is {}".format(tens))
print("The ones digit is {}".format(ones))
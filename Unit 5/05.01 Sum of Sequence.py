#Prompt for a sequence of numbers, the last number being zero.
#Print the sum of the numbers.

x = int(input("Enter a Number (zero to quit): "))
sumx = 0

while x != 0:
    x = int(input("Enter a Number (zero to quit): "))
    sumx += x
else:
    print("Sum: {}".format(sumx))
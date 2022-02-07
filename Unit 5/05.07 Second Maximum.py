#Prompt for a sequence of numbers, the last number being zero.
#Print the maximum and second maximum of the sequence.
#Assume that at least two numbers will always be entered.
#Hint: Each time you find a new maximum, the old maximum becomes the second maximum.


max1 = 0
max2 = 0
x = int(input("Enter a Number: "))
y = int(input("Enter a Number: "))

while x != 0:
    if x < y:
        x = y
    if max1 < x:
        max2 = max1
        max1 = x
    else:
        pass
    x = int(input("Enter a Number (zero to quit): "))
print("First Maximum: {}\n".format(max1) + "Second Maximum: {}".format(max2))
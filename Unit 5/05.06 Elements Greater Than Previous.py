#Prompt for a sequence of numbers, the last number being zero.
#Print the number many elements of this sequence are greater than their previous neighbor.

x = int(input("Enter a Number (zero to quit): "))
y = x
count = 0

while x != 0:
    if y < x:
        count += 1
    else:
        pass
    y = x
    x = int(input("Enter a Number (zero to quit): "))
print("Number of values greater than the previous: {}".format(count))
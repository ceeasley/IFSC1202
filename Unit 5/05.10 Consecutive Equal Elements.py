#Prompt for a sequence of numbers, the last number being zero.
#Print the maximum number of consecutive equal elements.
#If a value repeats the same number of times, display the first value.

x = int(input("Enter a Number (zero to quit): "))
y = int(input("Enter a Number (zero to quit): "))
count = 1
maxcount = 1

while x != 0:
    if x == y:
        count += 1
    elif x != y:
        count = 1
    if maxcount < count:
        maxcount = count

    x = int(input("Enter a Number (zero to quit): "))

print("{} repeated {} times".format(y,maxcount))
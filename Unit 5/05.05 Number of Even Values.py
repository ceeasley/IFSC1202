#Prompt for a sequence of numbers, the last number being zero.
#Print the number of even values.

x = int(input("Enter a Number (zero to quit): "))
count = 0

while x != 0:
    if (x%2) == 0:
        count += 1
    else:
        pass
    x = int(input("Enter a Number (zero to quit): "))
print("Number of Even Values: {}".format(count))
#Prompt for a sequence of numbers, the last number being zero.
#Print the largest value of the numbers.

x = int(input("Enter a Number (zero to quit): "))
max_val = 0

while x != 0:
    if max_val > x:
        pass
    else:
        max_val = x
    x = int(input("Enter a Number (zero to quit): "))
print("Maximum: {}".format(max_val))
#Prompt for a sequence of floating point or integer numbers, the last number being zero.
#Assume that at least one number will be entered.
#When the zero is entered, display the:
#    Count
#    Sum
#    Average
#    Minimum
#    Maximum
#Do not store the values in a list or use the min(), max(), or mean() functions

x = float(input("Enter a Number: "))
y = float(input("Enter a Number: "))
count = 1
sumx = y
minimum = x
maximum = x

while x != 0:
    count += 1
    sumx += x
    if x > y:
        if 0 < y < minimum:
            minimum = y
        if maximum < x:
            maximum = x
    if x < y:
        if minimum > x > 0:
            minimum = x
        if y > maximum:
            maximum = y

    y = x
    x = float(input("Enter a Number (zero to quit): "))


avg = sumx/count
print("Count: {}\n".format(count) + "Sum: {}\n".format(sumx) + "Average: {}\n".format(avg) + "Minimum: {}\n".format(minimum) + "Maximum: {}".format(maximum))

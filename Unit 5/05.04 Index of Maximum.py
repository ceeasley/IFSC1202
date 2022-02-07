#Prompt for a sequence of numbers, the last number being zero
#Print largest value and the index the largest value of the numbers.
#If no numbers are entered (only a zero), then both the maximum and the index should be 0.

x = int(input("Enter a Number (zero to quit): "))
max_val = 0
index = 0

while x != 0:
    index += 1
    if max_val > x:
        pass
    else:
        max_val = x
        sequence = index
    x = int(input("Enter a Number (zero to quit): "))

if x == 0 and index == 0:
    print("Maximum: 0\n" + "Index of Maximum: 0")
else: 
    print("Maximum: {}\n".format(max_val) + "Index of maximum: {}".format(sequence))
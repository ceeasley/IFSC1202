#Prompt for a sequence of numbers, the last number being zero.
#Print the maximum value and the number of times it occurs.

x = int(input("Enter a Number (zero to quit): "))
max_val = 0
count = 0

while x != 0:
    if max_val == x:
        count +=1
    elif max_val < x:
        max_val = x
        count = 1
    x = int(input("Enter a Number (zero to quit): "))

if x == 0 and count == 0:
    print("Maximum: 0\n" + "Number of Occurrences: 0")
else: 
    print("Maximum: {}\n".format(max_val) + "Number of Occurrences: {}".format(count))
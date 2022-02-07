#Prompt for a sequence of numbers, the last number being zero
#Print the average of the numbers
#If no data is entered (only a zero was entered), you will generate an error (division by zero). If no data is entered, print "Sequence Length is 0".

x = int(input("Enter a Number (zero to quit): "))
sumx = 0
sequence = 0

while x > 0:
    sumx += x
    x = int(input("Enter a Number (zero to quit): "))
    sequence += 1
if x == 0 and sequence == 0:
    print("Sequence Length is 0")

averagex = (sumx/sequence)
print("Average: {}".format(averagex))
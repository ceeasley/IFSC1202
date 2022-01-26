#Enter a number and print its tens digit.
#Be sure to use the .format method to create your output
#Use only math for your solution; do no use any string functions.

x = int(input("Enter a number: "))

tens = (x//10)%10

print("The tens digit is {}".format(tens))


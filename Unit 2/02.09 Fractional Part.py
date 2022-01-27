#Enter a positive real number and print its fractional part.
#Use only math for your solution; do no use any string functions.
#Hint: Round the result to 10 digits using the round function.

x = float(input("Enter a positive real number: "))

fraction = round(x%1,10)

print("Fractional part: {}".format(fraction))
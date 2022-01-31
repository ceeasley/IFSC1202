#Prompt for three numbers and print the smallest value.
#Try to use the cascade if-elif-else.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b and a < c:
    print ("{} is the smallest number.".format(a))
elif b < c: 
    print ("{} is the smallest number.".format(b))
else:
    print ("{} is the smallest number.".format(c))
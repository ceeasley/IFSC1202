#Prompt for three integers: two are equal to each other and the third one is different.
#Print the index number of the different one, either 1, 2 or 3.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b:
    print("3")
elif b == c:
    print("1")
elif a == c:
    print("2")
else:
    print("Two numbers should match.")
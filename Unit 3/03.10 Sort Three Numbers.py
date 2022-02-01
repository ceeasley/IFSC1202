#Prompt for three integers and print them in ascending order.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if b > c:
        print("{} {} {}".format(c, b, a))
    elif b <= c and c <= a:
        print("{} {} {}".format(b, c, a))
    elif b <= c and c > a:
        print("{} {} {}".format(b, a, c))
elif a <= b:
    if b < c:
        print("{} {} {}".format(a, b, c))
    elif b >= c and c >= a:
        print("{} {} {}".format(a, c, b))
    elif b >= c and c < a:
        print("{} {} {}".format(c, a, b))

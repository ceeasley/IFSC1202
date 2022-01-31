#Given a three-digit integer, print "YES" if its digits are in ascending order left to right, print "NO" otherwise.

x = int(input("Enter a three digit number: "))

a = x//100
b = (x%100)//10
c = x%10

if a < b < c:
    print("YES")
else:
    print("NO")
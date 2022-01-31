#A palindrome is a number which reads the same when read forward as it it does when read backward.
#Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
#Hint: put the units, tens, hundreds, and thousands in separate variables.

x = int(input("Enter a four digit number: "))

a = str(x//1000)
b = str((x%1000)//100)
c = str((x%100)//10)
d = str(x%10)

reverse = int(d + c + b + a)

if x == reverse:
    print("YES")
else:
    print("NO")
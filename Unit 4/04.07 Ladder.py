#For given integer N ≤ 9, print a ladder of N steps.
#The Kth step consists of the integers from 1 to K without spaces between them.
#You can use the sep= and end= arguments of the print() function.
#Hint: You can use a For loop within a For loop.

N = int(input("Enter N: "))

for i in range(1,N+1):
    for x in range(1,i+1):
        print(x,end="")
    print()
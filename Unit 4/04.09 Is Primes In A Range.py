#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#Given two integers A and B, print all prime numbers between them, inclusively.
#Hint: Copy your code from the Is Prime assignment and modify it so that N varies from A to B.

A = int(input("Enter A: "))
B = int(input("Enter B: "))


for i in range(A,B+1):
    for x in range(2,i):
        if i%x == 0:
            break
    else:
        print(i)
    

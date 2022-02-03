#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#Given an integer N > 1, print PRIME if it's prime and print COMPOSITE otherwise.
#Hint: Loop from 2 to (half of N) + 1 and check to see if any number evenly divides into N.

N = int(input("Enter N: "))
x = (N//2) + 1

for i in range(2,x):
    if (N%i) == 0:
        result = "COMPOSITE"
    else:
        result = "PRIME"

print(result)
    
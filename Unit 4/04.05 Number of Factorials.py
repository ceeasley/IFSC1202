#Given an integer N, print the sum of: 1! + 2! + 3! + ... + N!
#This problem has a solution with only one loop, so try to discover it.
#Don't use the math library.

x = 1
result = 0
N = int(input("Enter number: "))

for i in range(1,N+1):
    x = x * i
    result += x

print(result)
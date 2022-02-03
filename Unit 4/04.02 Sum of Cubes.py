#For the given integer N, calculate the sum cubes of each number from 1 to N.
#1**3 + 2**3 + … + N**3

result = 0
N = int(input("Enter N: "))

for i in range(N+1):
    x = i**3
    result += x

print(result)
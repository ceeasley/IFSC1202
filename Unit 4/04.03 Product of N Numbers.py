#In mathematics, the factorial of an integer N, denoted by N! is the following product:
#    N! = 1 × 2 × … × N
#For the given integer N, calculate the value N!
#Don't use math module in this exercise.

result = 1
N = int(input("Enter number: "))

for i in range(1,N+1):
    result = result * i

print(result)
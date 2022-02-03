#N numbers are given in the input. Read them and print their product.
#The first line of input contains the integer N, which is the number of integers to follow.
#Each of the next N lines contains one integer. Print the product of these N integers.

result = 1
N = int(input("Enter N: "))

for i in range(N):
    x = int(input("Enter number: "))
    result = result * x

print(result)
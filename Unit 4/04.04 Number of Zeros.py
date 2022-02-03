#Given N numbers: the first number in the input is N, after that N integers are given.
#Count the number of zeros among the given integers and print it.
#You need to count the numbers that are equal to zero, not the number of zero digits.

result = 0
N = int(input("Enter N: "))

for i in range(N):
    x = int(input("Enter number: "))
    if x == 0:
        result = result + 1
    else:
        pass

print("Number of zeros: ", result)
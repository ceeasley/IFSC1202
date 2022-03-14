nums = input("Enter Values Separated by Spaces: ")
numlist = [nums.split()]

for i in range(1, len(numlist),2):
    print(numlist[i])
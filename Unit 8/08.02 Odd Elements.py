nums = input("Enter Values Separated by Spaces: ")
numlist = nums.split()

for i in range(len(numlist)):
    if (int(numlist[i]) % 2) != 0:
        print(numlist[i])
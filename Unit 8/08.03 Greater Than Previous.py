nums = input("Enter Values Separated by Spaces: ")
numlist = nums.split()
x = int(numlist[0])

for i in range(len(numlist)):
    if int(numlist[i]) > x:
        print(numlist[i])
    x = int(numlist[i])
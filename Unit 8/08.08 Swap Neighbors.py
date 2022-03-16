nums = input("Enter Values in Ascending Order, Separated by Spaces: ")
numlist = nums.split()

if len(numlist) % 2 == 0:
    for i in range(0, len(numlist), 2):
        x = numlist[i]
        y = numlist[i+1]
        print(f"{y} {x}",end=" ")
    print()
else:
    for i in range(0, len(numlist)-1, 2):
        x = numlist[i]
        y = numlist[i+1]
        print(f"{y} {x}",end=" ")
    print(numlist[len(numlist)-1])
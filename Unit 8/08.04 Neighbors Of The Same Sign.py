nums = input("Enter Values Separated by Spaces: ")
numlist = nums.split()

y=0

for i in range(len(numlist)):
    x = int(numlist[i])
    if x > 0 and y > 0:
        print(f'{y} {x}')
    if x < 0 and y < 0:
        print(f'{y} {x}')
    y = x

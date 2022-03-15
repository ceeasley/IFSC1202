nums = input("Enter Values Separated by Spaces: ")
numlist = nums.split()

count = 0

for i in range(1, len(numlist)-1):
    x = int(numlist[i-1])
    y = int(numlist[i])
    z = int(numlist[i+1])
    if y > x and y > z:
        count += 1

print(count)
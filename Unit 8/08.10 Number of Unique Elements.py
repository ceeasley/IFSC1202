nums = input("Enter Values Separated by Spaces: ")
numlist = nums.split()
newlist = []
for i in range(len(numlist)):
    count = 1
    for j in range(i+1, len(numlist)):
        if numlist[i] == numlist[j]:
            count += 1
    for j in range(0, i-1):
        if numlist[i] == numlist[j]:
            count += 1
    if count == 1:
        newlist += numlist[i]
    
for i in range(len(newlist)):
    print(newlist[i], end=" ")
print()
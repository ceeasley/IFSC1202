nums = input("Enter Values Separated by Spaces: ")
numlist = nums.split()

maximum = int(numlist[0])
minimum = int(numlist[0])

for i in range(len(numlist)):
    if int(numlist[i]) > maximum:
        maxindex = i
        maximum = int(numlist[i])
    if int(numlist[i]) < minimum:
        minindex = i
        minimum = int(numlist[i])
numlist[minindex], numlist[maxindex] = numlist[maxindex], numlist[minindex]
for i in range(len(numlist)):
    print(numlist[i], end=" ")
print()
nums = input("Enter Values in Ascending Order, Separated by Spaces: ")
numlist = nums.split()

count = len(numlist)

for i in range(1, len(numlist)):
    if (numlist[i] == numlist [i-1]):
        count -= 1
print(f"Number of Distinct Elements: {count}")
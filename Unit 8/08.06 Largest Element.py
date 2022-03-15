nums = input("Enter Values Separated by Spaces: ")
numlist = nums.split()

x = 0
index = 0

for i in range(len(numlist)):
    if int(numlist[i]) > x:
        x = int(numlist[i])
        index = i

print(f"Largest Value: {x}\nIndex of Largest Value: {index}")
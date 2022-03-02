x = input("Enter a string: ")

print(x[2])
print(x[-2])
print(x[0:5])
for i in range(0, len(x)-2):
    print(x[i],end="")
print("\n"+x[::2])
print(x[1::2])
for i in range(-1,-len(x)-1, -1):
    print(x[i],end="")
print()
for i in range(-1,-len(x)-1, -2):
    print(x[i],end="")
print()
print(len(x))
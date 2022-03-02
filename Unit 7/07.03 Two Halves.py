x = input("Enter a string: ")
y = len(x)

x1 = slice(0,y//2)
x2 = slice(y//2, y)

print(x[x2]+x[x1])
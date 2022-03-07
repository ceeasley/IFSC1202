x = input("Enter a string: ")
fcount = 0

if x.find("f") != -1:
    y = x.find("f")
    if x.find("f", y+1) != -1:
        print(x.find("f", y+1))
    else:
        print("One f")
else:
    print("Zero f")
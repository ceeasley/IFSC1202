x = input("Enter a string: ")

if x.find("f") != -1:
    print(x.find("f"), end=" ")
    if x.rfind("f") != x.find("f"):
        print(x.rfind("f"))
    print()
else:
    print(0)

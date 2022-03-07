x = input("Enter a string containing at least two 'h's: ")

y = x.find("h")
z = x.rfind("h")

print(x[:y]+x[z+1:])
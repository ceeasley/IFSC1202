def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

def scale_list(a,s):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = int(a[i][j])*s
    return a

with open("09.03 NumbersList.txt") as lines:
    array = []
    for line in lines:
        row = line.split()
        array.append(row)
    print_list(array)
    x = int(input("Enter scale value: "))
    scaled = scale_list(array, x)
    print_list(scaled)
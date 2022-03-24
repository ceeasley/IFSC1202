def print_list(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

def swap_columns(a,i,j):
    for x in range(len(a)):
        a[x][i], a[x][j] = a[x][j], a[x][i]

with open("09.02 NumbersList.txt") as lines:
    array = []
    for line in lines:
        row = line.split()
        array.append(row)
print_list(array)
swap = input("Enter the columns to swap: ")
columns = swap.split()
x = int(columns[0])
y = int(columns[1])
print_list(swap_columns(array,x,y))
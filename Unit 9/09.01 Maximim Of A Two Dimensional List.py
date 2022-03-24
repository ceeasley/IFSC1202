xy = input("Enter the number of rows and columns: ")
tablelist = xy.split()
rows = int(tablelist[0])
columns = tablelist[1]
array = []
for i in range(rows):
    row = input(f"Row {i+1}: Enter {columns} values separated by spaces: ")
    rowdata = row.split()
    array.append(rowdata)

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
    print()

maxval = 0
x = 1
y = 1

for i in range(len(array)):
    for j in range(len(array[i])):
        if maxval < int(array[i][j]):
            maxval = int(array[i][j])
            maxcol = x
            maxrow = y
        x += 1
    y += 1
    x = 1
print(f"The maximum value '{maxval}' occurred in Row {maxrow}, Column {maxcol}")
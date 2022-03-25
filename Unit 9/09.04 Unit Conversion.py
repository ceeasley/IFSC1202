FromValue = input("Enter From Value: ")
FromUnit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
ToUnit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")

with open("09.04 Conversion.txt") as lines:
    array = []
    for line in lines:
        row = line.split()
        array.append(row)
    rowindex = 0
    colindex = 0
    multrow = False
    multcol = False
    for i in range(len(array)):
        if array[i][0] == FromUnit:
            multcol = i
        colindex += 1
    for i in range(len(array[0])):
        if array[0][i] == ToUnit:
            multrow = i
        rowindex += 1

    if multrow == multcol == False:
        print("FromUnit and ToUnit are not valid")
    elif multrow == False:
        print("FromUnit is not valid")
    elif multcol == False:
        print("ToUnit is not valid")
    else:
        ToValue = float(FromValue) * float(array[multcol][multrow])
        print(f'{FromValue} {FromUnit} => {ToValue:.7} {ToUnit}')
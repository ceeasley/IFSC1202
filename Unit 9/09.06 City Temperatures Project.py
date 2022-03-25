with open("09.06 CityTemps.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            row = line.split()
            array.append(row)
    for i in range(len(array)):
        sumtemp = 0
        for j in range(1,len(array[i])):
            sumtemp += int(array[i][j])
        average = int(sumtemp/(len(array[i])-1))
        array[i].append(average)

    print(f'{"City":10} {"Mo":^5} {"Tu":^5} {"We":^5} {"Th":^5} {"Fr":^5} {"Sa":^5} {"Su":^5} {"Avg":^5}')
    for i in range(len(array)):
        print(f'{array[i][0]:10}', end=' ')
        for j in range(1, len(array[i])):
            print(f'{array[i][j]:^5}', end=' ')
        print()
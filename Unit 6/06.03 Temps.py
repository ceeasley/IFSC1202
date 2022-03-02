def FahrToCel(F):
    C = (F - 32) * 5/9
    return C

with open("06.03 FTemps.txt") as temps:
    temp = temps.readline()
    with open("06.03 CTemps.text", "w") as n:
        while temp:
            n.write(f'{FahrToCel(float(temp)):5.1f}\n')
            temp = temps.readline()

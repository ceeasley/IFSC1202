def ProperCase(n):
    n = n.lower()
    n = n.capitalize()
    return n

def RemoveNewLines(n):
    x = n.replace("\n","")
    return x

def Trim(n):
    n = n.strip()
    return n

def FirstName(n):
    first = n[:n.find(" ")]
    return first

def LastName(n):
    last = n[n.rfind(" "):]
    return last

def MiddleName(n):
    middle = n[n.find(" "):n.rfind(" ")]
    return middle



with open("07.11 Names.txt") as fullnames:
    print(f'{"First":^10} {"Middle":^10} {"Last":^10}')
    print(f'{10*"-"} {10*"-"} {10*"-"}')
    name = fullnames.readlines()
    while name:
        RemoveNewLines(name)
        first = FirstName(name)
        middle = MiddleName(name)
        last = LastName(name)
        Trim(first)
        Trim(middle)
        Trim(last)
        if len(middle) == 1:
            middle = middle + "."
        ProperCase(first)
        ProperCase(middle)
        ProperCase(last)
        print(f'{first:10} {middle:10} {last:10}')




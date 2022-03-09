def ProperCase(n):
    x = n.lower()
    n = x.capitalize()
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
    start = n.find(" ")
    end = n.rfind(" ")
    middle = n[start+1:end]
    return middle

with open("07.11 Names.txt") as fullnames:
    print(f'{"First":^10} {"Middle":^10} {"Last":^10}')
    print(f'{10*"-"} {10*"-"} {10*"-"}')
    name = fullnames.readline()
    while name:
        name = RemoveNewLines(name)
        name = Trim(name)

        first = FirstName(name)
        middle = MiddleName(name)
        last = LastName(name)
        
        first = Trim(first)
        middle = Trim(middle)
        last = Trim(last)
        
        first = ProperCase(first)
        middle = ProperCase(middle)
        last = ProperCase(last)
        
        if len(middle) == 1:
            middle = middle + "."

        print(f'{first:10} {middle:10} {last:10}')
        name = fullnames.readline()
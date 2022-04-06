class Pet:
    def __init__(self, name, pettype, age):
        self.name = name
        self.pettype = pettype
        self.age = age

print(f'{"Name":10} {"Type":7} {"Age":5}')
with open ("10.01 Pets.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            line = line.replace(",","")
            row = line.split()
            array.append(row)
    for i in range(len(array)):
        newpet = Pet(array[i][0],array[i][1],array[i][2])
        print(f'{newpet.name:10} {newpet.pettype:7} {newpet.age:5}')
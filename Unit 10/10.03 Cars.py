class Car:
    def __init__(self, year, make, speed=0):
        self.year = year
        self.make = make
        self.speed = speed
    def accelerate(self, change):
        self.speed += change
        return self.speed
    def brake(self, change):
        self.speed += change
        return self.speed

with open ("10.03 Cars.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            line = line.replace(",","")
            row = line.split()
            array.append(row)
    newcar = Car(array[0][0],array[0][1])
    print(f'Make: {newcar.make}\nYear: {newcar.year}')
    print(f'{"Change":^7} {"Speed":^7}')
    for i in range(1,len(array)):
        if int(array[i][0]) > 0:
            newspeed = newcar.accelerate(int(array[i][0]))
            print(f'{array[i][0]:^7} {newspeed:^7}')
        else:
            newspeed = newcar.brake(int(array[i][0]))
            print(f'{array[i][0]:^7} {newspeed:^7}')
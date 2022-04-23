class Sketch:
    def __init__(self, size, xpos=0, ypos=0, direction="U", pen="U", canvas=[]):
        self.size = size
        self.xpos = xpos
        self.ypos = ypos
        self. direction = direction
        self.pen = pen
        self.canvas = canvas
    def printsketch(self):
        print("+"+("-"*int(self.size))+"+")
        for i in range(len(self.canvas)):
            print("|",end="")
            for j in range(len(self.canvas[i])):
                print(self.canvas[i][j],end="")
            print("|\n")
        print("+"+("-"*int(self.size))+"+")
        print (f'X = {self.xpos}  Y = {self.ypos}  Direction = {self.direction}')
    def penup(self):
        self.pen = "U"
    def pendown(self):
        self.pen = "D"
    def turnleft(self):
        if self.direction == "U":
            self.direction = "L"
        elif self.direction == "L":
            self.direction = "D"
        elif self.direction == "D":
            self.direction = "R"
        elif self.direction == "R":
            self.direction = "U"
    def turnright(self):
        if self.direction == "U":
            self.direction = "R"
        elif self.direction == "L":
            self.direction = "U"
        elif self.direction == "D":
            self.direction = "L"
        elif self.direction == "R":
            self.direction = "D"
    def move(self, distance):
        initialx = self.xpos
        initialy = self.ypos
        if self.direction == "R":
            finaly = int(self.ypos) + distance
            if finaly >= int(self.size):
                finaly = int(self.size)-1
            if self.pen == "D":
                for i in range(finaly-self.ypos):
                    self.canvas[initialx][self.ypos + i] = '*'
            finalx = self.xpos
        elif self.direction == "L":
            finaly = int(self.ypos) - distance
            if finaly < 0:
                finaly = 0
            if self.pen == "D":
                for i in range(self.ypos-finaly):
                    self.canvas[initialx][self.ypos-i] = '*'
                    self.ypos -= 1
            finalx = self.xpos
        elif self.direction == "U":
            finalx = int(self.xpos) + distance
            if finalx >= int(self.size):
                finalx = int(self.size)-1
            if self.pen == "D":
                for i in range(finalx-self.xpos):
                    self.canvas[self.xpos + i][initialy] = '*'
            finaly = self.ypos
        elif self.direction == "D":
            finalx = int(self.xpos) - distance
            if finalx < 0:
                finalx = 0
            if self.pen == "D":
                for i in range(finalx-self.xpos):
                    self.canvas[self.xpos - i][initialy] = '*'
            finaly = self.ypos
        self.xpos = finalx
        self.ypos = finaly
with open("Cshape.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            row = line.split(",")
            for i in range(len(row)):
                row[i] = row[i].strip()
            array.append(row)
    newsketch = Sketch(array[0][0])
    newsketch.canvas = int(newsketch.size)*[int(newsketch.size)*[" "]]
    for i in range(1,len(array)):
        if int(array[i][0]) == 1:
            newsketch.penup()
        elif int(array[i][0]) == 2:
            newsketch.pendown()
        elif int(array[i][0]) == 3:
            newsketch.turnright()
        elif int(array[i][0]) == 4:
            newsketch.turnleft()
        elif int(array[i][0]) == 5:
            newsketch.move(int(array[i][1]))
        elif int(array[i][0]) == 6:
            newsketch.printsketch()
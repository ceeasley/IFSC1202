from math import sqrt, atan, pi
# Step 1 - Define the class object "Point"
class Point:
# Step 2 - Define the initializer and any default values
    def __init__(self, Xvalue, Yvalue):
# Step 3 - Define the object attributes
        self.x = Xvalue
        self.y = Yvalue
# Step 4 - Define the methods for the object
# ToString returns a nicely formated string to represent the data point
    def ToString(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def Distance(self, other):
        distance = sqrt((other.x - self.x)**2+(other.y-self.y)**2)
        return distance
    def MidPoint(self, other):
        midx = (other.x + self.x)/2
        midy = (other.y + self.y)/2
        return f'({midx}, {midy})'
    def XAngle(self, other):
        slope = (other.y - self.y)/(other.x - self.y)
        xangle = atan(slope)*180/pi
        return xangle

with open("10.05 Points.txt") as lines:
    array = []
    for line in lines:
        if line != "\n":
            row = line.split(",")
            array.append(row)
    print(f'{"Point A":^17} {"Point B":^17} {"Distance":^17} {"Midpoint":^17} {"Angle":^17}')
    print(("-"*17+" ")*5)
    for i in range(len(array)):
        PointA = Point(float(array[i][0]), float(array[i][1]))
        PointB = Point(float(array[i][2]), float(array[i][3]))
        print(f'{PointA.ToString():17} {PointB.ToString():17} {PointA.Distance(PointB):<17.7f} {PointA.MidPoint(PointB):17} {PointA.XAngle(PointB):<17.7f}')
#Given the coordinates of the three points A, B, and C on a line, print a distance from the point A to closest point to it.
#Hint: Determine the distance from A to B by subtracting B from A, then determine the distance from A to C by subtracting C from A. Determine the smallest distance.

a = int(input("Enter Point A: "))
b = int(input("Enter Point B: "))
c = int(input("Enter Point C: "))

ab = abs(b-a)
ac = abs(c-a)

if ab > ac: 
    print(ac)
else:
    print(ab)
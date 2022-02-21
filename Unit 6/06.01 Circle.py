#You have a file that has the radius of a circle, one per line.
#Create a program that performs the following:
#    Defines a function called "diameter"
#        Accepts the radius (floating point) as a parameter
#        Calculates and returns the diameter of the circle, (2 times radius)
#    Defines a function called "circumference"
#        Accepts the radius (floating point) as a parameter
#        Calculates and returns the circumference of the circle, (2 times pi times radius)
#    Defines a function called "area"
#        Accepts the radius (floating point) as a parameter
#        Calculates and returns the area of the circle, (pi times radius squared)
#Opens and reads the 06.01 Radius.txt file
#Calculates and prints the radius, diameter, circumference, and area on a line. (each value is 15 columns wide, 5 decimal digits, and a space seperating each column.
#Print headings that right align with the data.
from math import pi

def diameter(n):
    diam = 2*n
    return diam

def circumference(n):
    circ = 2*n*pi
    return circ

def area(n):
    area_r = pi*(n**2)
    return area_r

with open("06.01 Radius.txt") as radii:
    radius = radii.readline()
    print(f'{"Radius":^15} {"Diameter":^15} {"Circumference":^15} {"Area":^15}')
    
    while radius:
        print(f"{float(radius):>15.5f} {diameter(float(radius)):>15.5f} {circumference(float(radius)):>15.5f} {area(float(radius)):>15.5f}")
        radius = radii.readline()


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


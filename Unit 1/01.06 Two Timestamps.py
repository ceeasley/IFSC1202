#A timestamp consists of three numbers:
#    number of hours
#    number of minutes
#    number of seconds
#Given two timestamps, calculate how many seconds are between them.
#Assume that the moment of the first timestamp occurred before the moment of the second timestamp.

h1 = int(input("Enter hours for the first timestamp: "))
m1 = int(input("Enter minutes for the first timestamp: "))
s1 = int(input("Enter seconds for the first timestamp: "))

h2 = int(input("Enter hours for the second timestamp: "))
m2 = int(input("Enter minutes for the second timestamp: "))
s2 = int(input("Enter seconds for the second timestamp: "))

timestamp1 = (h1*3600) + (m1*60) + s1
timestamp2 = (h2*3600) + (m2*60) + s2

diff = timestamp2 - timestamp1

print(str(diff)+" seconds elapsed between these two timestamps.")
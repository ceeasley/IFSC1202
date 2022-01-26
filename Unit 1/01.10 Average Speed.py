#Write a program that prompts for the length of a race in kilometers, then prompts for the number of minutes and number of seconds needed to run the race.
#Display the average speed in Miles per Hour
#Hint: Use the int() function to convert your input to an integer.
#Hint: There are 1.61 kilometers in a mile.

km = int(input("Length of race (km): "))
minutes = int(input("Duration of race (min): "))
seconds = int(input("Duration of race (sec): "))

time = (minutes/60) + (seconds/3600)

miles = km/1.61

speed = miles/time

print("This race was run at "+str(speed)+" miles per hour.")
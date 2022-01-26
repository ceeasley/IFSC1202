#Write a program that prompts for the number of minutes and number of seconds.
#Display the total number of seconds.

minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

time = (minutes * 60) + seconds

print(str(time)+" seconds")
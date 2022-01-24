#Write a program that prompts for an integer number and prints its previous and next numbers.
#Display the results exactly as shown below. There shouldn't be a space before the period.
#Remember that you can convert the numbers to strings using the function 'str'.

#Example:
#Enter Number: 179
#The next number for the number 179 is 180.
#The previous number for the number 179 is 178.

a = int(input("Enter a number: "))

prev = a-1
cons = a+1

print("The next number for the number "+str(a)+" is "+str(cons)+".")
print("The previous number for the number "+str(a)+" is "+str(prev)+".")
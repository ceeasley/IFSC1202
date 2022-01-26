#Prompt for two two-digit numbers.
#Merge them into single number as follows:
#    Tens digit from first number
#    Tens digit from second number
#    Units digit from first number
#    Units digit form second number
#Use only math for your solution; do no use any string functions.

a = int(input("Enter a two digit number: "))
b = int(input("Enter another two digit number: "))

tens1 = a//10
ones1 = a%10

tens2 = b//10
ones2 = b%10

print("{}{}{}{}".format(tens1,tens2,ones1,ones2))
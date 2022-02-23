#Create a python solution that performs the following:
#    Creates a function called isEven that accepts and integer and returns True if it is even and False if it is odd.
#    Creates a function called isOdd that accepts and integer and returns True if it is odd and False if it is even
#    Creates a function called isPrime that accepts and integer and returns True if it is prime and False if it is not prime. Remember that prime numbers have to be greater than 1.
#    Opens a file for input that contains integers, one per line (06.06 Numbers.txt)
#    Opens a file for output that will contain the even numbers (06.06 Evennumbers.txt)
#    Opens a file for output that will contain the odd numbers (06.06 Oddnumbers.txt)
#    Opens a file for output that will contain the prime numbers (06.06 Primenumbers.txt)
#    Reads each line of "06.06 Numbers.txt" and convert to an integer
#    Uses the isEven function to determine if the integer it even. If true, writes the integer to 06.06 Evennumbers.txt (one integer per line)
#    Uses the isOdd functon to determine if the integer is odd. If true, writes the integer to 06.06 Oddnumbers.txt (one integer per line),
#    Uses the isPrime functon to determine if the integer is prime. If true, writes the integer to 06.06 Primenumbers.txt (one integer per line),
#When finished, closes all of the files
#Displays a count of numbers in 06.06 Evennumbers.txt, 06.06 Oddnumbers.txt, 06.06 Primenumbers.txt, and 06.06 Numbers.txt
#Remember that constant for a True value is "True" not "true" and the constant value for a False value is "False" not "false".

def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False

def isOdd(n):
    if n%2 != 0:
        return True
    else:
        return False

def isPrime(n):
    if n > 1:
        ans = True
        for i in range(2,(n//2)+1):
            if (n%i) == 0:
                ans = False
    else:
        ans = False
    return ans
            

count = 0
evennum = 0
oddnum = 0
primenum = 0

with open("06.06 Numbers.txt") as numbers:
    number = numbers.readline()

    with open("06.06 Evennumbers.txt", "w") as even, open("06.06 Oddnumbers.txt", "w") as odd, open("06.06 Primenumbers.txt", "w") as prime:
        while number:
            if isEven(int(number)) is True:
                even.write(number)
                evennum += 1
            if isOdd(int(number)) is True:
                odd.write(number)
                oddnum += 1
            if isPrime(int(number)) is True:
                prime.write(number)
                primenum += 1
            count += 1
            number = numbers.readline()

print(f'{evennum} even numbers\n{oddnum} odd numbers\n{primenum} prime numbers\n{count} numbers read')
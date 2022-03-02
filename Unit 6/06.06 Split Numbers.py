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
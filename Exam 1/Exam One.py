# Write a python program in which the computer thinks of a random number from 1 to 20 and askes you to guess it. The computer will tell you if each guess is too high or too low. As closely as possible, follow the examples below.

#    Import the radint function from the random library. (See Unit 5) (20 points) (Hint: use randint)
#    Prompt for the user's name. (20 points) (Hint: use an input statement)
#    Display a greeting with the user's name and the number of guesses. (20 points) (Hint: use a print statement)
#    Have the computer generate a random number between 1 and 20. (See Unit 5) (20 points) (Hint: use randint)
#    Play the game for 5 rounds. (20 points) (Hint: use a FOR or a While Loop)
#    Prompt the user for a guess. (20 points) (Hint use an input statement and convert input to an integer)
#    If the guess is greater than the random number, print a message. (20 points) (Hint: use an IF statement and a print statement)
#    If the guess is less than the random number, print a message. (20 points) (Hint: use an IF statement and a print statement)
#    If the guess is equal to the random number, print a message with the user name and the number of guesses used. The game ends. (20 points) (Hint: use an IF statement and a print statement)
#    If the user exceeds the number of guesses, print a message with the random number. The game ends. (20 points) (Hint: use an IF statement and a print statement)

from random import randint 

x = randint(1,20)
count = 0
name = input("Hello! What is your name? ")

print("Well, {}, I am thinking of a number between 1 and 20.\nYou will have 5 guesses.".format(name))

for i in range(5):
    y = int(input("Take a guess: "))

    if x == y:
        count += 1
        print("Good job, {}! You guessed my number in {} guess(es)!".format(name,count))
        break
    if x < y:
        count += 1
        print("Your guess is too high.")
    if x > y:
        count += 1
        print("Your guess is too low.")
if x != y:
    print("Sorry, {}! The number I was thinking of was {}.".format(name, x))



#There was a set of cards with numbers from 1 to N. One of the card is now lost.
#Determine the number on that lost card given the numbers for the remaining cards.
#Hint: This solution has three parts. Suppose you have 10 cards.
#    First, sum the values from 1 to 10. This the total value of the cards.
#    Next, read each card (there will be 9 of them) and sum of their values.
#    Finally, subract the two sums. The difference is the missing card.

N = int(input("Enter number of cards: "))
x = 0
z = 0

for i in range(1,N+1):
    x += i

for i in range(1,N):
    y = int(input("Enter card: "))
    z += y

result = x - z

print("Missing card: {}".format(result))
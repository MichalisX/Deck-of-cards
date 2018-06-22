# Creating a deck of cards
import random
import itertools

suits = ['spades', 'hearts', 'clubs', 'diamonds']
vals = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
spades=hearts=clubs=diamonds=0

deck = list (itertools.product(vals, suits))

random.shuffle(deck)

#for vals, suits in deck:
#    print((vals, suits), end=' - ')

print(' ')
hold = [deck[i] for i in range(0,7)]
print('Hand = ', hold[0], hold[1])
print('Board = ', hold[2], hold[3], hold[4], hold[5], hold[6])

for vals, suits in hold:
    if suits=='spades':
        spades=spades+1
    if suits=='hearts':
        hearts=hearts+1
    if suits=='clubs':
        clubs=clubs+1
    if suits=='diamonds':
        diamonds=diamonds+1

print(spades, ' spades,', hearts, ' hearts, ', clubs, ' clubs, ', diamonds, ' diamonds.')

if max(spades, hearts, clubs, diamonds)>=5:
    print('You have a flush')






# Finding poker hands in a deck of cards
import random
import itertools


suits = ['spades', 'hearts', 'clubs', 'diamonds']
vals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
face_cards = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

# Converting face cards to numbers
def make_number(card):
    if card[0].isnumeric():
        return int(card[0])
    else:
        return face_cards[card[0]]

# Checking if a hand is a flush
def is_flush(hand):
    test_suit = hand[0][1]
    return all(card[1] == test_suit for card in hand)

# Initializing values
flush = pair = straight = 0
keep_max = keep_min = 0
str_flush = just_flush = 0
player_had_nothing = player_had_pair = player_had_twopair = player_had_trips = 0
player_had_straight = player_had_flush = player_had_full = player_had_quads = 0
player_had_straigh_flush = 0

##################### RUN TIMES
run_times = 1000000
counter = run_times
print('Run for %d' % run_times, 'times')
#####################

deck = list (itertools.product(vals, suits))

while counter>0:
    random.shuffle(deck)        # Shuffles the deck

    hold = [deck[i] for i in range(0, 7)]    # Selects 2 first cards for hand and 5 for the board

    # Checking all possible 2 card combinations for pairs
    for a, b in itertools.combinations(hold,2):
        if a[0]==b[0]:
            pair=pair+1

    # Checking all 5-card combinations for a straight
    s = []
    for a in hold:
        if make_number(a[0]) not in s:
            s.append(make_number(a[0]))
            if make_number(a[0]) == 14:
                s.append(1)

    for b in itertools.combinations(s, 5):
        if max(b) - min(b) == 4:
            straight = 1
            keep_max=max(b)
            keep_min=min(b)

    # Checking all 5-card combinations for a flush
    for a in itertools.combinations(hold, 5):
        if is_flush(a):     # check for straight flush
            if straight==1:
                new_max = 0
                new_min = 15
                if keep_max==5:     # Case A, 2, 3, 4, 5
                    for b in a:
                        test = make_number(b[0])
                        if test==14:
                            test=1
                        if new_max < test:
                            new_max = test
                        if new_min > test:
                            new_min = test
                else:               # All other cases
                    for b in a:
                        if new_max < make_number(b[0]):
                            new_max = make_number(b[0])
                        if new_min > make_number(b[0]):
                            new_min = make_number(b[0])

                if keep_max==new_max and keep_min== new_min:
                    str_flush=1
                else:
                    just_flush=1
            else:
                just_flush=1

    # Based on the number of pairs decide on the hand
    if pair==1:
        player_had_pair=player_had_pair+1
    elif pair==2:
        player_had_twopair=player_had_twopair+1
    elif pair==3:
        player_had_trips=player_had_trips+1
    elif pair==4 or pair==5:
        player_had_full=player_had_full+1
    elif pair>5:
        player_had_quads=player_had_quads+1
    else:
        pass

    if str_flush == 1:
        player_had_straigh_flush=player_had_straigh_flush+1
        flush = 0
        straight = 0
    elif str_flush==0 and just_flush==1:
        flush = 1
        straight = 0
    elif str_flush==0 and just_flush==0 and straight==1:
        straight ==1
    else:
        pass

    if flush == 1:
        player_had_flush = player_had_flush + 1

    if straight ==1:
        player_had_straight = player_had_straight +1


    counter=counter-1
    keep_max = keep_min = 0
    flush=pair=straight=0
    just_flush=str_flush=0

player_had_nothing=run_times -\
                   player_had_pair -\
                   player_had_twopair - \
                   player_had_trips -\
                   player_had_straight -\
                   player_had_flush -\
                   player_had_full -\
                   player_had_quads -\
                   player_had_straigh_flush
print('')
print('RESULTS')
print ('Hands with nothing    = ', player_had_nothing, end=' hands, ')
print ("%.2f" % (player_had_nothing/run_times*100),'%')
print ('Hands with a pair     = ', player_had_pair, end=' hands, ')
print ("%.2f" % (player_had_pair/run_times*100), '%')
print ('Hands with two pairs  = ', player_had_twopair, end=' hands, ')
print ("%.2f" % (player_had_twopair/run_times*100), '%')
print ('Hands with trips      = ', player_had_trips, end=' hands, ')
print ("%.2f" % (player_had_trips/run_times*100), '%')
print ('Hands with straight   = ', player_had_straight, end=' hands, ')
print ("%.2f" % (player_had_straight/run_times*100), '%')
print ('Hands with flush      = ', player_had_flush, end=' hands, ')
print ("%.2f" % (player_had_flush/run_times*100), '%')
print ('Hands with full house = ', player_had_full, end=' hands, ')
print ("%.2f" % (player_had_full/run_times*100), '%')
print ('Hands with quads      = ', player_had_quads, end=' hands, ')
print ("%.2f" % (player_had_quads/run_times*100), '%')
print ('Hands with str flush  = ', player_had_straigh_flush, end=' hands, ')
print ("%.2f" % (player_had_straigh_flush/run_times*100), '%')

# Finding poker hands in a deck of cards
import random
import itertools
import time

start = time.time()

suits = ['s', 'h', 'c', 'd']
vals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
face_cards = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
value='No hand'

def test_hand(card):
    if card[0] in vals and card[2] in vals and card[1] in suits and card[3] in suits:
        if card[0] == card[2] and card[1] == card[3]:
            return 0
        else:
            return 1
    else:
        return 0

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
str_flush = just_flush = royal_flush = 0
player_had_nothing = player_had_pair = player_had_twopair = player_had_trips = 0
player_had_straight = player_had_flush = player_had_full = player_had_quads = 0
player_had_straigh_flush = player_had_royal_flush = 0
start_pair = start_ak = start_suit = start_connectors = start_suited_connectors = 0
#choose_hand = 0


run_times=int(input("How many times you want me to run: "))
#custom_hand=input("Do you want to enter a hand (y/n): ")
#if custom_hand=='y' or custom_hand=='yes':
#    starting_hand = str(input("Enter hand like AsKd no spaces: "))
#    while not test_hand(starting_hand):
#        starting_hand = str(input("Enter hand like AsKd no spaces: "))
#    print('Running with starting hand:', starting_hand[:4])
#    choose_hand = 1
#else:
#    print('Running with a random hand')

print('Run for', "{:,}".format(run_times), 'times')

deck = list (itertools.product(vals, suits))


counter = 1

while counter<=run_times:
    random.shuffle(deck)        # Shuffles the deck

    hold = [deck[i] for i in range(0, 7)]    # Selects 2 first cards for hand and 5 for the board

#    if choose_hand == 1:
#        pass

    hand_p = hold[0][0] + hold[0][1] + ', ' + hold[1][0] + hold[1][1]
    board = hold[2][0] + hold[2][1] + ', ' + hold[3][0] + hold[3][1] + ', ' + hold[4][0] + hold[4][1] + ', ' + \
            hold[5][0] + hold[5][1] + ', ' + hold[6][0] + hold[6][1]

    if hold[0][0]==hold[1][0]:
        start_pair = start_pair + 1
    elif (hold[0][0]=='K' and hold[1][0]=='A') or (hold[0][0]=='A' and hold[1][0]=='K'):
        start_ak = start_ak + 1
    elif hold[0][1]==hold[1][1] and (make_number(hold[0][0])-make_number(hold[1][0])==1 or make_number(hold[0][0])-make_number(hold[1][0])==-1):
        start_suited_connectors = start_suited_connectors + 1
    elif hold[0][1]==hold[1][1]:
        start_suit = start_suit + 1
    elif make_number(hold[0][0])-make_number(hold[1][0])==1 or make_number(hold[0][0])-make_number(hold[1][0])==-1:
        start_connectors = start_connectors + 1
    else:
        pass

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
                    if keep_min==10:
                        royal_flush=1
                else:
                    just_flush=1
            else:
                just_flush=1

    if str_flush == 1:
        if royal_flush==1:
            player_had_royal_flush=player_had_royal_flush+1
            pair=0
            value = 'Royal Flush!'
        else:
            player_had_straigh_flush=player_had_straigh_flush+1
            pair=0
            value = 'Straight flush'
        flush = 0
        straight = 0
    elif str_flush==0 and just_flush==1:
        flush = 1
        value = 'Flush'
        straight = 0
    elif str_flush==0 and just_flush==0 and straight==1:
        straight = 1
        value = 'Straight'
    else:
        pass

    if flush == 1:
        player_had_flush = player_had_flush + 1
        pair=0

    if straight ==1:
        player_had_straight = player_had_straight +1
        pair=0

    # Based on the number of pairs decide on the hand
    if pair==1:
        player_had_pair=player_had_pair+1
        value='One pair'
    elif pair==2:
        player_had_twopair=player_had_twopair+1
        value = 'Two pairs'
    elif pair==3:
        if len(s)==4:
            player_had_twopair = player_had_twopair + 1
            value = 'Two pairs'
        else:
            player_had_trips=player_had_trips+1
            value = 'Three of a kind'
    elif pair==4 or pair==5:
        player_had_full=player_had_full+1
        value = 'Full house'
    elif pair>5:
        player_had_quads=player_had_quads+1
        value = 'Four of a kind'
    else:
        pass


    if pair==0 and flush==0 and straight==0 and str_flush==0 and royal_flush==0:
        player_had_nothing=player_had_nothing+1

    if counter % 10000 == 0:
        print('Hand', "{:,}".format(counter), ' = ', hand_p, end='.   ')
        print('Board:', board, end='.')
        print('  Value =', value)

    counter = counter + 1
    keep_max = keep_min = 0
    flush = pair = straight = 0
    just_flush = str_flush = royal_flush = 0
    value = 'No hand'

print('')
print('STARTING HAND RESULTS')
print ('Starting hands with any pair                         = ', "{:,}".format(start_pair), end=' hands, ')
print ("%.3f" % (start_pair/run_times*100),'%')
print ('Starting hands with any AK (suited or not)           = ', "{:,}".format(start_ak), end=' hands, ')
print ("%.3f" % (start_ak/run_times*100),'%')
print ('Starting hands with suited connectors (not AK or A2) = ', "{:,}".format(start_suited_connectors), end=' hands, ')
print ("%.3f" % (start_suited_connectors/run_times*100),'%')
print ('Starting hands with any other suited hand            = ', "{:,}".format(start_suit), end=' hands, ')
print ("%.3f" % (start_suit/run_times*100),'%')
print ('Starting hands with any other connectors (not suited)= ', "{:,}".format(start_connectors), end=' hands, ')
print ("%.3f" % (start_connectors/run_times*100),'%')

print ('FINAL RESULTS')
print ('Hands with nothing    = ', "{:,}".format(player_had_nothing), end=' hands, ')
print ("%.3f" % (player_had_nothing/run_times*100),'%')
print ('Hands with a pair     = ', "{:,}".format(player_had_pair), end=' hands, ')
print ("%.3f" % (player_had_pair/run_times*100), '%')
print ('Hands with two pairs  = ', "{:,}".format(player_had_twopair), end=' hands, ')
print ("%.3f" % (player_had_twopair/run_times*100), '%')
print ('Hands with trips      = ', "{:,}".format(player_had_trips), end=' hands, ')
print ("%.3f" % (player_had_trips/run_times*100), '%')
print ('Hands with straight   = ', "{:,}".format(player_had_straight), end=' hands, ')
print ("%.3f" % (player_had_straight/run_times*100), '%')
print ('Hands with flush      = ', "{:,}".format(player_had_flush), end=' hands, ')
print ("%.3f" % (player_had_flush/run_times*100), '%')
print ('Hands with full house = ', "{:,}".format(player_had_full), end=' hands, ')
print ("%.3f" % (player_had_full/run_times*100), '%')
print ('Hands with quads      = ', "{:,}".format(player_had_quads), end=' hands, ')
print ("%.3f" % (player_had_quads/run_times*100), '%')
print ('Hands with str flush  = ', "{:,}".format(player_had_straigh_flush), end=' hands, ')
print ("%.3f" % (player_had_straigh_flush/run_times*100), '%')
print ('Hands with ROYAL FLU  = ', "{:,}".format(player_had_royal_flush), end=' hands, ')
print ("%.3f" % (player_had_royal_flush/run_times*100), '%')

end = time.time()
print('End after: ', end-start)

with open("data/test.txt") as f:
    data = [line[:-1].split() for line in f]

# data = list of [hand, bid, score]

def get_type_score(hand):
    """
    1. Five of a kind, where all five cards have the same label: AAAAA
        len 1 max_count 5
    2. Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        len 2 max_count 4
    3. Full house, where three cards have the same label, and the remaining two cards share a
       different label: 23332
        len 2 max_count 3
    4. Three of a kind, where three cards have the same label, and the remaining two cards are 
       each different from any other card in the hand: TTT98
        len 3 max_count 3
    5. Two pair, where two cards share one label, two other cards share a second label, and the 
       remaining card has a third label: 23432
        len 3 max_count 2
    6. One pair, where two cards share one label, and the other three cards have a different label 
       from the pair and each other: A23A4
        len 4 max_count 2
    7. High card, where all cards' labels are distinct: 23456
        len 5 max_count 1
    score = len * 10000000 / max_count
    LOWER SCORE IS BETTER
    """
    labels = {} # elem is label, num of cards with that label
    for card in hand:
        labels[card] = 1 if card not in labels else labels[card]+1
    #print(labels, "len", len(list(labels.keys())), "max_count", labels[max(labels, key = lambda x: labels[x])]  )
    return len(list(labels.keys()))*10 / labels[max(labels, key = lambda x: labels[x])]

for i in range(len(data)):
    score_type = get_type_score(data[i][0])
    """
    If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. 
    If these cards are different, the hand with the stronger first card is considered stronger. 
    If the first card in each hand have the same label, however, then move on to considering the second card in each hand. 
    If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, 
    then the fourth, then the fifth.
    """
    # In the end, the cards are hex numbers, where T=A, J=B, Q=C, K=D, A=E
    score_cards = int(data[i][0].replace("A","E").replace("K","D").replace("Q","C").replace("J","B").replace("T", "A"), 16)
    data[i].append(score_type + 0.9 / score_cards)
    #print("hand:", data[i][0], "score:", score_type, score_cards, "=>",data[i][2])
    

data = sorted(data, key=lambda x: x[2], reverse=True)

winnings = 0
for i in range(len(data)):
    winnings += (i+1) * int(data[i][1])
    print("rank:", i+1, "hand:", data[i][0], "score:", data[i][2], "bid:", data[i][1])

print("first star:", winnings)

"""
SECOND STAR
J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.
J cards are now the weakest individual cards (order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.)
"""

for i in range(len(data)):
    score_s2 = 0
    data[i].append(score_s2)


data = sorted(data, key=lambda x: x[3], reverse=True)

winnings = 0
for i in range(len(data)):
    winnings += (i+1) * int(data[i][1])
    print("rank:", i+1, "hand:", data[i][0], "score:", data[i][3], "bid:", data[i][1])

print("second star:", winnings)

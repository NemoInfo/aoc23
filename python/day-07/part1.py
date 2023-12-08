from collections import defaultdict

hands = [(line.split()[0], int(line.split()[1])) for line in open(0)]

cards = "23456789TJQKA"
value = {card: i for i, card in enumerate(cards)}

def type(cards):
    d = defaultdict(int)
    for card in cards:
        d[card] += 1

    if len(d) == 1:
        return 6
    if len(d) == 2:
        if 4 in d.values():
            return 5
        return 4
    if len(d) == 3:
        if 3 in d.values():
            return 3
        return 2
    if len(d) == 4:
        return 1
    return 0

def score(hand):
    return list(map(lambda x: value[x], hand))

hands.sort(key=lambda x: (type(x[0]), score(x[0])))

s = 0
for rank, (_, bet) in enumerate(hands, 1):
    s += bet * rank

print(s)

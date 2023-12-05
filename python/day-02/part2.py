import re
import math

s = 0
for i, x in enumerate(open(0)):
    w = " ".join(x.split()[2:])
    vec = re.split(" |; |, ", w)

    maxes = {color: 0 for color in ["red", "green", "blue"]}

    counts, colors = [*map(int, vec[0::2])], vec[1::2]
    for count, color in zip(counts, colors):
        maxes[color] = max(maxes[color], count)

    s += math.prod([*maxes.values()])

print(s)

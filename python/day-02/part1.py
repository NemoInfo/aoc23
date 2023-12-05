import re

bound = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

s = 0
for i, x in enumerate(open(0)):
    w = " ".join(x.split()[2:])
    vec = re.split(" |; |, ", w)

    counts, colors = [*map(int, vec[0::2])], vec[1::2]
    for count, color in zip(counts, colors):
        if count > bound[color]:
            break
    else:
        s += i + 1

print(s)

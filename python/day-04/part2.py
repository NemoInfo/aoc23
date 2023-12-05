from collections import defaultdict

d = defaultdict(int)
lines = open(0).read().splitlines()
for i, line in enumerate(lines):
    d[i] += 1
    line = line.split(":")[1].strip()
    winners, actual = [[*map(int, x.split())] for x in line.split("|")]

    count = len([*filter(lambda x: x in actual, winners)])

    for di in range(i + 1, min(len(lines), i + count + 1)):
        d[di] += d[i]


print(sum(d.values()))

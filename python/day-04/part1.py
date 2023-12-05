s = 0
for line in open(0):
    line = line.split(":")[1].strip()
    winners, actual = [[*map(int, x.split())] for x in line.split("|")]

    count = len([*filter(lambda x: x in actual, winners)])

    s += count and 1 << (count - 1)

print(s)

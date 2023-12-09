lists = [ list(map(int, line.split())) for line in open(0)]

def diff(l):
    d = []
    for i in range(len(l) - 1):
        d.append(l[i+1] - l[i])
    return d

def zero(l):
    return not any(l)

t = 0
for l in lists:
    d = l
    ends = []
    while not zero(d):
        ends.append(d[-1])
        d = diff(d)

    t += sum(ends)

print(t)

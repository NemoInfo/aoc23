ts, ds = open(0).read().splitlines()

ts = [*map(int, ts.split(":")[1].split())]
ds = [*map(int, ds.split(":")[1].split())]

s = 1
for t, d in zip(ts, ds):
    c = 0
    for b in range(0, t + 1):
        if b * (t - b) > d:
            c += 1

    s *= c

print(s)

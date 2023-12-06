from math import sqrt, ceil, floor
ts, ds = [list(map(int, line.split(":")[1].split())) for line in open(0)]

res = 1
for t, d in zip(ts, ds):
    delta = sqrt(t ** 2 - 4 * d)
    x1 = (t - delta) / 2
    x2 = (t + delta) / 2

    res *= floor(x2) - ceil(x1) + 1 - (x1 == floor(x1)) - (x2 == ceil(x2))

print(res)

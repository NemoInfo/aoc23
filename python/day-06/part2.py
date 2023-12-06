ts, ds = open(0).read().splitlines()

t = int("".join(ts.split(":")[1].split()))
d = int("".join(ds.split(":")[1].split()))

ht = t // 2 + 1
low, high = 0, ht
while low < high:
    mid = low + (high - low) // 2
    val = mid * (t - mid)
    if val <= d:
        low = mid + 1
    else:
        high = mid

res = (ht - low) * 2 - (not t & 1)
print(res)

seeds, *blocks = open(0).read().split("\n\n")

seeds = [*map(int, seeds.split(":")[1].split())]
seeds = [*map(lambda x: (x[0], x[0] + x[1]), zip(seeds[0::2], seeds[1::2]))]

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    next = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            ns = max(b, s)
            ne = min(b + c, e)

            if ns >= ne:
                continue
            next.append((ns - b + a, ne - b + a))
            if s < ns:
                seeds.append((s, ns))
            if ne < e:
                seeds.append((ne, e))
            break
        else:
            next.append((s, e))
    seeds = next

print(min(seeds)[0])

seeds, *blocks = open(0).read().split("\n\n")

seeds = [*map(int, seeds.split(":")[1].split())]

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    next = []
    for seed in seeds:
        for a, b, c in ranges:
            if b <= seed < b + c:
                next.append(seed - b + a)
                break
        else:
            next.append(seed)

    seeds = next

print(min(seeds))

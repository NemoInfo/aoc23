lines = open(0).read().splitlines()
seeds = [*map(int, lines[0].split(": ")[1].split())]

maps = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.splitlines()[1:])), "\n".join(lines).split("\n\n")[1:]))

best = 1 << 31
for seed in seeds:
    n = seed
    for ms in maps:
        for m in ms:
            if m[1] <= n < m[1] + m[2]:
                n = n - m[1] + m[0]
                break
    best = min(best, n)


print(best)

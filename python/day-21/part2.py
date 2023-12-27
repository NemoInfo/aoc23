import numpy as np

grid = open(0).read().splitlines()

start = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

def move(sources):
    new = set()
    drs = [-1, 0, 1, 0]
    dcs = [0, -1, 0, 1]
    for r, c in sources:
        for dr, dc in zip(drs, dcs):
            if grid[(r + dr) % len(grid)][(c + dc) % len(grid[0])] != "#":
                new.add((r + dr, c + dc))
    return new

def score(n):
    dp = [set() for _ in range(3)]
    dp[0].add(start)
    dp[1] = move(dp[0])
    dp[2] = move(dp[1])

    for _ in range(n - 2):
        new = dp[1].union(
            move(dp[2] - dp[0])
        )

        dp = dp[1:]
        dp.append(new)

    return len(new)

xs = [65 + i * 131 for i in range(3)]
ys = [score(x) for x in xs]

xs = np.array(xs)
ys = np.array(ys)
p = np.poly1d(np.polyfit(xs, ys, 2))

print(np.ceil(p(26501365)).astype(int))

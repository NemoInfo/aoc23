import numpy as np

BOUNDS = [200000000000000, 400000000000000]
# BOUNDS = [7, 27] # Test Bounds

stones = [[*map(int, line.strip().replace(" @", ",").split(","))] for line in open(0)]

stones = [*map(lambda x: x[:2] + x[3:-1], stones)]
lines = [*map(lambda pv: (pv[3] / pv[2], pv[1] - pv[3] / pv[2] * pv[0]), stones)]

total = 0
for i, [a, b] in enumerate(lines):
    for j, [c, d] in enumerate(lines[i+1:], i+1):
        if a == c:
            continue

        x = (d - b) / (a - c)
        y = a * x + b

        if not (BOUNDS[0] <= x <= BOUNDS[1] and
                BOUNDS[0] <= y <= BOUNDS[1]):
            continue

        if all((x - px) * vx >= 0 and (y - py) * vy >= 0
               for px, py, vx, vy in [stones[i], stones[j]]):
            total += 1

print(total)

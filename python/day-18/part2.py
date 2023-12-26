dirs = {
    "0": (0, 1),
    "1": (1, 0),
    "2": (0, -1),
    "3": (-1, 0),
}

dig = [(0, 0)]
b = 0

for line in open(0):
    hx = line.split()[-1]
    dr, dc = dirs[hx[-2]]
    n = int(hx[2:-2], 16)

    b += n
    r, c = dig[-1]
    dig.append((r + dr * n, c + dc * n))

# Shoelace Formula
A = abs(sum(
    dig[i][0] * (dig[i - 1][1] - dig[(i + 1) % len(dig)][1])
    for i in range(len(dig)))) // 2

# Pick's Theorem
i = A - b // 2 + 1

print(i + b)

patterns = [*map(str.splitlines, open(0).read().split("\n\n"))]

def check_horizontal(m):
    for r in range(1, len(m)):
        top = m[:r][::-1]
        bot = m[r:]

        top = top[:len(bot)]
        bot = bot[:len(top)]

        if top == bot:
            return r


total = 0
for pattern in patterns:
    horizontal = check_horizontal(pattern)

    if horizontal is not None:
        total += 100 * horizontal
        continue

    pattern_t = ["".join(row) for row in zip(*pattern)]

    total += check_horizontal(pattern_t)

print(total)

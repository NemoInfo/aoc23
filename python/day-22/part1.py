bricks = [list(map(int, line.replace("~", ",").split(","))) for line in open(0)]
bricks.sort(key=lambda x: x[2])

def overlap(a, b):
    if max(a[0], b[0]) <= min(a[3], b[3]) and \
       max(a[1], b[1]) <= min(a[4], b[4]):
        return True

# Drop bricks
for i, brick in enumerate(bricks):
    min_z = 1
    for other in bricks[:i]:
        if overlap(brick, other):
            min_z = max(min_z, other[5] + 1)

    brick[5] -= brick[2] - min_z
    brick[2] = min_z

bricks.sort(key=lambda x: x[2])


# Compute dependecies
dep = {id: [] for id in range(len(bricks))}
for i, brick in enumerate(bricks):
    for j, other in enumerate(bricks[:i]):
        if overlap(brick, other) and other[5] + 1 == brick[2]:
            dep[i].append(j)

# Compute dependants
sup = {id: [] for id in range(len(bricks))}
for i, dependencies in dep.items():
    for j in dependencies:
        sup[j].append(i)

total = 0
for i in sup:
    for j in sup[i]:
        if len(dep[j]) <= 1:
            break
    else:
        total += 1

print(total)

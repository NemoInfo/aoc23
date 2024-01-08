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


def remove_brick(r, removed):
    removed.add(r)

    for dependant in sup[r]:
        for dependency in dep[dependant]:
            if dependency not in removed:
                break
        else:
            remove_brick(dependant, removed)

    return len(removed) - 1


total = 0
for i in range(len(bricks)):
    total += remove_brick(i, set())

print(total)

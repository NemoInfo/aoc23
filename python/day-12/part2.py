def count(s, goal, cache=dict()):
    if s == "":
        return int(not goal)
    if not goal:
        return int("#" not in s)

    if (s, goal) in cache:
        return cache[(s, goal)]

    result = 0

    # Case 1: ? -> .
    if s[0] in ".?":
        result += count(s[1:], goal)

    # Case 2: ? -> #
    if s[0] in "#?" and \
       len(s) >= goal[0] and \
       "." not in s[:goal[0]] and \
       (len(s) == goal[0] or s[goal[0]] != "#"):
        result += count(s[goal[0] + 1:], goal[1:])

    cache[(s, goal)] = result
    return result


total = 0
for line in open(0):
    spring, goal = line.split()

    spring = "?".join([spring] * 5)
    goal = tuple(map(int, goal.split(","))) * 5

    total += count(spring, goal)

print(total)

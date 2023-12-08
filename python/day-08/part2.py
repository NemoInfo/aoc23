import math
directions, nodes = open(0).read().split("\n\n")

lr = {"L": 0, "R": 1}
directions = [*map(lambda x: lr[x], directions)]

nodes = {
    node.split(" = ")[0]: (
        node.split(" = ")[1].split(", ")[0][1:],
        node.split(" = ")[1].split(", ")[1][:-1]
    ) for node in nodes.splitlines()
}

currs = [node for node in nodes if node[-1] == "A"]
periods = []
for curr in currs:
    turn = 0
    while curr[-1] != "Z":
        curr = nodes[curr][directions[turn % len(directions)]]
        turn += 1
    periods.append(turn)

print(math.lcm(*periods))

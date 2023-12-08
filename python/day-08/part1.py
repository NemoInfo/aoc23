directions, nodes = open(0).read().split("\n\n")

lr = {"L": 0, "R": 1}
directions = [*map(lambda x: lr[x], directions)]

nodes = {
    node.split(" = ")[0]: (
        node.split(" = ")[1].split(", ")[0][1:],
        node.split(" = ")[1].split(", ")[1][:-1]
    ) for node in nodes.splitlines()
}

turn = 0
curr = "AAA"
while curr != "ZZZ":
    curr = nodes[curr][directions[turn % len(directions)]]
    turn += 1

print(turn)

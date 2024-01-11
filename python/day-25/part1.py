from collections import defaultdict, deque

graph = defaultdict(list)

for line in open(0):
    src, *neighbours = line.strip().replace(":", "").split(" ")
    for node in neighbours:
        graph[src].append(node)
        graph[node].append(src)

edges = defaultdict(lambda: 0)

for start in graph:
    q = deque([start])
    seen = {start}
    prev = {}

    while q:
        node = q.popleft()

        for neighbour in graph[node]:
            if neighbour in seen:
                continue

            seen.add(neighbour)
            q.append(neighbour)
            prev[neighbour] = node

    for node in graph:
        while node != start:
            edges[tuple(sorted(((node), (prev[node]))))] += 1
            node = prev[node]


sorted_edges = sorted(edges, key=edges.get)
print(sorted_edges[-3:])

for a, b in sorted_edges[-3:]:
    graph[a].remove(b)
    graph[b].remove(a)

start = list(graph)[0]
q = deque([start])
seen = {start}

while q:
    node = q.popleft()

    for neighbour in graph[node]:
        if neighbour in seen:
            continue

        seen.add(neighbour)
        q.append(neighbour)

total = len(seen) * (len(graph) - len(seen))
print(total)

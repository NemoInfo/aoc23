import math
from collections import deque

class Module:
    def __init__(self, outputs):
        self.outputs = outputs

class FlipFlop(Module):
    def __init__(self, outputs):
        super().__init__(outputs)
        self.mem = False

    def __repr__(self):
        return "%{out=" + ",".join(self.outputs) + ", mem=" + str(self.mem) + "}"

class Conjunction(Module):
    def __init__(self, outputs):
        super().__init__(outputs)
        self.mem = {}

    def __repr__(self):
        return "&{out=" + ",".join(self.outputs) + ", mem=" + str(self.mem) + "}"

modules = {}
broadcast_dst = []

for line in open(0):
    left, right = line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_dst = outputs
        continue
    mod_name = left[1:]
    if left[0] == "%":
        modules[mod_name] = FlipFlop(outputs)
    elif left[0] == "&":
        modules[mod_name] = Conjunction(outputs)
    else:
        raise ValueError(f"Oh shit oh fuck {left[0]}")

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and isinstance(modules[output], Conjunction):
            modules[output].mem[name] = False

[to_rx] = [name for name in modules if "rx" in modules[name].outputs]

cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if to_rx in module.outputs}

presses = 0
while True:
    q = deque([("broadcaster", dst, False) for dst in broadcast_dst])
    presses += 1
    while q:
        src, dst, signal = q.popleft()

        if dst not in modules:
            continue

        module = modules[dst]

        if dst == to_rx and signal:
            seen[src] += 1

            if src not in cycle_lengths:
                cycle_lengths[src] = presses
            else:
                assert presses == seen[src] * cycle_lengths[src]

            if all(seen.values()):
                print(math.lcm(*cycle_lengths.values()))
                exit(0)

        if isinstance(module, FlipFlop):
            if signal:
                continue
            module.mem = not module.mem
            out_signal = module.mem
        elif isinstance(module, Conjunction):
            module.mem[src] = signal
            out_signal = not all(module.mem.values())

        for output in module.outputs:
            q.append((dst, output, out_signal))


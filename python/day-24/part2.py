import sympy

stones = [[*map(int, line.strip().replace(" @", ",").split(","))] for line in open(0)]
xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr yr zr vxr vyr vzr")

equations = []
for px, py, pz, vx, vy, vz in stones[:5]:
    equations.append((xr - px) * (vy - vyr) - (yr - py) * (vx - vxr))
    equations.append((xr - px) * (vz - vzr) - (zr - pz) * (vx - vxr))

answers = sympy.solve(equations)[0]

print(answers)
print(answers[xr] + answers[yr] + answers[zr])

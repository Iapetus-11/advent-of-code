with open("input.txt", "r") as f:
    lines = [l.rstrip("\n") for l in f.readlines()]

positions =[*map(int, lines[0].split(","))]
p_min = min(positions)
p_max = max(positions)

fuel_usages = {}

for i in range(p_min, p_max+1):
    fuel = 0
    for p in positions:
        steps = abs(i - p)
        fuel += (steps**2)//2+(steps-(steps//2))

    fuel_usages[i] = fuel

print(min(fuel_usages.values()))

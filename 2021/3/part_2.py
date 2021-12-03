with open("input.txt") as f:
    lines = [l.rstrip("\n") for l in f.readlines() if l != "\n"]

oxy = None
co2 = None

og_lines = lines.copy()
ls_lines = lines.copy()

for i in range(len(lines[0])):
    ones = 0
    zeros = 0

    for l in og_lines:
        if l[i] == "0":
            zeros += 1
        else:
            ones += 1
        
    mcb = "1" if ones >= zeros else "0"

    print("oglines:", og_lines, "mcb:", mcb)
    n_lines = []
    for l in og_lines:
        print(l)
        print(" "*i + "^")
        if l[i] == mcb:
            n_lines.append(l)
    og_lines = n_lines
    if not oxy and len(og_lines) == 1:
        oxy = eval(f"0b{og_lines[0]}")

    ones = 0
    zeros = 0

    for l in ls_lines:
        if l[i] == "0":
            zeros += 1
        else:
            ones += 1
        
    lcb = "1" if zeros>ones else "0"

    n_lines = []
    for l in ls_lines:
        if l[i] == lcb:
            n_lines.append(l)
    ls_lines = n_lines
    if not co2 and len(ls_lines) == 1:
        co2 = eval(f"0b{ls_lines[0]}")

print(oxy,co2)
print(oxy*co2)

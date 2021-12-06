with open("inputshort.txt", "r") as f:
    lines = [l.rstrip("\n") for l in f.readlines()]

fish = [*map(int, lines[0].split(","))]

for i in range(80):
    for j in range(len(fish)):
        f = fish[j]
        if f == 0:
            f = 6
            fish.append(8)
        else:
            f -= 1

        fish[j] = f

print(len(fish))

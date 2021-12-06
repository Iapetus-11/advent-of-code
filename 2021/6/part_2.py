from collections import defaultdict


with open("input.txt", "r") as f:
    lines = [l.rstrip("\n") for l in f.readlines()]

fish_list = [*map(int, lines[0].split(","))]
fish = defaultdict(int)  # timer: fish_count

for f in fish_list:
    if f in fish:
        fish[f] += 1
    else:
        fish[f] = 1

for i in range(256):
    fish_0 = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7] + fish_0
    fish[7] = fish[8]
    fish[8] = fish_0
    

print(sum(fish.values()))

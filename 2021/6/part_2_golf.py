fish = [open("input.txt").read().count(str(i)) for i in range(9)]
for _ in range(256):
    fish_0 = fish[0]
    for i in range(8):
        fish[i] = fish[i+1]
        if i == 6: fish[6] += fish_0
    fish[8] = fish_0
print(sum(fish))

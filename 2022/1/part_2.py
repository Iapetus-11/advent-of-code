with open("input.txt", "r") as f:
    elves = [sum([int(n or '0') for n in g.split('\n')]) for g in f.read().split('\n\n')]
    print(sum(sorted(elves, reverse=True)[:3]))

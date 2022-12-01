with open("input.txt", "r") as f:
    print(max([sum([int(n or '0') for n in g.split('\n')]) for g in f.read().split('\n\n')]))

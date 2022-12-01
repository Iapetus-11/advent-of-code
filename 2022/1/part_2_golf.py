print(sum(sorted(sum(int(n) for n in g.split('\n') if n) for g in open("input.txt").read().split("\n\n"))[-3:]))

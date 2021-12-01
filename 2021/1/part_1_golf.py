s = [*map(int, open("input.txt").readlines()[:-1])]
print(len([x for i, x in enumerate(s, 1) if x > [9 ** 9, *s][i - 1]]))

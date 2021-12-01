s=[*map(int,open("input.txt").readlines()[:-1])];print(sum(1 for i in range(len(s))if sum(s[i:i+3])>sum(s[i-1:i+2])))

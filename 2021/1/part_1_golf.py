s=[*map(int,open("i").readlines()[:-1])];print(sum(1 for i,x in enumerate(s[1:],1)if x>s[i-1]))

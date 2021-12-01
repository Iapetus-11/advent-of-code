s=[*map(int,open("input.txt").readlines()[:-1])];print(len([x for i in range(len(s)) if (x:=sum(s[i:i+3])>sum(s[i-1:i+2]))]))

with open("input.txt")as f:s=[*map(int,f.read()[:-1].split("\n"))];print(len([x for i,x in enumerate(s,1)if x>([9**9]+s)[i-1]]))

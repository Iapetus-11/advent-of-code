print(sum(map(lambda i:(e:='ABC'.index(i[0]),y:=(e+'XYZ'.index(i[2])-1)%3,y+1+((e+1)%3==y)*6+(e==y)*3)[2],open('input.txt').readlines())))
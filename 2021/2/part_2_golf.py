a=h=d=0
for l in open("input.txt").readlines():
    o=l[0]
    v=int(l[-2])
    if o=='f':
        h+=v
        d+=a*v
    if o=='d':a+=v
    if o=='u':a-=v
print(h*d)

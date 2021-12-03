import numpy

with open("input.txt") as f:
    lines = [l for l in f.readlines() if l != "\n"]

g_rate = ""
e_rate = ""

for i in range(12):
    ones = 0
    zeros = 0
    for l in lines:
        if l[i] == "0":
            zeros += 1
        else:
            ones += 1
        
    if ones > zeros:
        g_rate += "1"
        e_rate += '0'
    else:
        g_rate += "0"
        e_rate += "1"

print(g_rate, e_rate)

print(eval(f"0b{g_rate}")*(eval(f"0b{e_rate}")))




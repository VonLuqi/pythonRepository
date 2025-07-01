n = [3]

for i in range(9):
    mult = n[i] * 2
    n.append(mult)

for num in n:
    if num in {3,6,96}: print("${}$".format(num),end=",")
    else: print("{}".format(num),end=",")
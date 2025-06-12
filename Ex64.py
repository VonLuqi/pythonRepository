n = int(input("Quer contar até qual número? "))

c = 0

while c < n:
    c += 1
    print("{} -- ".format(c),end="")
    if c % 3 == 0: print("PIN\n")
n = [0, 0, 0]
c = 0

while c < 3:
    n[c] = int(input("Digite um número: "))
    c += 1
    
print(f"A soma dos números é {sum(n)}")
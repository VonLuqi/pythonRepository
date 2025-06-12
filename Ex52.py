num = [int(input(f"Digite o número de número {i+1}: ")) for i in range(2)]

num.sort()

if len(set(num)) == 1: print("Os números são iguais, logo não existe maior ou menor")
else: print(num)
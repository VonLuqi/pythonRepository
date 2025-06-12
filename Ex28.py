salario = [float(input(f"Digite o seu salário, pessoa {i+1}\n\nR$")) for i in range(4)]

maior = max([salario[i] for i in range(len(salario))])

print(f"O maior salário entre as pessoas citadas é R${maior:.2f}!\n")
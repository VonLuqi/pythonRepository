idade = [int(input(f"Digite a idade da pessoa {i+1}: ")) for i in range(4)]

maior = max([idade[i] for i in range(len(idade))])
menor = min([idade[i] for i in range(len(idade))])

print(f"O mais jovem tem {menor} anos e o mais velho tem {maior} anos!\n")
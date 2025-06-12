n = [int(input(f"Digite o número {i+1}: ")) for i in range(3)]

par = sum(1 for num in n if num % 2 == 0)
impar = sum(1 for num in n if num % 2 != 0)

print(f"Foram encontrados {par} números pares e {impar} números ímpares!\n")
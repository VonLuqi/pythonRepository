maior_dez = 0
homens = 0
mulher_menor_vinte = 0

for i in range(4):
    while True:
        try:
            idade = int(input("Qual a sua idade? "))
            if idade <= 0:
                raise ValueError("Digite uma idade válida...")
            if idade > 10:
                maior_dez += 1
            break
        except ValueError as e:
            print(f"\nErro: {e}\n")
        
        try:
            sexo = input("Qual o seu sexo? ").strip().lower()
            if sexo not in {'m', 'masculino', 'f', 'feminino'}:
                raise ValueError("Digite um sexo válido...")
            if sexo in {'f', 'feminino'} and idade < 20:
                mulher_menor_vinte += 1
            if sexo in {'m', 'masculino'}:
                homens += 1
            break
        except ValueError as e:
            print(f"\nErro: {e}\n")
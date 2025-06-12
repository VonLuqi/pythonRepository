idade = int(input("Qual a sua idade? "))

if idade == 18:
    sexo = input("Qual o seu sexo? ").strip().lower()
    if sexo == "masculino":
        nacionalidade = input("Qual a sua nacionalidade? ").strip().lower()
        if nacionalidade == "brasileiro": print("Bem-vindo soldado!")
else: print("dispensado")
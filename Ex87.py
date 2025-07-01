import re

c = 0

def validar_nome(nome):
    if not nome or not nome.strip():
        print("\nErro: O nome não pode ser vazio.\n")
        return False
    
    if len(nome.strip()) < 3:
        print("\nErro: O nome deve ter pelo menos 3 caracteres.\n")
        return False
    
    padrao = re.compile(r"^[a-zA-ZÁ-ú ]+$")

    if padrao.match(nome):
        return True
    else:
        print("\nErro: O nome deve conter apenas letras e espaços.\n")
        return False
    

while True:
    while True:
            nome_usuario = input("Digite seu nome: (mín 3 letras) ")
            if validar_nome(nome_usuario):
                break
    while True:
        try:
            idade = int(input("Qual a sua idade? "))

            if idade <= 0:
                raise ValueError("Digite uma idade válida...")
            break
        except ValueError as e:
            print(f"\nErro: {e}\n")

    if nome_usuario == "João" and idade > 35:
        break
    
    c += 1

    if c >= 3:
        print("Bloqueado...")
        print(f"\nVocê excedeu 3 tentativas...")
        break


import re

marcos = 0

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
    
for i in range(5):
    while True:
        name = input("Digite seu nome: ")

        if validar_nome(name): break
    if name.strip().lower() == "marcos": marcos += 1

print(f"Dos cadastrados, {marcos} se chamam Marcos!")
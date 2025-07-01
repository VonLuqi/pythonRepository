import re
import time as t
import os
import platform as pl

def limpar_tela():
    system_name = pl.system()
    
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clean')

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
    
def main():
    limpar_tela()
    for i in range(3):
        nome_usuario = ""

        while True:
            nome_usuario = input("Digite seu nome: (mín 3 letras)\n\n")
            if validar_nome(nome_usuario):
                limpar_tela()
                break

        print(f"{nome_usuario} foi cadastrados com sucesso!\n")
        t.sleep(3)
        limpar_tela()

if __name__ == "__main__":
    main()
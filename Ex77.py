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
    
def validar_telefone(telefone):
    padrao = re.compile(r"^\(?\d{2}\)?\s?9\d{4}-?\d{4}$")

    if padrao.match(telefone):
        return True
    else:
        print("Erro: Formato de telefone inválido"
              "Use (XX) 9XXXX-XXXX ou similar.")
        return False

def main():
    for i in range(3):
        nome_usuario = ""
        telefone_usuario = ""

        while True:
            nome_usuario = input("Digite seu nome: (mín 3 letras)\n\n")
            if validar_nome(nome_usuario):
                limpar_tela()
                break

        while True:
            telefone_usuario = input("Digite seu número de telefone: ((XX) 9XXXX-XXXX)\n\n")
            if validar_telefone(telefone_usuario):
                limpar_tela()
                break

        print(f"Bem-vindo {nome_usuario}! Telefone {telefone_usuario} cadastrado com sucesso!\n")
        t.sleep(3)
        limpar_tela()

if __name__ == "__main__":
    main()
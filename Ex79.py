import time as t
import os
import platform as pl

def limpar_tela():
    system_name = pl.system()
    
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clean')

def main():
    limpar_tela()
    for i in range(2):
        raca_cachorro = input("Qual a raça do seu cachorro? ").strip()
        cor_cachorro = input(f"Qual a cor do seu {raca_cachorro}? ").lower()
        porte_cachorro = input(f"Qual o porte do seu {raca_cachorro}? ").lower()

        limpar_tela()

        print(f"O cachorro da raça {raca_cachorro} e da cor {cor_cachorro} e porte {porte_cachorro} foi cadastrado com sucesso!")

        t.sleep(3)
        limpar_tela()

if __name__ == "__main__":
    main()
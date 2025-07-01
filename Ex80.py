import time as t
import os
import platform as pl

def limpar_tela():
    system_name = pl.system()
    
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clean')

def decimal(num):
    if num % 1 != 0:
        return f"{num:.2f}"
    else:
        return f"{int(num)}"

def main():
    limpar_tela()
    while True:
        num_tabuada = float(input("Quer ver a tabuada de qual número?\n\nn: "))

        limpar_tela()

        for i in range(10):
            if i == 0: print("="*10,"\n\n")
            print(f"{decimal(num_tabuada)} x {decimal(i+1)} = {decimal(num_tabuada*(i+1))}")

        resposta = input(f"\nDepois da tabuada de {decimal(num_tabuada)}, quer ver de outro número? (s/n) ").strip().lower()

        if resposta not in {'s', 'sim', 'y', 'yes'}: break

        print("\n")

if __name__ == "__main__":
    main()
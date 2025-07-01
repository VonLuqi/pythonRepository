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
    qnt_even = 0
    sum_even = 0
    qnt_odd = 0
    sum_odd = 0
    
    for i in range(4):
        num = int(input(f"Digite o número de número {i+1}: "))

        if num % 2 == 0:
            qnt_even += 1
            sum_even += num
        else:
            qnt_odd += 1
            sum_odd += num

    total_sum = sum_odd + sum_even

    print(f"Foram cadastrados {qnt_even} números pares\n"
          f"Foram cadastrados {qnt_odd} números ímpares\n"
          f"A soma dos pares é {sum_even}\n"
          f"A dos ímpares é {sum_odd}\n"
          f"A soma geral é {total_sum}\n")
            

if __name__ == "__main__":
    main()
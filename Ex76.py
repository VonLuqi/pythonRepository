import random as r

while True:
    n = int(input("Digite um número: "))
    evenOrOdd = int(input("Você quer [1 - par] [2 - ímpar]? "))

    numPc = r.randint(1, 9)
    
    soma = n + numPc
    
    result = "par" if soma % 2 == 0 else "ímpar"
    evenOrOdd = "par" if evenOrOdd == 1 else "ímpar"
    
    if result == evenOrOdd:
        print("\nParabéns você venceu!")
        break
    else: print("\nVocê perdeu... Tente novamente!\n")
n = [int(input(f"Digite o n{i+1}: ")) for i in range(2)]

r = int(input("Qual operação você quer fazer?\n\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n\nR: "))

match r:
    case 1: print(sum(n))
    case 2: print(n[0]-n[1])
    case 3: print(n[0]*n[1])
    case 4: print(n[0]/n[1])
    case _: print("Opção inválida... programa encerrado!")
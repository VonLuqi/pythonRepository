preco = float(input("Qual o valor do produto? R$"))

r = int(input("Qual data estamos?\n\n[1] Carnaval\n[2] Férias Escolares\n[3] Dia das Crianças\n[4] Black Friday\n[5] Natal\n\nR: "))

match r:
    case 1: print(preco * 1.1)
    case 2: print(preco * 1.2)
    case 3: print(preco * 1.05)
    case 4: print(preco * 0.7)
    case 5: print(preco * 0.95)
    case _: print("Opção inválida... encerrando programa!")
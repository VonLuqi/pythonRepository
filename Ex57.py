r = int(input("Qual série você viu no final de semana?\n\n[1] Sandman\n[2] Wandinha\n[3] Game of Thrones\n[4] Dota\n[5] Dexter\n\nR: "))

match r:
    case 1: print("A série escolhida foi Sandman")
    case 2: print("A série escolhida foi Wandinha")
    case 3: print("A série escolhida foi Game of Thrones")
    case 4: print("A série escolhida foi Dota")
    case 5: print("A série escolhida foi Dexter")
    case _: print("Opção inválida... encerrando programa!")
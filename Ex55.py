peso = float(input("Qual o seu peso na terra? (kg) "))

r = int(input("Qual planeta deseja ir?\n\n[1] Mercúrio\n[2] Vênus\n[3] Marte\n[4] Júpiter\n[5] Saturno\n[6] Urano\n\nR: "))

match r:
    case 1: print(peso * 0.37)
    case 2: print(peso * 0.88)
    case 3: print(peso * 0.38)
    case 4: print(peso * 2.64)
    case 5: print(peso * 1.15)
    case 6: print(peso * 1.17)
    case _: print("Opção inválida... encerrando programa!")
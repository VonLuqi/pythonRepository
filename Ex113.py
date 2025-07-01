import random as r
                    # 0       1        2         3        4
prs_placeholder = ["pedra","papel","tesoura","lagarto","spock"]
sorteio = r.randint(0,4)
prs_bot = prs_placeholder[sorteio]

while True:
    try:
        choice = int(input("Vamos jogar Pedra, Papel e Tesoura\n\nQual você escolhe?\n\n[1] Pedra\n[2] Papel\n[3] Tesoura\n[4] Lagarto\n[5] Spock\n\nR: "))

        if choice not in {1,2,3,4,5}:
            raise ValueError("Você deve escolher uma das opções...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

choice -= 1
prs_player = prs_placeholder[choice]

if prs_bot == prs_player:
    print(f"Você jogou {prs_player} e o bot jogou {prs_bot}, logo foi um empate!")
elif (choice == 0 and (sorteio == 2 or sorteio == 3)) or (choice == 1 and (sorteio == 0 or sorteio == 4)) or (choice == 2 and (sorteio == 1 or sorteio == 3)) or (choice == 3 and (sorteio == 1 or sorteio == 4)) or (choice == 4 and (sorteio == 0 or sorteio == 2)):
    print(f"Você jogou {prs_player} e o bot jogou {prs_bot}, logo você venceu!")
else:
    print(f"Você jogou {prs_player} e o bot jogou {prs_bot}, logo você perdeu!")

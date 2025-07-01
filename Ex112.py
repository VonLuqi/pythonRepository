import random as r

prs_placeholder = ["pedra","papel","tesoura"]
sorteio = r.randint(0,2)
prs_bot = prs_placeholder[sorteio]

while True:
    try:
        choice = int(input("Vamos jogar Pedra, Papel e Tesoura\n\nQual você escolhe?\n\n[1] Pedra\n[2] Papel\n[3] Tesoura\n\nR: "))

        if choice not in {1,2,3}:
            raise ValueError("Você deve escolher uma das opções...")
        break
    except ValueError as e:
        print(f"\nErro: {e}\n")

prs_player = prs_placeholder[choice-1]

if prs_bot == prs_player:
    print(f"Você jogou {prs_player} e o bot jogou {prs_bot}, logo foi um empate!")
elif (choice == 1 and sorteio == 2) or (choice == 2 and sorteio == 0) or (choice == 3 and sorteio == 1):
    print(f"Você jogou {prs_player} e o bot jogou {prs_bot}, logo você venceu!")
else:
    print(f"Você jogou {prs_player} e o bot jogou {prs_bot}, logo você perdeu!")

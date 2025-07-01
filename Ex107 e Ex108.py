import random as r
import time as t
import os
import platform as pt

def limpar_tela():
    system_name = pt.system()

    if system_name == "Windows": os.system('cls')
    else: os.system('clear')

def victory(red_chance: int, black_chance: int, white_chance: int) -> int:
    percent = r.randint(1, 100)

    if percent <= red_chance: return 1
    elif percent <= red_chance + black_chance: return 2
    else: return 3

def get_new_saldo(saldo: float, bet:float, num_vic:int) -> float:
    new_saldo = saldo

    if num_vic in {1, 2}: new_saldo += bet * 2
    else: new_saldo += bet * 14

    return new_saldo

def main():
    while True: # Início do sistema / Reiniciar
        user = {
            "name":"",
            "money":0,
            "idade":0
        }

        limpar_tela()

        user["name"] = input("Qual o seu nome? ")

        t.sleep(1)
        limpar_tela()

        print(f"Bem-vindo {user['name']}!")
        t.sleep(2)
        limpar_tela()

        while True:
            try:
                idade = int(input("Qual a sua idade? "))

                if idade < 18:
                    raise ValueError("Você é muito novo... Encerrando o programa...")
                break
            except ValueError as e:
                print(f"Erro: {e}")
                t.sleep(3)
                return
            finally:
                limpar_tela()
        
        while True:
            try:
                user["money"] = float(input("Quanto dinheiro você tem na conta? R$"))

                if user["money"] <= 0:
                    raise ValueError("O valor não pode ser 0 e nem negativo...")
                print("Depositando...")
                break
            except ValueError as e:
                print(f"Erro: {e}")
            finally:
                t.sleep(3)
                limpar_tela()
        
        while True: # Segunda parte do sistema, a parte do jogo / Jogar novamente
            print(f"===== {user['name']} =====\n\nSaldo R${user['money']:.2f}\n")

            while True:
                try:
                    bet = float(input("Você quer apostar quanto? R$"))

                    if bet > user["money"]:
                        raise ValueError(f"Você não pode apostar mais do que tem.\nAtualmente seu saldo é R${user['money']:.2f}")
                    user["money"] -= bet
                    break
                except ValueError as e:
                    print(f"Erro: {e}")
                    t.sleep(1)
            
            while True:
                try:
                    choice = int(input("\nEscolha a cor para apostar:\n\n[1] Vermelho -> x2\n[2] Preto -> x2\n[3] Branco -> x14\n\nR: "))

                    if choice not in {1, 2, 3}:
                        raise ValueError("Você deve escolher uma das opções, a que escolheu é inválida...")
                    t.sleep(1)
                    limpar_tela()
                    break
                except ValueError as e:
                    print(f"\nErro: {e}\n")
                    t.sleep(1)

            print("Calculando...")

            t.sleep(3)
            limpar_tela()
            vic = victory(49,49,2)

            if vic == choice:
                user['money'] = get_new_saldo(user["money"], bet, victory)
                print(f"Você venceu! Meus parabéns, seu saldo agora é R${user['money']}!")
            elif user["money"] <= 0:
                print(f"Infelizmente você perdeu TUDO (┬┬﹏┬┬) , Seu saldo atual é R${user['money']}... você faliu...")
                break
            else:
                print(f"Infelizmente você perdeu (┬┬﹏┬┬) , mas não fique triste, tente de novo! Seu saldo atual é R${user['money']}...")

            t.sleep(2)
            limpar_tela()

            continuar = input("Você quer continuar a jogar? [s/n] ") # Jogar novamente

            if continuar not in {'s','sim','y','yes'}: break

            limpar_tela()
        reiniciar = input("\nQuer reiniciar o sistema? [s/n] ") # Reiniciar o sistema

        if reiniciar not in {'s','sim','y','yes'}: break

        limpar_tela()



if __name__ == "__main__":
    main()
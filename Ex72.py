userLogin = {
    "fácil": "ff"
}

firstTry = True

multa = 2

while True:
    user = input("Qual o seu usuário para login? ").strip()
    password = input("Qual a sua senha? ").strip()
    
    if user in userLogin and password == userLogin[user]: 
        print(f"Acesso efetuado corretamente! Bem-vindo {user}!")
        break
    else:
        if firstTry == False: multa *= 2
        print(f"\nVocê será multado em R${multa} pela sua falha, tente novamente...\n")
        firstTry = False
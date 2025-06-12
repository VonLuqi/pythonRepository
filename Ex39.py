user = {
    "nome": input("Qual o seu nome? "),
    "idade": int(input("Qual a sua idade? "))
}

maioridade = "maior de idade" if user["idade"] >= 18 else "menor de idade"

print(f"{user['nome']} é {maioridade}!\n")
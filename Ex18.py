user = [
    input("Você tem mais que 25 anos? (sim/nao) "),
    input("Você fala inglês? (sim/nao) ")
]

msn = "verdadeiro" if user[1] == "sim" or (user[1] == "sim" and user[0] == "sim") else "falso"
print(msn)
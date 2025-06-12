user = {
    "valor": float(input("Qual o valor da casa? R$")),
    "salario": float(input("Qual o seu salário atual? R$")),
    "meses": int(input("Em quantos meses pretende pagar? "))
}

print("empréstimo negado" if (user["valor"] / user["meses"]) >= (user["salario"] * 0.3) else "empréstimo aprovado")
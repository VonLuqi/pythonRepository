data = {
    "dia": int(input("Digite a data de hoje: (dia/mes/ano) [digite o dia e de enter e assim por diante]\n\n")),
    "mes": int(input()),
    "ano": int(input())
}

if data["dia"] == 9 and data["mes"] == 9 and data["ano"] == 2022:
    dia = input("Sabe o que se comemora nesse dia? ").strip().lower()
    if dia == "dia do administrador":
        senac = input("Sabe o que vai ter no SENAC hoje? ").strip().lower()
        if senac == "sim": print("Então você ja sabe da surpresa inesperada, nesse caso a surpresa nem é tão inesperada assim")
else: print("Hoje é o dia de uma surpresa INESPERADA")
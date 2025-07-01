import Assets.functions as fn

temDivida = input("Você tem alguma dívida? ").strip().lower()

if temDivida in {'s','sim','y','yes'}:
    total = fn.lascado()
    print(f"O total de sua dívida atual é R${total}")
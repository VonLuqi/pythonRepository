car = {
    "tempo": int(input("Quantos dias foram gastos na viagem? ")),
    "vel": float(input("Qual foi a velocidade média percorrida? ")),
}

dist = car["tempo"] * 24 * car["vel"]
litros = dist / 12

print(f"Você andou por {dist}Km e gastou {litros} litros!\n")
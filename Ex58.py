r = int(input("Qual desses humoristas você gosta?\n\n[1] Fábio Porchat\n[2] Danilo Gentili\n[3] Rafinha Bastos\n\nR: "))

cidade = input("Qual cidade você mora? ").lower().strip()

match r:
    case 1:
        if cidade == "araxá":
            idade = int(input("Qual a sua idade?"))
            if idade >= 18: print("Tem show do Fábio Porchat!")
            else: print("Muito novo...")
    case 2:
        if cidade == "são paulo": print("Tem show do Danilo Gentili!")
    case 3:
        if cidade == "rio grande do sul": print("Tem show do Rafinha Bastos!")
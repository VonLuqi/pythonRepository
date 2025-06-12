perguntas = [
    "Você usa martelo?\n\nR: ",          # add thor
    "Você usa uma armadura?\n\nR: ",     # add hf
    "Você usa uma roupa colada?\n\nR: ", # add cap
    "Você é um deus?\n\nR: ",            # add thor
    "Você usa um escudo?\n\nR: "         # add cap
]

cap = 0
hf = 0
thor = 0

print("Responda 'sim' ou 'não' para as perguntas.\n")

for i in range(len(perguntas)):
    resposta = input(perguntas[i]).strip().lower()
    
    if resposta in ["sim","s","claro","yes","y"]:
        if i in [0,3]: thor += 1
        if i == 1: hf += 1
        if i in [2,4]: cap += 1
        
print(f"=====PONTUAÇÃO FINAL=====\n\nThor tem {thor} pontos\nCapitão América tem {cap} pontos\nHomem de ferro tem {hf} pontos\n")
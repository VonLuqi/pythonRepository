user = {
    "nome": [],
    "tel": []
}

c = 0

while c < 3:
    exibirNome = input("Digite seu nome: ")
    user["nome"].append(exibirNome)
    
    exibirTelefone = int(input("Digite seu telefone: "))
    user["tel"].append(exibirTelefone)
    
    print(f"{exibirNome} cadastrado com sucesso!")
    
    c += 1
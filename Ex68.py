user = {
    "nome": [],
    "sexo": [],
    "idade": []
}

c = 0

while c in range(5):
    c += 1
    
    nome = input(f"Qual o seu nome, pessoa {c}: ")
    sexo = input(f"Qual o seu sexo {nome}? ").strip().lower()
    idade = int(input(f"Qual a sua idade {nome}? "))
    
    user["nome"].append(nome)
    user["sexo"].append(sexo)
    user["idade"].append(idade)
    
print("\n=== Cadastro Finalizado! ===\n")
    
idade_homem_mais_velho = -1
nome_homem_mais_velho = ""

idade_mulher_mais_nova = float('inf')
nome_mulher_mais_nova = ""

c = 0

while c in range(len(user["nome"])):
    sexo_atual = user["sexo"][c]
    idade_atual = user["idade"][c]
    nome_atual = user["nome"][c]
    
    if sexo_atual in ['m', 'masculino']:
        if idade_atual > idade_homem_mais_velho:
            idade_homem_mais_velho = idade_atual
            nome_homem_mais_velho = nome_atual
    elif sexo_atual in ['f', 'feminino']:
        if idade_atual < idade_mulher_mais_nova:
            idade_mulher_mais_nova = idade_atual
            nome_mulher_mais_nova = nome_atual
    c += 1
            
print("=== Análise de Dados ===")

if nome_homem_mais_velho: print(f"O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos de idade!")
else: print("Nenhum homem foi cadastrado.")

if nome_mulher_mais_nova: print(f"A mulher mais nova é {nome_mulher_mais_nova} com {idade_mulher_mais_nova} anos de idade!")
else: print("Nenhuma mulher foi cadastrada.")
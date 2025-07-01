import Assets.functions as fn

respostas = [
    input("Responda algumas perguntas de forma honesta (responda apenas com s/n):\n\nVocê ja telefonou para a vítima? ").strip().lower(),
    input("Você ja esteve no local do crime? ").strip().lower(),
    input("Você mora perto da vítima? ").strip().lower(),
    input("Você devia para a vítima? ").strip().lower(),
    input("Você ja trabalhou com a vítima? ").strip().lower()
]

resultado_final = fn.investigar(respostas)

print(f"Você foi classificado como {resultado_final}... aguarde próximas notícias.")
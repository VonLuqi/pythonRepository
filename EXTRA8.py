tamanho_arquivo = float(input("Digite o tamanho do arquivo que quer baixar (Mb): "))
velocidade_internet = float(input("Qual a velocidade da sua internet (Mbps): "))

mbpm = velocidade_internet * 60

minutos_para_baixar = tamanho_arquivo // mbpm

print(f"Seu download vai demorar {minutos_para_baixar} minutos para baixar.")
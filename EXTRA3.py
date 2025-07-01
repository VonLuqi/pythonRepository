gigabits = float(input("Digite o valor do arquivo, em Gb: "))

megabits = gigabits * 1024
kilobits = gigabits * 1024 * 1024

print(f"Megabytes: {megabits}\nKilobytes: {kilobits}")
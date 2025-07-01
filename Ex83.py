import re
import time as t
import os
import platform as pl

def log_execucao(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Iniciando a execução de '{func.__name__}'...")
        t.sleep(1)
        resultado = func(*args, **kwargs)
        print(f"[LOG] Finalizando a execução de '{func.__name__}'.\n")
        return resultado
    return wrapper

def lidar_com_erros(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"\n[ERRO] Ocorreu um problema na função [{func.__name__}': {e}\n]")
            return False
    return wrapper
    
@log_execucao
def limpar_tela():
    system_name = pl.system()
    
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clean')

@lidar_com_erros
def validar_nome(nome):
    if not nome or not nome.strip():
        print("\nErro: O nome não pode ser vazio.\n")
        return False
    
    if len(nome.strip()) < 3:
        print("\nErro: O nome deve ter pelo menos 3 caracteres.\n")
        return False
    
    padrao = re.compile(r"^[a-zA-ZÁ-ú ]+$")

    if padrao.match(nome):
        return True
    else:
        print("\nErro: O nome deve conter apenas letras e espaços.\n")
        return False

@log_execucao
def main():
    qnt_homem = 0
    limpar_tela()
    for i in range(3):
        nome_usuario = ""

        while True:
            nome_usuario = input("Digite seu nome: (mín 3 letras)\n\n")
            if validar_nome(nome_usuario):
                limpar_tela()
                break
        
        while True:
            try:
                sexo = input("Qual o seu sexo? (F/M) ").strip().lower()
                if sexo not in {'f', 'm', 'feminino', 'masculino'}: raise ValueError("Opção inválida, tente F ou M...")
                if sexo in {'m', 'masculino'}: qnt_homem += 1
                limpar_tela()
                break
            except ValueError as e:
                print(f"\nErro: {e}\n")

    print(f"{qnt_homem} homens foram cadastrados com sucesso!\n")
    t.sleep(3)
    limpar_tela()

if __name__ == "__main__":
    main()
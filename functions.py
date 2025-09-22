import os
os.system("cls")

"""
ID.............: 1234
Nome...........: Julio André
Idade..........: 56
Sexo...........: Masculino
Tipo de login..: 
Precisa de ajuda: Sim
Problema.......: Login
Teleconsulta...: Sim
Especialidade..: Cardiologia
Sucesso........: Sim
Satisfação.....: 4
Tempo no app...: 25 min
Tempo login....: 45 seg
Absenteísmo....: Não
"""

dados = {}

# Solicitando o ID do usuário
while True:
    try:
        dados["id_usuario"] = int(input("ID do usuário: "))
        break
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.\n")

# Solicitando o Nome do usuário
dados["nome_usuario"] = str(input("Nome: ")).strip().capitalize()

# Solicitando a Idade do usuário
while True:
    try:
        dados["idade_usuario"] = int(input("Idade do usuário: "))
        break
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.\n")

# Solicitando a Sexo do usuário
while True:
    sexo = str(input("Sexo do usuário [M/F]: ")).strip().upper()[0]
    if sexo not in "MF":
        print("Entrada inválida. (M = Masculino | F = Feminino)")
    else:
        break
dados["sexo_usuario"] = sexo

# Solicitando o Tipo de Login
while True:
    try:
        escolha = int(input("""Tipo de login:
    1 -> Gov
    2 -> Etiqueta
Escolha: """))
        
        if escolha == 1:
            dados["tipo_login"] = "gov"
            break
        elif escolha == 2:
            dados["tipo_login"] = "etiqueta"
            break
        else:
            print("Entrada inválida. Digite 1 para Gov ou 2 para Etiqueta.")
    except ValueError:
        print("Entrada inválida. Digite um número (1 ou 2).")

# Solicitando se Precisou de ajuda
while True:
    resposta = str(input("Precisou de ajuda? [S/N]: ")).strip().upper()[0]
    
    if resposta not in "SN":
        print("Entrada inválida. (Digite S para Sim ou N para Não)")
        continue

    if resposta == "S":
        dados["ajuda"] = {}
        dados["ajuda"]["precisou"] = True

        # Solicita o momento da ajuda
        while True:
            try:
                momento = int(input("""Quando precisou de ajuda?
1 -> Antes do login
2 -> Depois do login
Escolha: """))

                if momento == 1:
                    dados["ajuda"]["momento"] = "antes login"
                    break
                elif momento == 2:
                    dados["ajuda"]["momento"] = "depois login"
                    break
                else:
                    print("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Digite um número (1 ou 2).")

        break

    elif resposta == "N":
        dados["ajuda"] = False
        break


def imprimir_dados(dados, espaco='') -> None:
    for k, v in dados.items():
        print(f"{espaco}{k}:", end=' ')
        if isinstance(v, dict):
            print()
            imprimir_dados(v, espaco + '  ')
        else:
            print(v)



os.system("cls")
imprimir_dados(dados)
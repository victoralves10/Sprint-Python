import os
import json
os.system("cls")

# ---------------- Separador ---------------- 
# Exibe uma linha separadora no console 
def separador() -> None:
    print("\n" + "-"*30 + "\n")

# ---------------- Título ---------------- 
# Exibe um título centralizado com linhas decorativas 
def titulo(_texto: str) -> None:
    print("=-" * 35)
    print(_texto.center(70))
    print("=-" * 35, "\n")

# ---------------- Solicita números ---------------- 
# Solicita ao usuário um número inteiro, opcionalmente dentro de um intervalo 
def solicita_numero(
    _mensagem: str, _valores_minimos: int | None = None, _valores_maximos: int | None = None) -> int:
    while True:
        try:
            n = int(input(_mensagem))
            if (_valores_minimos is not None and n < _valores_minimos) or (_valores_maximos is not None and n > _valores_maximos):
                print(f"Digite um número entre {_valores_minimos} e {_valores_maximos}.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


# ---------------- Solicita texto ---------------- 
# Solicita ao usuário um texto não vazio #
def solicita_texto(_mensagem: str) -> str:
    while True:
        texto = input(_mensagem).strip()
        if texto:
            return texto
        print("Não pode ficar vazio.")  


# ---------------- Solicita Sim/Não ---------------- 
# Solicita uma resposta Sim/Não ao usuário e retorna True para "Sim" e False para "Não" 
def solicita_sim_nao(_mensagem: str) -> bool:
    while True:
        resp = input(_mensagem).strip().upper()[0]
        if resp in ["S", "N"]: 
            return resp == "S"
        print("Entrada inválida. Digite S para Sim ou N para Não.")


# ---------------- Solicita opção ---------------- 
# Solicita ao usuário que escolha uma opção numerada e retorna o valor correspondente 
def solicita_opcao(_mensagem: str, _opcoes: dict) -> str:
    while True:
        print(_mensagem)
        for k, v in _opcoes.items():
            print(f"{k} -> {v}")
        escolha = solicita_numero("Escolha: ")
        if escolha in _opcoes:
            return _opcoes[escolha]
        print("Opção inválida. Tente novamente.")


# ---------------- Funções de dados específicos ---------------- 

# Solicita a idade do usuário 
def solicita_idade() -> int:
    return solicita_numero("Idade do usuário: ")

# ---------------- Solicita o sexo do usuário ---------------- 
# Solicita "M" ou "F"
def solicita_sexo() -> str:
    while True:
        sexo = input("Sexo do usuário [M/F]: ").strip().upper()
        if sexo in ["M", "F"]:
            return sexo  # Retorna apenas a letra
        print("Entrada inválida. (M = Masculino | F = Feminino)")

# ---------------- Solicita o Tipo do login do usuário ---------------- 
# Solicita o tipo de login do usuário 
def solicita_tipo_login() -> str:
    opcoes = {1: "gov", 2: "etiqueta"}
    return solicita_opcao("Tipo de login:", opcoes)

# Solicita informações se precisou de ajuda 
def solicita_ajuda() -> dict:
    if solicita_sim_nao("Precisou de ajuda? [S/N]: "):
        opcoes_momento = {1: "antes login", 2: "depois login"}
        momento = solicita_opcao("Quando precisou de ajuda?", opcoes_momento)

        opcoes_problema = {1: "login", 2: "consulta", 3: "agenda", 4: "outros"}
        problema = solicita_opcao("Onde ocorreu o problema?", opcoes_problema)

        return {"precisou": True, "momento": momento, "problema": problema}
    else:
        return {"precisou": False}


# Solicita a especialidade escolhida pelo usuário e se teve sucesso 
def solicita_especialidade() -> dict:
    opcoes = {1: "cardiologia", 2: "neurologia", 3: "oncologia", 4: "ortopedia"}
    especialidade = solicita_opcao("Escolha a especialidade:", opcoes)
    sucesso = solicita_sim_nao("Teve sucesso? [S/N]: ")
    return {"especialidade": especialidade, "sucesso": sucesso}

# Solicita satisfação do usuário (1 a 5) #
def solicita_satisfacao() -> int:
    return solicita_numero("Satisfação do usuário 1-5: ", 1, 5)

# Solicita tempo total de uso do app (em minutos) #
def solicita_tempo_uso() -> int:
    return solicita_numero("Tempo total de uso no app (em minutos): ", 0)

# Solicita tempo de login no app (em minutos) #
def solicita_tempo_login() -> int:
    return solicita_numero("Tempo de login no app (em minutos): ", 0)

# Solicita se houve absenteísmo #
def solicita_absenteismo() -> bool:
    return solicita_sim_nao("Absenteísmo? [S/N]: ")


# ---------------- Solicitação de dados principal ---------------- #
# Solicita ao usuário todos os dados necessários e retorna um dicionário completo #
def solicita_dados(_dados: dict | None = None) -> dict:
    if _dados is None:
        _dados = {}  # Cria um dicionário vazio caso não seja passado

    # Solicita ID do usuário
    _dados["id_usuario"] = solicita_numero("ID do usuário: ")
    separador()

    # Solicita nome do usuário
    _dados["nome_usuario"] = solicita_texto("Nome do usuário: ")
    separador()

    # Solicita idade do usuário
    _dados["idade_usuario"] = solicita_idade()
    separador()

    # Solicita sexo do usuário
    _dados["sexo_usuario"] = solicita_sexo()
    separador()

    # Solicita tipo de login
    _dados["tipo_login"] = solicita_tipo_login()
    separador()

    # Solicita se precisou de ajuda e detalhes
    _dados["ajuda"] = solicita_ajuda()
    separador()

    # Solicita especialidade e se teve sucesso
    _dados["especialidade"] = solicita_especialidade()
    separador()

    # Solicita satisfação do usuário (1-5)
    _dados["satisfacao"] = solicita_satisfacao()
    separador()

    # Solicita tempo total de uso do app
    _dados["tempo_uso"] = solicita_tempo_uso()
    separador()

    # Solicita tempo de login no app
    _dados["tempo_login"] = solicita_tempo_login()
    separador()

    # Solicita se houve absenteísmo
    _dados["absenteismo"] = solicita_absenteismo()
    separador()

    return _dados

# ---------------- Exibição de dados do usuário ---------------- #
# Exibe todos os dados do usuário em tabela alinhada, detalhando subcampos e convertendo booleanos #
def exibir_dados(_dados: dict) -> None:
    # Cabeçalho da tabela
    print(f"{'Campo':<25} {'Valor':>30}")
    print("-" * 56)

    # Mapeamento de nomes "bonitos" para cada campo
    nomes_campos = {
        "id_usuario": "ID",
        "nome_usuario": "Nome",
        "idade_usuario": "Idade",
        "sexo_usuario": "Sexo",
        "tipo_login": "Tipo de Login",
        "ajuda": "Precisou de Ajuda",
        "especialidade": "Especialidade",
        "satisfacao": "Satisfação",
        "tempo_uso": "Tempo de Uso (min)",
        "tempo_login": "Tempo de Login (min)",
        "absenteismo": "Absenteísmo"
    }

    for k, v in _dados.items():
        campo = nomes_campos.get(k, k)

        # Subcampos de 'ajuda'
        if k == "ajuda" and isinstance(v, dict):
            print(f"{campo:<25} {'Sim' if v.get('precisou') else 'Não':>30}")
            if v.get('precisou', False):
                print(f"{'Momento':<25} {v.get('momento',''):>30}")
                print(f"{'Problema':<25} {v.get('problema',''):>30}")
            continue

        # Subcampos de 'especialidade'
        elif k == "especialidade" and isinstance(v, dict):
            v = f"{v.get('especialidade','')} - {'Sucesso' if v.get('sucesso') else 'Fracasso'}"

        # Booleanos gerais
        elif isinstance(v, bool):
            v = "Sim" if v else "Não"

        # Impressão final do campo
        print(f"{campo:<25} {str(v):>30}")




# Menu escolha
def texto_menu_principal():
    print("\n1. Adicionar Novo Registro".ljust(31) + " - Cadastre informações de teleconsultas")
    print("2. Visualizar Dashboard".ljust(30) + " - Resumo de Métricas")
    print("3. Gerenciar Registro".ljust(30) + " - Editar ou excluir registros")
    print("\n0. Sair do sistema\n")


# Menu principal
def menu_principal():

    while True:
        os.system("cls")
        dados = {}
        titulo("ACCESSIBILITY TECH DASHBOARD")
        print("Menu Principal\n".center(70))

        texto_menu_principal()

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        match escolha:
            case 1:
                os.system("cls")
                dados = solicita_dados()
                os.system("cls")
                exibir_dados(dados)
                input("\nEnter para continar")
                continue
            case 2:
                exibir_dados(dados)
                input("\nEnter para continar")
            case 0:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
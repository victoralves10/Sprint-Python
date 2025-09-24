import json
import os

def limpa_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def separacao(_simbolo: str, _qtd: int) -> None:
    print(f"{_simbolo * _qtd}")

def imprime_titulo(titulo: str, largura: int) -> None:
    print("=-" * largura)
    print(titulo.center(largura * 2))
    print("=-" * largura)

"""
# ler json de um arquiovo para dicionario
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.loads(f) # dados é um dicionario
"""

#---------- Validação de Entrada de Dados ----------

# Solicita ao usuário um número inteiro e só retorna quando a entrada for válida.
def solicita_numero(_mensagem: str) -> int:
    while True:
        entrada = str(input(_mensagem)).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        try:
            return int(entrada)
        except ValueError:
            print("Digite apenas números inteiros.")


# Solicita um texto para o usuário e só retorna uma entrada válida.
def solicita_texto(_mensagem: str) -> str:
    while True:
        texto = input(_mensagem).strip()
        if texto:
            return texto
        
# Solicita ao usuário "S" ou "N" e retorna True para "S" e False para "N"
def resposta_sim_nao(_mensagem: str) -> bool:
    while True:
        entrada = input(f"{_mensagem}").strip().upper()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        if entrada[0] in ["S", "N"]:
            return entrada[0] == "S"
        else:
            print("Responda com 'S' para sim ou 'N' para não.")

# Solicita ao usuário um número inteiro dentro de um intervalo específico
def solicita_opcao(_mensagem: str, _min: int, _max: int) -> int:
    while True:
        entrada = str(input(_mensagem)).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        try:
            entrada = int(entrada)
            if _min <= entrada <= _max:
                return entrada
            else:
                print(f"Erro! digite {_min} à {_max}.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

#---------- Solicitação e Validação de Entrada de Dados Específicos ----------

# Solicita sexo "M" ou "F"
def solicita_sexo() -> str:
    while True:
        entrada = input("Sexo: [M/F] ").strip().upper()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        if entrada[0] in ["M", "F"]:
            return entrada[0]
        else:
            print("Responda com 'M' para Masculino ou 'F' para Feminino.")

# Solicita o tipo de login
def solicita_tipo_login() -> str:
    mensagem = "Tipo login: \n 1 -> Gov\n 2 -> Etiqueta\n  Escolha: "
    escolha = solicita_opcao(mensagem, 1, 2)
    if escolha == 1:
        escolha = "gov"
    else:
        escolha = "etiqueta"
    return escolha

# Solicita como foi a ajuda
def solicita_ajuda() -> dict:
    if resposta_sim_nao("Precisou de ajuda? [S/N] "):
        mensagem_login = " 1 -> Antes do login\n 2 -> depois do login\n  Escolha: "
        momento_login = solicita_opcao(mensagem_login, 1,2)

        mensagem_problema = """\nOnde ocorreu o problema?
 1 -> Login
 2 -> Consulta
 3 -> Agenda
 4 -> Outros
   Escolha: """
        tipo_problema = solicita_opcao(mensagem_problema, 1, 4)

        if momento_login == 1:
            momento_login = "antes login"
        else:
            momento_login = "depois login"

        match tipo_problema:
            case 1:
                tipo_problema = "login"
            case 2:
                tipo_problema = "consulta"
            case 3:
                tipo_problema = "agenda"
            case 4:
                tipo_problema = "outros"
        return {
            "precisou": True,
            "momento": momento_login,
            "problema": tipo_problema
            }
    else:
        return {"precisou": False}
    
# Solicita a especialidade escolhida pelo usuário e se teve sucesso
def solicita_especialidade() -> dict:
    mensagem_especialidade = """\nEscolha a especialidade:
 1 -> Cardiologia
 2 -> Neurologia
 3 -> Oncologia
 4 -> Ortopedia
   Escolha: """
    
    especialidade_opcao = solicita_opcao(mensagem_especialidade, 1, 4)

    match especialidade_opcao:
        case 1:
            especialidade = "cardiologia"
        case 2:
            especialidade = "neurologia"
        case 3:
            especialidade = "oncologia"
        case 4:
            especialidade = "ortopedia"

    sucesso = resposta_sim_nao("Teve sucesso? [S/N]: ")

    return {
        "especialidade": especialidade,
        "sucesso": sucesso
    }

# Solicita satisfação do usuário de 1 a 5
def solicita_satisfacao() -> int:
    return solicita_opcao("Satisfação do usuário 1-5: ", 1,5)

# Solicita o tempo de uso no app 
def solicita_tempo_uso() -> int:
    return solicita_numero("Tempo de uso no app (digite apenas os minutos): ")

# Solicita o tempo de login no app 
def solicita_tempo_login() -> int:
    return solicita_numero("Tempo de login no app (digite apenas os minutos): ")

# Solicita se houve absenteísmo 
def solicita_absenteismo() -> bool:
    return resposta_sim_nao("Absenteísmo? [S/N]: ")

#---------- Solicitação de Dados DashBoard ----------
# Coleta os dados do usuário e retorna um dicionário com os dados
def solicita_dados() -> dict:
    id_usuario = solicita_numero("ID do usuário: ")

    print()
    nome = solicita_texto("Nome do usuário: ")

    print()
    idade = solicita_numero("Idade: ")

    print()
    sexo = solicita_sexo()

    print()
    tipo_login = solicita_tipo_login()

    print()
    ajuda = solicita_ajuda()

    print()
    especialidade = solicita_especialidade()

    print()
    satisfacao = solicita_satisfacao()

    print()
    tempo_uso = solicita_tempo_uso()

    print()
    tempo_login = solicita_tempo_login()

    print()
    absenteismo = solicita_absenteismo()

    return {
        "id_usuario": id_usuario,
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "tipo_login": tipo_login,
        "ajuda": ajuda,
        "especialidade": especialidade,
        "satisfacao": satisfacao,
        "tempo_uso": tempo_uso,
        "tempo_login": tempo_login,
        "absenteismo": absenteismo
    }

# Pega os dados do usuário e formata com o ID como chave principal
def solicita_dados_dict() -> dict:
    dados = solicita_dados()
    id_str = str(dados["id_usuario"])
    return {id_str: dados}

#---------- Gravar Dados JSON ----------
def gravar_json(_arquivo_json, _novo_dado: dict):
    # Lê os dados atual se o arquivo existir
    if os.path.exists(_arquivo_json):
        with open(_arquivo_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = {}
    else:
        dados = {}

    # Atualiza os dados com o novo dicionário
    dados.update(_novo_dado)

    # Salva de volta no json
    with open(_arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        input("Dados Registrados com sucesso!!\nEnter Para voltar pro menu...")



def imprimir_dados(dados, espaco='') -> None:
    for k, v in dados.items():
        print(f"{espaco}{k}:", end=' ')
        if isinstance(v, dict):
            print()
            imprimir_dados(v, espaco + '  ')
        else:
            print(v)


def excluir_registro(_arquivo_json: str) -> None:
    while True:
        # Lê os dados 
        if os.path.exists(_arquivo_json): # verifica se existe
            with open(_arquivo_json, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    input("Arquivo corrompido.\n\nPressione Enter para continuar...")
                    return
        else:
            input("Não há registros para excluir.\n\nPressione Enter para continuar...")
            return

        if not dados:
            input("Não há registros para excluir.\n\nPressione Enter para continuar...")
            return

        print("Registros disponíveis:\n")
        print("ID           | NOME")
        separacao("=-", 26)
        for k, v in dados.items():
            print(f"{k:12} | {v.get('nome','')}")

        print("\n0. Cancelar e sair.")

        # Solicita o ID para ircluir
        id_para_excluir = str(solicita_numero("\nDigite o ID do usuário a ser excluído: "))

        if id_para_excluir == "0":
            break  # Volta ao menu

        if id_para_excluir in dados:
            print()
            imprimir_dados(dados[id_para_excluir])

            confirmacao = resposta_sim_nao(f"\nDeseja excluir cadastro do usuário {dados[id_para_excluir].get('nome')}? [S/N]: ")
            if confirmacao: # Se for true
                del dados[id_para_excluir]
                # Salva os dados atualizado
                with open(_arquivo_json, 'w', encoding='utf-8') as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)
                input("Registro excluído com sucesso!\n\nPressione Enter para continuar...")
                break
            else:
                input("Exclusão cancelada.\n\nPressione Enter para continuar...")
        else:
            input("\nID não encontrado.\n\nPressione Enter para continuar...")
            break


def menu_dashboard() -> None:
    dados_usuario = {}
    arquivo = "dados_usuario.json"
    while True:
        limpa_tela()
        imprime_titulo("MENU DASHBOARD", 30)
        print()

        print("1. Adicionar Novo Registro")
        print("2. Visualizar Dashboard")
        print("3. Editar dados")
        print("4. Excluir registros")
        print("0. Sair do Sistema")
        print()
        escolha = solicita_opcao("Escolha: ",0,4)

        match escolha:
            case 1:
                limpa_tela()
                dados_usuario = solicita_dados_dict()
                gravar_json(arquivo, dados_usuario)

            case 4:
                limpa_tela()
                excluir_registro(arquivo)
            case 0:
                print("Encerrando programa...")
                break


menu_dashboard()
import json
import os

# ----------------- Funções de Utilidade Geral -----------------

def limpar_terminal() -> None:
    """Limpa o console (terminal)."""
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_separacao(_simbolo: str, _qtd: int) -> None:
    """Imprime um separador (linha) com um símbolo e quantidade especificados."""
    print(f"{_simbolo * _qtd}")

def imprimir_titulo_formatado(titulo: str, largura: int) -> None:
    """Imprime um título centralizado e formatado com bordas."""
    print("=-" * largura)
    print(titulo.center(largura * 2))
    print("=-" * largura)

"""
# ler json de um arquiovo para dicionario
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.loads(f) # dados é um dicionario
"""

# ----------------- Funções de Validação de Entrada de Dados -----------------

# Solicita ao usuário um número inteiro e só retorna quando a entrada for válida.
def pedir_numero_inteiro(_mensagem: str) -> int:
    """Solicita um número inteiro do usuário e garante uma entrada válida."""
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
def pedir_texto_obrigatorio(_mensagem: str) -> str:
    """Solicita um texto (string) não vazio do usuário."""
    while True:
        texto = input(_mensagem).strip()
        if texto:
            return texto
        
# Solicita ao usuário "S" ou "N" e retorna True para "S" e False para "N"
def obter_confirmacao_sim_nao(_mensagem: str) -> bool:
    """Solicita uma resposta 'S' (sim) ou 'N' (não) e retorna um booleano."""
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
def pedir_opcao_intervalo(_mensagem: str, _min: int, _max: int) -> int:
    """Solicita um número dentro de um intervalo mínimo e máximo especificado."""
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

# ----------------- Funções de Coleta de Dados Específicos -----------------

# Solicita sexo "M" ou "F"
def coletar_sexo() -> str:
    """Solicita o sexo do usuário ('M' ou 'F')."""
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
def coletar_tipo_login() -> str:
    """Solicita e retorna o tipo de login ('gov' ou 'etiqueta')."""
    mensagem = "Tipo login: \n 1 -> Gov\n 2 -> Etiqueta\n  Escolha: "
    escolha = pedir_opcao_intervalo(mensagem, 1, 2)
    if escolha == 1:
        escolha = "gov"
    else:
        escolha = "etiqueta"
    return escolha

# Solicita como foi a ajuda
def coletar_dados_ajuda() -> dict:
    """Coleta informações sobre a necessidade de ajuda do usuário (momento e problema)."""
    if obter_confirmacao_sim_nao("Precisou de ajuda? [S/N] "):
        mensagem_login = " 1 -> Antes do login\n 2 -> depois do login\n  Escolha: "
        momento_login = pedir_opcao_intervalo(mensagem_login, 1,2)

        mensagem_problema = """\nOnde ocorreu o problema?
 1 -> Login
 2 -> Consulta
 3 -> Agenda
 4 -> Outros
    Escolha: """
        tipo_problema = pedir_opcao_intervalo(mensagem_problema, 1, 4)

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
def coletar_especialidade_sucesso() -> dict:
    """Coleta a especialidade escolhida e se houve sucesso na marcação."""
    mensagem_especialidade = """\nEscolha a especialidade:
 1 -> Cardiologia
 2 -> Neurologia
 3 -> Oncologia
 4 -> Ortopedia
    Escolha: """
    
    especialidade_opcao = pedir_opcao_intervalo(mensagem_especialidade, 1, 4)

    match especialidade_opcao:
        case 1:
            especialidade = "cardiologia"
        case 2:
            especialidade = "neurologia"
        case 3:
            especialidade = "oncologia"
        case 4:
            especialidade = "ortopedia"

    sucesso = obter_confirmacao_sim_nao("Teve sucesso? [S/N]: ")

    return {
        "especialidade": especialidade,
        "sucesso": sucesso
    }

# Solicita satisfação do usuário de 1 a 5
def coletar_nivel_satisfacao() -> int:
    """Solicita o nível de satisfação do usuário (1 a 5)."""
    return pedir_opcao_intervalo("Satisfação do usuário 1-5: ", 1,5)

# Solicita o tempo de uso no app 
def coletar_tempo_uso() -> int:
    """Solicita o tempo de uso no app em minutos."""
    return pedir_numero_inteiro("Tempo de uso no app (digite apenas os minutos): ")

# Solicita o tempo de login no app 
def coletar_tempo_login() -> int:
    """Solicita o tempo gasto no login no app em minutos."""
    return pedir_numero_inteiro("Tempo de login no app (digite apenas os minutos): ")

# Solicita se houve absenteísmo 
def coletar_absenteismo() -> bool:
    """Pergunta se houve absenteísmo ('S'/'N')."""
    return obter_confirmacao_sim_nao("Absenteísmo? [S/N]: ")

# ----------------- Funções de Coleta de Dados para Dashboard -----------------

# Coleta os dados do usuário e retorna um dicionário com os dados
def coletar_todos_dados_usuario(_arquivo_json: str) -> dict:
    """Coleta todos os dados do usuário para o Dashboard e retorna um dicionário."""
    id_usuario = gerar_id(_arquivo_json)
    print(f"ID gerado automaticamente: {id_usuario}")


    print()
    nome = pedir_texto_obrigatorio("Nome do usuário: ")

    print()
    idade = pedir_numero_inteiro("Idade: ")

    print()
    sexo = coletar_sexo()

    print()
    tipo_login = coletar_tipo_login()

    print()
    ajuda = coletar_dados_ajuda()

    print()
    especialidade = coletar_especialidade_sucesso()

    print()
    satisfacao = coletar_nivel_satisfacao()

    print()
    tempo_uso = coletar_tempo_uso()

    print()
    tempo_login = coletar_tempo_login()

    print()
    absenteismo = coletar_absenteismo()
    print()

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
def formatar_dados_com_id(_arquivo_json: str) -> dict:
    """Chama coletar_todos_dados_usuario e formata o resultado com o ID do usuário como chave principal."""
    dados = coletar_todos_dados_usuario(_arquivo_json)
    id_str = str(dados["id_usuario"])
    return {id_str: dados}


# ----------------- Funções de Gerenciamento de JSON -----------------

# Gera automaticamente o próximo ID baseado no JSON
def gerar_id(_arquivo_json: str) -> int:
    """Lê o arquivo JSON e retorna o próximo ID disponível (int)."""
    dados = carregar_dados_json(_arquivo_json)
    if not dados:
        return 1
    # Pega o maior ID e soma 1
    return max(map(int, dados.keys())) + 1

# Retorna os dados de um arquivo JSON como dicionário
def carregar_dados_json(_arquivo_json: str) -> dict:
    """Lê um arquivo JSON e retorna seu conteúdo como um dicionário. Retorna um dicionário vazio em caso de erro ou arquivo não existente."""
    # Verifica se o arquivo existe
    if os.path.exists(_arquivo_json):
        with open(_arquivo_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                # Se o JSON estiver vazio ou corrompido, retorna dict vazio
                dados = {}
    else:
        # Se não existir, retorna dict vazio
        dados = {}

    return dados


def salvar_dados_json(_arquivo_json, _novo_dado: dict):
    """Lê um arquivo JSON, adiciona/atualiza o novo dado e salva de volta no arquivo."""
    # Lê os dados atual se o arquivo existir
    dados = carregar_dados_json(_arquivo_json)

    # Atualiza os dados com o novo dicionário
    dados.update(_novo_dado)

    # Salva de volta no json
    with open(_arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        input("Dados Registrados com sucesso!!\nEnter Para voltar pro menu...")

# Exibe um único registro formatado (com ou sem numeração)
def exibir_registro_formatado(id_usuario: str, info: dict, numerado: bool = False) -> None:
    largura = 20
    linhas = []

    # Dados principais
    linhas.append((f"ID:", id_usuario))
    linhas.append(("Nome:", info["nome"].title()))
    linhas.append(("Idade:", info["idade"]))
    linhas.append(("Sexo:", info["sexo"].upper()))
    linhas.append(("Tipo do Login:", info["tipo_login"].capitalize()))

    # Seção Ajuda
    linhas.append(("--- Ajuda ---", ""))
    ajuda = info.get("ajuda", {})
    linhas.append(("Precisou:", str(ajuda.get("precisou", False)).capitalize()))
    if ajuda.get("precisou", False):
        linhas.append(("Momento:", ajuda.get("momento", "-").capitalize()))
        linhas.append(("Problema:", ajuda.get("problema", "-").capitalize()))

    # Especialidade
    especialidade = info.get("especialidade", {})
    linhas.append(("Especialidade:", especialidade.get("especialidade", "-").capitalize()))
    linhas.append(("Sucesso:", str(especialidade.get("sucesso", False)).capitalize()))

    # Outros campos
    linhas.append(("Satisfação:", info["satisfacao"]))
    linhas.append(("Tempo de Uso:", f"{info['tempo_uso']} minutos"))
    linhas.append(("Tempo de Login:", f"{info['tempo_login']} minutos"))
    linhas.append(("Absenteísmo:", str(info["absenteismo"]).capitalize()))

    # Impressão formatada
    for idx, (campo, valor) in enumerate(linhas, start=1):
        if campo.startswith("---"):  # título de seção
            print(f"\n\t{campo}")
        else:
            if numerado:
                print(f"{idx:<3}{campo:<{largura}} {valor}")
            else:
                print(f"{campo:<{largura}} {valor}")


# Lê um arquivo JSON de usuários e exibe os dados formatados na tela
def visualizar_dados_json(_arquivo_json: str):
    """Lê um arquivo JSON e exibe os dados de cada usuário formatados no console."""
    dados = carregar_dados_json(_arquivo_json)
    
    if not dados:
        print("Nenhum dado encontrado.")
        return

    print("\n--- DADOS DOS USUÁRIOS ---\n")
    for id_usuario, info in dados.items():
        exibir_registro_formatado(id_usuario, info, numerado=False)  # false para listagem normal
        print("\n" + "-" * 40 + "\n")


def remover_registro(_arquivo_json: str) -> None:
    """Permite ao usuário selecionar um registro por ID e excluí-lo do arquivo JSON."""
    while True:
        # Lê os dados 
        dados = carregar_dados_json(_arquivo_json)

        if not dados:
            input("Não há registros para excluir.\n\nPressione Enter para continuar...")
            return

        print("Registros disponíveis:\n")
        print("ID            | NOME")
        imprimir_separacao("=-", 26)
        for k, v in dados.items():
            print(f"{k:12} | {v.get('nome','')}")

        print("\n0. Cancelar e sair.")

        # Solicita o ID para excluir
        id_para_excluir = str(pedir_numero_inteiro("\nDigite o ID do usuário a ser excluído: "))

        if id_para_excluir == "0":
            break  # Volta ao menu

        if id_para_excluir in dados:
            limpar_terminal()
            print("\n--- REGISTRO A SER EXCLUÍDO ---\n")
            
            # --- Adaptação para exibir um único registro ---
            largura = 20
            info = dados[id_para_excluir]
            print(f"{'ID:':<{largura}} {id_para_excluir}")
            print(f"{'Nome:':<{largura}} {info['nome'].title()}")
            print(f"{'Idade:':<{largura}} {info['idade']}")
            print(f"{'Sexo:':<{largura}} {info['sexo'].upper()}")
            print(f"{'Tipo do Login:':<{largura}} {info['tipo_login'].capitalize()}")
            
            print("\n--- Ajuda ---")
            ajuda = info.get("ajuda", {})
            print(f"{'Precisou:':<{largura}} {str(ajuda.get('precisou', False)).capitalize()}")
            if ajuda.get("precisou", False):
                print(f"{'Momento:':<{largura}} {ajuda.get('momento', '-').capitalize()}")
                print(f"{'Problema:':<{largura}} {ajuda.get('problema', '-').capitalize()}")
            
            especialidade = info.get("especialidade", {})
            print(f"{'Especialidade:':<{largura}} {especialidade.get('especialidade', '-').capitalize()}")
            print(f"{'Sucesso:':<{largura}} {str(especialidade.get('sucesso', False)).capitalize()}")
            
            print(f"\n{'Satisfação:':<{largura}} {info['satisfacao']}")
            print(f"{'Tempo de Uso:':<{largura}} {info['tempo_uso']} minutos")
            print(f"{'Tempo de Login:':<{largura}} {info['tempo_login']} minutos")
            print(f"{'Absenteísmo:':<{largura}} {str(info['absenteismo']).capitalize()}")
            print("\n" + "-" * 40 + "\n")
            # --- Fim da adaptação ---

            confirmacao = obter_confirmacao_sim_nao(f"\nDeseja excluir cadastro do usuário {dados[id_para_excluir].get('nome')}? [S/N]: ")
            if confirmacao: # Se for true
                del dados[id_para_excluir]
                # Salva os dados atualizado
                with open(_arquivo_json, 'w', encoding='utf-8') as f:
                    json.dump(dados, f, indent=4, ensure_ascii=False)
                input("Registro excluído com sucesso!\n\nPressione Enter para continuar...")
                break
            else:
                input("Exclusão cancelada.\n\nPressione Enter para continuar...")
                break
        else:
            input("\nID não encontrado.\n\nPressione Enter para continuar...")
            # Não usei o break aqui, para permitir nova tentativa de ID, o que faz mais sentido do que o código anterior.


def menu_principal_dashboard() -> None:
    """Função principal que exibe o menu e controla o fluxo do programa."""
    dados_usuario = {}
    arquivo = "dados_usuario.json"
    while True:
        limpar_terminal()
        imprimir_titulo_formatado("MENU DASHBOARD", 30)
        print()

        print("1. Adicionar Novo Registro")
        print("2. Visualizar Dashboard")
        print("3. Editar dados")
        print("4. Excluir registros")
        print("0. Sair do Sistema")
        print()
        escolha = pedir_opcao_intervalo("Escolha: ",0,4)

        match escolha:
            case 1:
                limpar_terminal()
                dados_usuario = formatar_dados_com_id(arquivo)
                salvar_dados_json(arquivo, dados_usuario)

            
            case 2:
                limpar_terminal()
                visualizar_dados_json(arquivo)
                input("\nEnter para voltar!...")

            case 4:
                limpar_terminal()
                remover_registro(arquivo)
            case 0:
                print("Encerrando programa...")
                break


menu_principal_dashboard()

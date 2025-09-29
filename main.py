import json
import os

# =============================================================
#           1. FUNÇÕES DE UTILIDADE E CONTROLE DE FLUXO
# =============================================================

def limpa_tela():
    """Limpa o console (terminal)."""
    os.system("cls" if os.name == "nt" else "clear")

def imprime_linha_separadora(simbolo: str, quantidade: int):
    """Imprime uma linha separadora."""
    print(f"{simbolo * quantidade}")

def imprime_titulo_centralizado(titulo: str, largura: int):
    """Imprime um título centralizado com bordas."""
    print("=-" * largura)
    print(titulo.center(largura * 2))
    print("=-" * largura)

# =============================================================
#           2. FUNÇÕES DE VALIDAÇÃO E ENTRADA DE DADOS
# =============================================================

def pede_numero_inteiro(mensagem: str) -> int:
    """Solicita e retorna um número inteiro válido."""
    while True:
        entrada = str(input(mensagem)).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        try:
            return int(entrada)
        except ValueError:
            print("Digite apenas números inteiros.")

def pede_texto_obrigatorio(mensagem: str) -> str:
    """Solicita e retorna um texto (string) não vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        
def obtem_confirmacao_sim_nao(mensagem: str) -> bool:
    """Solicita 'S' ou 'N' e retorna True ou False."""
    while True:
        entrada = input(f"{mensagem}").strip().upper()
        if entrada and entrada[0] in ["S", "N"]:
            return entrada[0] == "S"
        print("Responda com 'S' para sim ou 'N' para não.")

def pede_opcao_no_intervalo(mensagem: str, minimo: int, maximo: int) -> int:
    """Solicita um número dentro de um intervalo [minimo, maximo]."""
    while True:
        entrada = str(input(mensagem)).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        try:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Erro! digite {minimo} à {maximo}.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

# ----------------- Sub-rotinas de Coleta de Dados Específicos -----------------

def coleta_sexo() -> str:
    """Retorna o sexo ('M' ou 'F')."""
    while True:
        entrada = input("\nSexo: [M/F] ").strip().upper()
        if entrada and entrada[0] in ["M", "F"]:
            return entrada[0]
        print("Responda com 'M' para Masculino ou 'F' para Feminino.")

def coleta_tipo_login() -> str:
    """Retorna o tipo de login ('gov' ou 'etiqueta')."""
    mensagem = "\nTipo login: \n 1 -> Gov\n 2 -> Etiqueta\n  Escolha: "
    escolha = pede_opcao_no_intervalo(mensagem, 1, 2)
    return "gov" if escolha == 1 else "etiqueta"

def coleta_dados_ajuda() -> dict:
    """Retorna dados sobre necessidade, momento e problema de ajuda."""
    if obtem_confirmacao_sim_nao("\nPrecisou de ajuda? [S/N] "):
        momento_opc = pede_opcao_no_intervalo(" 1 -> Antes do login\n 2 -> depois do login\n  Escolha: ", 1, 2)
        momento = "antes login" if momento_opc == 1 else "depois login"

        mensagem_problema = """\nOnde ocorreu o problema?
 1 -> Login, 2 -> Consulta, 3 -> Agenda, 4 -> Outros
  Escolha: """
        problema_opc = pede_opcao_no_intervalo(mensagem_problema, 1, 4)
        problema_map = {1: "login", 2: "consulta", 3: "agenda", 4: "outros"}
        
        return {"precisou": True, "momento": momento, "problema": problema_map.get(problema_opc)}
    else:
        return {"precisou": False}
    
def coleta_especialidade() -> str:
    """Retorna a especialidade escolhida pelo usuário."""
    mensagem = """\nEscolha a especialidade:
 1 -> Cardiologia
 2 -> Neurologia
 3 -> Oncologia
 4 -> Ortopedia
 Escolha: """
    opcao = pede_opcao_no_intervalo(mensagem, 1, 4)
    mapa = {1: "cardiologia", 2: "neurologia", 3: "oncologia", 4: "ortopedia"}
    return mapa[opcao]

def coleta_sucesso() -> bool:
    """Retorna True/False se houve sucesso na marcação."""
    return obtem_confirmacao_sim_nao("\nTeve sucesso? [S/N]: ")






def coleta_precisou_ajuda() -> bool:
    return obtem_confirmacao_sim_nao("\nPrecisou de ajuda? [S/N]: ")

def coleta_momento_ajuda() -> str:
    mensagem = """\nQuando precisou de ajuda?
 1 -> Antes do login
 2 -> Durante o uso
 3 -> Depois do uso
 Escolha: """
    opcao = pede_opcao_no_intervalo(mensagem, 1, 3)
    mapa = {1: "antes", 2: "durante", 3: "depois"}
    return mapa[opcao]

def coleta_problema_ajuda() -> str:
    mensagem = """\nQual foi o problema?
 1 -> Técnico
 2 -> Dúvida
 3 -> Outro
 Escolha: """
    opcao = pede_opcao_no_intervalo(mensagem, 1, 3)
    mapa = {1: "técnico", 2: "dúvida", 3: "outro"}
    return mapa[opcao]












# ----------------- Função Central de Coleta de Dados -----------------

def coleta_dados_de_usuario(nome_arquivo: str) -> dict:
    """Coleta todos os dados do usuário para o Dashboard."""
    id_usuario = gera_id_usuario(nome_arquivo)
    print(f"ID gerado automaticamente: {id_usuario}")

    # Coleta de dados
    nome = pede_texto_obrigatorio("\nNome do usuário: ")
    idade = pede_numero_inteiro("\nIdade: ")
    sexo = coleta_sexo()
    tipo_login = coleta_tipo_login()
    
    precisou_ajuda = coleta_precisou_ajuda()
    momento = coleta_momento_ajuda() if precisou_ajuda else None
    problema = coleta_problema_ajuda() if precisou_ajuda else None

    ajuda = {
        "precisou": precisou_ajuda,
        "momento": momento,
        "problema": problema
    }

    especialidade = coleta_especialidade()
    sucesso = coleta_sucesso()
    satisfacao = pede_opcao_no_intervalo("\nSatisfação do usuário 1-5: ", 1, 5)
    tempo_uso = pede_numero_inteiro("\nTempo de uso no app (minutos): ")
    tempo_login = pede_numero_inteiro("\nTempo de login no app (minutos): ")
    absenteismo = obtem_confirmacao_sim_nao("\nAbsenteísmo? [S/N]: ")

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

def formata_dados_para_salvar(nome_arquivo: str) -> dict:
    """Formata os dados coletados com o ID do usuário como chave principal."""
    dados_coletados = coleta_dados_de_usuario(nome_arquivo)
    id_str = str(dados_coletados["id_usuario"])
    # Remove a chave 'id_usuario' que agora será a chave externa do JSON
    del dados_coletados["id_usuario"] 
    return {id_str: dados_coletados}

# =============================================================
#           3. FUNÇÕES DE GERENCIAMENTO DE JSON
# =============================================================

def gera_id_usuario(nome_arquivo: str) -> int:
    """Retorna o próximo ID disponível no arquivo JSON."""
    dados = carrega_dados_json(nome_arquivo)
    if not dados:
        return 1
    # Pega o maior ID e soma 1
    return max(map(int, dados.keys())) + 1

def carrega_dados_json(nome_arquivo: str) -> dict:
    """Lê um arquivo JSON e retorna seu conteúdo. Retorna {} se não existir/inválido."""
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def salva_dados_json(nome_arquivo: str, novo_dado: dict):
    """Adiciona/atualiza o novo dado no JSON e salva o arquivo."""
    dados_atuais = carrega_dados_json(nome_arquivo)
    dados_atuais.update(novo_dado)
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_atuais, f, indent=4, ensure_ascii=False)
    input("Dados Registrados com sucesso!!\nEnter Para voltar pro menu...")

# =============================================================
#           4. FUNÇÕES DE CÁLCULO DE INDICADORES (LÓGICA)
# =============================================================

def calcula_taxa_sucesso_especialidade(dados_especialidade: dict) -> dict:
    """Calcula a taxa de sucesso para cada especialidade e retorna o dicionário (seguro contra strings)."""
    especialidades_data = {}

    # Inicializa a estrutura de volume e sucesso
    for nome_esp in ["cardiologia", "neurologia", "oncologia", "ortopedia"]:
        especialidades_data[nome_esp] = {"volume": 0, "sucesso": 0}

    for usuario in dados_especialidade.values():
        esp_info = usuario.get("especialidade", {})
        # Se for string, transforma em dict com chave "especialidade"
        if isinstance(esp_info, str):
            esp_info = {"especialidade": esp_info, "sucesso": False}

        esp = esp_info.get("especialidade")

        if esp in especialidades_data:
            especialidades_data[esp]["volume"] += 1
            if esp_info.get("sucesso", False):
                especialidades_data[esp]["sucesso"] += 1

    # Adiciona a taxa percentual de sucesso
    especialidades_finais = {}
    for nome_esp, data in especialidades_data.items():
        volume = data["volume"]
        sucesso_pct = round((data["sucesso"] / volume) * 100) if volume > 0 else 0

        especialidades_finais[nome_esp.capitalize()] = {
            "volume": volume,
            "taxa": f"{sucesso_pct}%"
        }

    return especialidades_finais

    
    # Adiciona a taxa percentual de sucesso
    especialidades_finais = {}
    for nome_esp, data in especialidades_data.items():
        volume = data["volume"]
        sucesso_pct = round((data["sucesso"] / volume) * 100) if volume > 0 else 0
        
        especialidades_finais[nome_esp.capitalize()] = {
            "volume": volume,
            "taxa": f"{sucesso_pct}%"
        }
        
    return especialidades_finais


def calcula_indicadores(dados: dict) -> dict:
    """Calcula todas as métricas percentuais, médias e totais. Retorna valores numéricos."""
    total_usuarios = len(dados)
    if total_usuarios == 0:
        return {}

    # Contadores e somas
    soma_satisfacao = soma_tempo_uso = soma_tempo_login = 0
    total_sucesso = total_absenteismo = ajuda_total = ajuda_antes = ajuda_depois = 0
    genero = {"M": 0, "F": 0}
    login = {"gov": 0, "etiqueta": 0}
    problemas = {"login": 0, "consulta": 0, "agenda": 0, "outros": 0}
    

    for usuario in dados.values():
        # Somas
        soma_satisfacao += usuario.get("satisfacao", 0)
        soma_tempo_uso += usuario.get("tempo_uso", 0)
        soma_tempo_login += usuario.get("tempo_login", 0)

        esp_info = usuario.get("especialidade", {})
        if isinstance(esp_info, str):
            esp_info = {"especialidade": esp_info, "sucesso": False}
        if esp_info.get("sucesso", False):
            total_sucesso += 1


        # Gênero e Login
        sexo = usuario.get("sexo", "").upper()
        if sexo in genero:
            genero[sexo] += 1
        tipo_login = usuario.get("tipo_login", "").lower()
        if tipo_login in login:
            login[tipo_login] += 1

        # Ajuda e Problemas
        ajuda = usuario.get("ajuda", {})
        if ajuda.get("precisou", False):
            ajuda_total += 1
            momento = ajuda.get("momento")
            if momento == "antes login":
                ajuda_antes += 1
            elif momento == "depois login":
                ajuda_depois += 1
            problema = ajuda.get("problema")
            if problema in problemas:
                problemas[problema] += 1

    # Cálculos finais de percentuais e médias
    indicadores = {
        "total_usuarios": total_usuarios,
        "taxa_sucesso": round((total_sucesso / total_usuarios) * 100, 1),
        "satisfacao_media": round(soma_satisfacao / total_usuarios, 1),
        "taxa_absenteismo": round((total_absenteismo / total_usuarios) * 100, 1),
        "tempo_medio_login": round(soma_tempo_login / total_usuarios, 1),
        "tempo_medio_uso": round(soma_tempo_uso / total_usuarios, 1),
        
        "genero_m_pct": round((genero["M"] / total_usuarios) * 100),
        "genero_f_pct": round((genero["F"] / total_usuarios) * 100),
        "login_gov_pct": round((login["gov"] / total_usuarios) * 100),
        "login_etiqueta_pct": round((login["etiqueta"] / total_usuarios) * 100),
        
        "taxa_ajuda": round((ajuda_total / total_usuarios) * 100, 1),
        "ajuda_antes_pct": round((ajuda_antes / ajuda_total) * 100) if ajuda_total else 0,
        "ajuda_depois_pct": round((ajuda_depois / ajuda_total) * 100) if ajuda_total else 0,
        
        "problemas_pct": {k: round((v / total_usuarios) * 100) for k, v in problemas.items()},
    }
    
    return indicadores

# =============================================================
#           5. FUNÇÕES DE FORMATAÇÃO (PREPARAÇÃO DE VIEW)
# =============================================================

def formata_indicadores_para_dashboard(indicadores: dict, especialidades_data: dict) -> dict:
    """Formata os valores numéricos dos indicadores em strings para impressão."""
    problemas_formatados = {
        k.capitalize(): f"[ {v}% ]" 
        for k, v in indicadores.get("problemas_pct", {}).items()
    }

    return {
        # Alto Nível
        "sucesso": f"[ {indicadores['taxa_sucesso']}% ]",
        "satisfacao": f"[ {indicadores['satisfacao_media']} / 5.0 ]",
        "tempo_login": f"[ {indicadores['tempo_medio_login']} min ]",
        "tempo_uso": f"[ {indicadores['tempo_medio_uso']} min ]",
        "total_usuarios": f"[ {indicadores['total_usuarios']} ]",
        "absenteismo": f"[ {indicadores['taxa_absenteismo']}% ]",
        
        # Demografia e Login
        "genero_f": f"[ {indicadores['genero_f_pct']}% ]",
        "genero_m": f"[ {indicadores['genero_m_pct']}% ]",
        "login_gov": f"[ {indicadores['login_gov_pct']}% ]",
        "login_etiqueta": f"[ {indicadores['login_etiqueta_pct']}% ]",
        
        # Ajuda e Erros
        "ajuda_pct": f"[ {indicadores['taxa_ajuda']}% ]",
        "ajuda_antes": f"[ {indicadores['ajuda_antes_pct']}% ]",
        "ajuda_depois": f"[ {indicadores['ajuda_depois_pct']}% ]",
        "problemas": problemas_formatados,
        
        # Especialidade (já formatada em calcula_taxa_sucesso_especialidade)
        "especialidades": especialidades_data
    }

# =============================================================
#           6. FUNÇÕES DE IMPRESSÃO (VIEW)
# =============================================================

def imprime_par_alinhado(rotulo1, valor1, largura_campo1, largura_valor1, rotulo2=None, valor2=None):
    """Imprime uma ou duas métricas lado a lado com alinhamento fixo."""
    linha = f"{rotulo1:<{largura_campo1}} {valor1:<{largura_valor1}}"
    if rotulo2 and valor2:
        linha += f"| {rotulo2:<{largura_campo1}} {valor2}"
    print(linha)

def imprime_dashboard(indicadores_formatados: dict):
    """Imprime o dashboard formatado no terminal com alinhamento corrigido."""
    # Larguras fixas para alinhamento
    LARGURA_CAMPO = 20
    LARGURA_VALOR = 15
    LARGURA_TOTAL = 90

    print("\n" + "="*LARGURA_TOTAL)
    print(f"{'':<20} 📊 DASHBOARD DE DADOS AGREGADOS 📊")
    print("="*LARGURA_TOTAL + "\n")

    print("----- INDICADORES DE ALTO NÍVEL -----")
    imprime_par_alinhado("Taxa de Sucesso", indicadores_formatados['sucesso'], LARGURA_CAMPO, LARGURA_VALOR, 
                         "Satisfação Média", indicadores_formatados['satisfacao'])
    imprime_par_alinhado("Tempo Médio Login", indicadores_formatados['tempo_login'], LARGURA_CAMPO, LARGURA_VALOR, 
                         "Tempo Médio Uso", indicadores_formatados['tempo_uso'])
    imprime_par_alinhado("Total de Usuários", indicadores_formatados['total_usuarios'], LARGURA_CAMPO, LARGURA_VALOR, 
                         "Taxa de Absenteísmo", indicadores_formatados['absenteismo'])

    print("\n----- DEMOGRAFIA E LOGIN -----")
    imprime_par_alinhado("Gênero Feminino (F)", indicadores_formatados['genero_f'], LARGURA_CAMPO, LARGURA_VALOR, 
                         "Gênero Masculino (M)", indicadores_formatados['genero_m'])
    imprime_par_alinhado("Login Gov", indicadores_formatados['login_gov'], LARGURA_CAMPO, LARGURA_VALOR, 
                         "Login Etiqueta", indicadores_formatados['login_etiqueta'])

    print("\n----- AJUDA E ERROS -----")
    print(f"{'Necessidade de Ajuda':<{LARGURA_CAMPO}} {indicadores_formatados['ajuda_pct']}")
    imprime_par_alinhado("Ajuda Antes Login", indicadores_formatados['ajuda_antes'], LARGURA_CAMPO, LARGURA_VALOR, 
                         "Ajuda Depois Login", indicadores_formatados['ajuda_depois'])
    
    print("\nDistribuição dos Problemas:")
    problemas_list = list(indicadores_formatados["problemas"].items())
    
    # Imprime dois problemas por linha
    largura_problema = 20
    for i in range(0, len(problemas_list), 2):
        p1, v1 = problemas_list[i]
        
        linha = f"   - {p1:<{largura_problema}} {v1:<9}"
        
        if i + 1 < len(problemas_list):
            p2, v2 = problemas_list[i+1]
            linha += f" |    - {p2:<{largura_problema}} {v2:<9}"
        print(linha)

    print("\n----- DESEMPENHO POR ESPECIALIDADE -----\n")
    
    # Tabela de Especialidades
    LARGURA_COL_ESP = 25
    LARGURA_COL_VOL = 10
    LARGURA_COL_SUC = 16
    
    print(f"{'Especialidade':<{LARGURA_COL_ESP}} | {'Volume':<{LARGURA_COL_VOL}} | {'Taxa de Sucesso':<{LARGURA_COL_SUC}}")
    print("-"*(LARGURA_COL_ESP+1) + "|" + "-"*(LARGURA_COL_VOL+1) + "|" + "-"*(LARGURA_COL_SUC+1))
    
    for esp, data in indicadores_formatados["especialidades"].items():
        print(f"{esp:<{LARGURA_COL_ESP}} | {data['volume']:<{LARGURA_COL_VOL}} | {data['taxa']:<{LARGURA_COL_SUC}}")
    
    print("\n" + "="*LARGURA_TOTAL + "\n")
    input("Pressione Enter para voltar ao menu...")

def mostra_dashboard(nome_arquivo: str):
    """Orquestra o cálculo, a formatação e a impressão do Dashboard."""
    dados_brutos = carrega_dados_json(nome_arquivo)
    
    if not dados_brutos:
        limpa_tela()
        print("\n==============================================")
        print("📊 DASHBOARD DE DADOS AGREGADOS 📊")
        print("==============================================\n")
        print("⚠ Nenhum dado encontrado. Adicione registros primeiro.\n")
        input("Pressione Enter para voltar ao menu...")
        return

    # 1. CÁLCULO (Lógica de Negócio)
    indicadores_numericos = calcula_indicadores(dados_brutos)
    dados_especialidade = calcula_taxa_sucesso_especialidade(dados_brutos)
    
    if not indicadores_numericos:
        print("Nenhum dado para calcular indicadores.")
        return
        
    # 2. FORMATAÇÃO (Preparação da View)
    indicadores_formatados = formata_indicadores_para_dashboard(indicadores_numericos, dados_especialidade)
    
    # 3. IMPRESSÃO (View)
    imprime_dashboard(indicadores_formatados)


# =============================================================
#           7. FUNÇÕES DE CRUD (Remoção e Edição)
# =============================================================

def exibe_registro_detalhado(id_usuario: str, info: dict, numerado: bool = False):
    """Exibe os dados detalhados de um único usuário."""
    largura = 20
    linhas = []

    linhas.append(("ID:", id_usuario))
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
    linhas.append(("--- Especialidade ---", ""))
    especialidade = info.get("especialidade", {})
    linhas.append(("Especialidade:", especialidade.get("especialidade", "-").capitalize()))
    linhas.append(("Sucesso:", str(especialidade.get("sucesso", False)).capitalize()))

    # Outros campos
    linhas.append(("--- Outros ---", ""))
    linhas.append(("Satisfação:", info["satisfacao"]))
    linhas.append(("Tempo de Uso:", f"{info['tempo_uso']} minutos"))
    linhas.append(("Tempo de Login:", f"{info['tempo_login']} minutos"))
    linhas.append(("Absenteísmo:", str(info["absenteismo"]).capitalize()))

    # Impressão formatada
    numero = 1
    for campo, valor in linhas:
        if campo.startswith("---"):
            print(f"\n{'':<4}{campo.replace('-', '').strip()}")
        else:
            if numerado:
                print(f"{numero:2} - {campo:<{largura}} {valor}")
                numero += 1
            else:
                print(f"{campo:<{largura}} {valor}")

def remove_registro(nome_arquivo: str):
    dados = carrega_dados_json(nome_arquivo)

    if not dados:
        input("Não há registros para excluir.\n\nPressione Enter para continuar...")
        return

    print("Registros disponíveis:\n")
    print("ID            | NOME")
    imprime_linha_separadora("=-", 26)
    for k, v in dados.items():
        print(f"{k:12} | {v.get('nome','')}")

    print("\n0. Cancelar e sair.")
    id_para_excluir = str(pede_numero_inteiro("\nDigite o ID do usuário a ser excluído: "))

    if id_para_excluir == "0":
        return

    if id_para_excluir in dados:
        limpa_tela()
        print("\n--- REGISTRO A SER EXCLUÍDO ---\n")

        info = dados[id_para_excluir]
        exibe_registro_detalhado(id_para_excluir, info, numerado=True)
        print("\n" + "-" * 40 + "\n")

        confirmacao = obtem_confirmacao_sim_nao(
            f"\nDeseja excluir cadastro do usuário {info.get('nome')}? [S/N]: "
        )
        if confirmacao:
            del dados[id_para_excluir]
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            input("Registro excluído com sucesso!\n\nPressione Enter para continuar...")
        else:
            input("Exclusão cancelada.\n\nPressione Enter para continuar...")
    else:
        input("\nID não encontrado.\n\nPressione Enter para continuar...")

def edita_registro(nome_arquivo: str):
    """Permite editar campos de um registro existente."""
    dados = carrega_dados_json(nome_arquivo)

    if not dados:
        input("Não há registros para editar.\n\nPressione Enter para continuar...")
        return

    print("Registros disponíveis:\n")
    print("ID            | NOME")
    imprime_linha_separadora("=-", 26)
    for k, v in dados.items():
        print(f"{k:12} | {v.get('nome','')}")
    print("\n0. Cancelar e sair.")
    
    id_escolhido = str(pede_numero_inteiro("\nDigite o ID do usuário a ser editado: "))
    if id_escolhido == "0":
        return

    if id_escolhido not in dados:
        input("\nID não encontrado.\n\nPressione Enter para continuar...")
        return

    info = dados[id_escolhido]

    while True:
        limpa_tela()
        print(f"\n--- EDITANDO REGISTRO: {info.get('nome','')} ---\n")
        exibe_registro_detalhado(id_escolhido, info, numerado=True)

        print("\n0 - Voltar")
        escolha = pede_opcao_no_intervalo("\nEscolha o número do campo para editar: ", 0, 14)

        if escolha == 0:
            break

        match escolha:
            case 1:  # ID
                print("ID não pode ser alterado!")
            case 2:  # Nome
                info["nome"] = pede_texto_obrigatorio("Novo Nome: ")
            case 3:  # Idade
                info["idade"] = pede_numero_inteiro("Nova Idade: ")
            case 4:  # Sexo
                info["sexo"] = coleta_sexo()
            case 5:  # Tipo do Login
                info["tipo_login"] = coleta_tipo_login()
            case 6:  # Precisou de ajuda
                info["ajuda"]["precisou"] = obtem_confirmacao_sim_nao("Precisou de ajuda? [S/N]: ")
            case 7:  # Momento da ajuda
                if info["ajuda"].get("precisou", False):
                    mensagem = " 1 -> Antes do login\n 2 -> Depois do login\nEscolha: "
                    opc = pede_opcao_no_intervalo(mensagem, 1, 2)
                    info["ajuda"]["momento"] = "antes login" if opc == 1 else "depois login"
                else:
                    input("O usuário não precisou de ajuda. Pressione Enter para continuar...")
            case 8:  # Problema
                if info["ajuda"].get("precisou", False):
                    mensagem = " 1 -> Login\n 2 -> Consulta\n 3 -> Agenda\n 4 -> Outros\nEscolha: "
                    opc = pede_opcao_no_intervalo(mensagem, 1, 4)
                    info["ajuda"]["problema"] = {1:"login",2:"consulta",3:"agenda",4:"outros"}[opc]
                else:
                    input("O usuário não precisou de ajuda. Pressione Enter para continuar...")
            case 9:  # Especialidade
                mensagem = " 1 -> Cardiologia\n 2 -> Neurologia\n 3 -> Oncologia\n 4 -> Ortopedia\nEscolha: "
                opc = pede_opcao_no_intervalo(mensagem, 1, 4)
                info.setdefault("especialidade", {})
                info["especialidade"]["especialidade"] = {1:"cardiologia",2:"neurologia",3:"oncologia",4:"ortopedia"}[opc]
            case 10:  # Sucesso da especialidade
                info.setdefault("especialidade", {})
                info["especialidade"]["sucesso"] = obtem_confirmacao_sim_nao("Sucesso? [S/N]: ")
            case 11:  # Satisfação
                info["satisfacao"] = pede_opcao_no_intervalo("Nova Satisfação 1-5: ", 1, 5)
            case 12:  # Tempo de Uso
                info["tempo_uso"] = pede_numero_inteiro("Novo Tempo de Uso (minutos): ")
            case 13:  # Tempo de Login
                info["tempo_login"] = pede_numero_inteiro("Novo Tempo de Login (minutos): ")
            case 14:  # Absenteísmo
                info["absenteismo"] = obtem_confirmacao_sim_nao("Absenteísmo? [S/N]: ")
            case _:
                input("Opção inválida. Pressione Enter para continuar...")

        # Atualiza e salva o JSON
        dados[id_escolhido] = info
        salva_dados_json(nome_arquivo, {id_escolhido: info})
        # Removido o input redundante aqui.


# =============================================================
#           BLOCO PRINCIPAL
# =============================================================
dados_usuario = {}
arquivo = "dados_usuario.json"
while True:
    limpa_tela()
    imprime_titulo_centralizado("AXCESS TECH", 30)
    print()

    print("1. Adicionar Novo Registro")
    print("2. Visualizar Dashboard")
    print("3. Editar dados")
    print("4. Excluir registros")
    print("0. Sair do Sistema")
    print()
    escolha = pede_opcao_no_intervalo("Escolha: ",0,4)

    match escolha:
        case 1:
            limpa_tela()
            dados_usuario = formata_dados_para_salvar(arquivo)
            salva_dados_json(arquivo, dados_usuario)

        case 2:
            limpa_tela()
            mostra_dashboard(arquivo)
            
        case 3:
            limpa_tela()
            edita_registro(arquivo)
        case 4:
            limpa_tela()
            remove_registro(arquivo)
        case 0:
            print("Encerrando programa...")
            break
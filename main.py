import os
from functions import *
os.system("cls")

# ---------------- Execução ---------------- #

dados = {}

titulo("Solicitando dados")
solicita_dados(dados)

titulo("Mostrando dados")
exibir_dados(dados)
import os
import re
import sys

# Códigos ANSI para cores
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def renomear_pastas(diretorio):
    for nome_pasta in os.listdir(diretorio):
        caminho_antigo = os.path.join(diretorio, nome_pasta)
        if os.path.isdir(caminho_antigo):
            match = re.search(r'(c\d+(?:\.\d+)?)', nome_pasta, re.IGNORECASE)
            if match:
                novo_nome = match.group(1)
                caminho_novo = os.path.join(diretorio, novo_nome)
                if not os.path.exists(caminho_novo):
                    os.rename(caminho_antigo, caminho_novo)
                    print(f'{GREEN}Renomeado: {nome_pasta} -> {novo_nome}{RESET}')
                else:
                    print(f'{YELLOW}Pasta {novo_nome} já existe. Pulando...{RESET}')
            else:
                print(f'{RED}Padrão não encontrado em: {nome_pasta}{RESET}')

start_path = sys.argv[1] if len(sys.argv) > 1 else '.'

renomear_pastas(start_path)
import os
import re
import sys

def renomear_pastas(diretorio):
    for nome_pasta in os.listdir(diretorio):
        caminho_antigo = os.path.join(diretorio, nome_pasta)
        if os.path.isdir(caminho_antigo):
            # Procura pelo padrão cXXX (ex: c001)
            match = re.search(r'(c\d+)', nome_pasta, re.IGNORECASE)
            if match:
                novo_nome = match.group(1)
                caminho_novo = os.path.join(diretorio, novo_nome)
                if not os.path.exists(caminho_novo):
                    os.rename(caminho_antigo, caminho_novo)
                    print(f'Renomeado: {nome_pasta} -> {novo_nome}')
                else:
                    print(f'Pasta {novo_nome} já existe. Pulando...')
            else:
                print(f'Padrão não encontrado em: {nome_pasta}')

start_path = sys.argv[1] if len(sys.argv) > 1 else '.'

renomear_pastas(start_path)

# Exemplo de uso:
# renomear_pastas('/caminho/para/seu/diretorio')
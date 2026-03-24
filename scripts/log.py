import os
import sys
from datetime import datetime

# start_path = sys.argv[1] if len(sys.argv) > 1 else '.'

def logger(start_path = '.'):
    # Lista para armazenar caminhos relativos dos arquivos
    arquivos_relativos = []

    for root, dirs, files in os.walk(start_path):
        # Ignora diretórios '.yacreaderlibrary' e 'log'
        rel_parts = os.path.relpath(root, start_path).split(os.sep)
        if '.yacreaderlibrary' in rel_parts or 'log' in rel_parts:
            continue
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), start_path)
            arquivos_relativos.append(rel_path)

    # Cria diretório de log se não existir
    log_dir = os.path.join(start_path, 'log')
    os.makedirs(log_dir, exist_ok=True)

    # Nome do arquivo de log com data e hora
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = os.path.join(log_dir, f'log_{now}.txt')

    # Escreve os caminhos no arquivo de log
    with open(log_filename, 'w', encoding='utf-8') as f:
        for caminho in arquivos_relativos:
            f.write(caminho + '\n')

    print(f"Log criado em: {log_filename}")
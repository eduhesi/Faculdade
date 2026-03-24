import os
from datetime import datetime
from printer import printer as p, PrinterType

def logger(start_path: str = '.', ignore: list = None) -> str:
    """
    Gera um log com os caminhos relativos de todos os arquivos em start_path,
    ignorando diretórios especificados em ignore.
    Retorna o caminho do arquivo de log criado.
    """
    if ignore is None:
        ignore = ['.yacreaderlibrary', 'log']

    arquivos_relativos = []

    for root, _, files in os.walk(start_path):
        rel_parts = os.path.relpath(root, start_path).split(os.sep)
        if any(ign in rel_parts for ign in ignore):
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

    p(f"Log criado em: {log_filename}", PrinterType.SUCCESS)
    return log_filename
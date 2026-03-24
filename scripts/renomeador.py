import os
import re
from printer import printer as p, PrinterType

def renomear_pastas(diretorio, pattern: str = None):
    """
    Renomeia pastas em 'diretorio' usando o padrão regex informado.
    :param diretorio: Caminho do diretório a ser processado.
    :param pattern: Regex para extração do novo nome da pasta (default: capítulos 'c001', 'c001.1', etc).
    """
    if pattern is None:
        pattern = r'(c\d+(?:\.\d+)?)'
    for nome_pasta in os.listdir(diretorio):
        caminho_antigo = os.path.join(diretorio, nome_pasta)
        if os.path.isdir(caminho_antigo):
            match = re.search(pattern, nome_pasta, re.IGNORECASE)
            if match:
                novo_nome = match.group(1)
                caminho_novo = os.path.join(diretorio, novo_nome)
                if not os.path.exists(caminho_novo):
                    os.rename(caminho_antigo, caminho_novo)
                    p(f'Renomeado: {nome_pasta} -> {novo_nome}', PrinterType.SUCCESS)
                else:
                    p(f'Pasta {novo_nome} já existe. Pulando...', PrinterType.ALERT)
            else:
                p(f'Padrão não encontrado em: {nome_pasta}', PrinterType.ERROR)
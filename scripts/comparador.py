import os
import sys
from printer import printer as p, PrinterType

def comparador(files):
    links_unicos = set()
    for nome_arquivo in files:
        if not os.path.exists(nome_arquivo):
            p(f"Arquivo não encontrado: {nome_arquivo}", PrinterType.ERROR)
            continue
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                link = linha.strip()
                if link:
                    links_unicos.add(link)

    with open('itens_unicos', 'w', encoding='utf-8') as f:
        for link in sorted(links_unicos):
            f.write(link + '\n')
    p("Itens únicos salvos em ./itens_unicos",PrinterType.SUCCESS) if len(links_unicos) > 1 else p("Sem itens únicos")

if __name__ == "__main__":
    # Recupera todos os argumentos após o nome do script
    arquivos = sys.argv[1:]
    if not arquivos:
        p("Uso: python script.py arquivo1.txt arquivo2.txt ...", PrinterType.OTHER)
        sys.exit(1)
    comparador(arquivos)
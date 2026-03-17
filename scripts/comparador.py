arquivos = ['a', 'b', 'c']
links_unicos = set()

for nome_arquivo in arquivos:
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            link = linha.strip()
            if link:
                links_unicos.add(link)

with open('d', 'w', encoding='utf-8') as f:
    for link in sorted(links_unicos):
        f.write(link + '\n')
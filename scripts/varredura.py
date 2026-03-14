import os

pastas_com_arquivos_diferentes = []

for root, dirs, files in os.walk('.'):
    for file in files:
        if not file.endswith(('.tar', '.zip', '.cbz')):            
            pastas_com_arquivos_diferentes.append(os.path.abspath(root))
            break  # Já encontrou um arquivo diferente, pode passar para a próxima pasta

# Remover duplicatas, caso existam
pastas_com_arquivos_diferentes = list(set(pastas_com_arquivos_diferentes))

for a in pastas_com_arquivos_diferentes:
    print(a)

# print(pastas_com_arquivos_diferentes)
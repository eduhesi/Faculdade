import os
import sys

start_path = sys.argv[1] if len(sys.argv) > 1 else '.'
pastas_com_arquivos_diferentes = []

for root, dirs, files in os.walk(start_path):
    if 'mangafire' in os.path.relpath(root, start_path).split(os.sep):
        continue
    for file in files:
        if not file.endswith(('.tar', '.zip', '.cbz')):
            rel = os.path.relpath(root, start_path)
            pastas_com_arquivos_diferentes.append(rel)
            break

for a in pastas_com_arquivos_diferentes:
    print(a)
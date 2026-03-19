import os
import sys
from datetime import datetime

start_path = sys.argv[1] if len(sys.argv) > 1 else '.'
pastas_com_arquivos_diferentes = []

for root, dirs, files in os.walk(start_path):
    if 'mangafire' in os.path.relpath(root, start_path).split(os.sep):
        continue
    for file in files:
        # if not
        if file.endswith(('.tar', '.zip', '.cbz')):
            rel = os.path.relpath(root, start_path)
            pastas_com_arquivos_diferentes.append(rel)
            break

# Gera nome do arquivo com data e hora
now = datetime.now().strftime('%Y%m%d_%H%M%S')
# log_dir = os.path.join(start_path, 'log')
# os.makedirs(log_dir, exist_ok=True)
# log_filename = os.path.join(log_dir, f'log_{now}.txt')
log_filename = f'log_{now}.txt'
with open(log_filename, 'w', encoding='utf-8') as f:
    for a in pastas_com_arquivos_diferentes:
        f.write(a + '\n')
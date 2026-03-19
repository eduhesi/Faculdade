import os
import sys

# Códigos ANSI para cores
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

start_path = sys.argv[1] if len(sys.argv) > 1 else '.'

for root, dirs, files in os.walk(start_path):
    rel_dir = os.path.relpath(root, start_path)
    if rel_dir == '.':
        continue  # Ignora o diretório inicial
    dir_name = os.path.basename(root)
    file_path = os.path.join(root, f"{dir_name}")
    if os.path.exists(file_path):
        print(f"{YELLOW}Ignorado (já existe): {file_path}{RESET}")
        continue
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(rel_dir + '\n')
    print(f"{GREEN}Criado: {file_path} -> {rel_dir}{RESET}")
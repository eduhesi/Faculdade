import os
import sys

start_path = sys.argv[1] if len(sys.argv) > 1 else '.'

for root, dirs, files in os.walk(start_path):
    rel_dir = os.path.relpath(root, start_path)
    if rel_dir == '.':
        continue  # Ignora o diretório inicial
    dir_name = os.path.basename(root)
    file_path = os.path.join(root, f"{dir_name}")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(rel_dir + '\n')
    print(f"Criado: {file_path} -> {rel_dir}")
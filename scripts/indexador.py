import os
from printer import printer as p, PrinterType

def indexador(start_path="."):
    for root, _, _ in os.walk(start_path):
        rel_dir = os.path.relpath(root, start_path)
        if rel_dir == '.':
            continue  # Ignora o diretório inicial
        dir_name = os.path.basename(root)
        file_path = os.path.join(root, f"{dir_name}")
        if os.path.exists(file_path):
            p(f"Ignorado (já existe): {file_path}", PrinterType.ALERT)
            continue
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(rel_dir + '\n')
        p(f"Criado: {file_path} -> {rel_dir}", PrinterType.SUCCESS)
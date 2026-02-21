import os
import sys
import tarfile

# Recebe o caminho de início como argumento ou usa o diretório atual
start_path = sys.argv[1] if len(sys.argv) > 1 else '.'

# Lista todos os diretórios no caminho de início (exceto ele mesmo)
diretorios = [
    d for d in os.listdir(start_path)
    if (
        os.path.isdir(os.path.join(start_path, d)) 
        and d != '.' 
        and not d.startswith('.')
    )
]

for dir_name in diretorios:
    tar_name = f"{dir_name}.tar.gz"
    dir_full_path = os.path.join(start_path, dir_name)
    with tarfile.open(os.path.join(start_path, tar_name), "w:gz") as tar:
        tar.add(dir_full_path, arcname=dir_name)
    print(f"Diretório '{dir_full_path}' comprimido em '{tar_name}'")
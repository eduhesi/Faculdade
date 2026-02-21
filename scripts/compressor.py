import os
import tarfile

# Lista todos os diretórios no diretório atual (exceto '.')
diretorios = [d for d in os.listdir('.') if os.path.isdir(d) and d != '.']

for dir_name in diretorios:
    tar_name = f"{dir_name}.tar.gz"
    with tarfile.open(tar_name, "w:gz") as tar:
        tar.add(dir_name, arcname=dir_name)
    print(f"Diretório '{dir_name}' comprimido em '{tar_name}'")
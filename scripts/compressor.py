import os
import sys
import tarfile

# Códigos ANSI para cores
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

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

erros = []

for dir_name in diretorios:
    tar_name = f"{dir_name}.tar"
    tar_path = os.path.join(start_path, tar_name)
    dir_full_path = os.path.join(start_path, dir_name)
    if os.path.exists(tar_path):
        print(f"{YELLOW}Arquivo '{tar_name}' já existe. Pulando compressão do diretório '{dir_name}'.{RESET}")
        continue
    try:
        with tarfile.open(os.path.join(start_path, tar_name), "w") as tar:
            tar.add(dir_full_path, arcname=dir_name)
        print(f"{YELLOW}Diretório '{dir_full_path}' comprimido em '{tar_name}'{RESET}")
    except Exception as e:
        print(f"{RED}Erro ao comprimir '{dir_full_path}': {e}{RESET}")
        erros.append(dir_name)

if erros:
    print(f"{RED}Falha ao comprimir os diretórios:{RESET}")
    for nome in erros:
        print(f"{RED}- {nome}{RESET}")
else:
    print(f"{GREEN}Todos os diretórios foram comprimidos com sucesso!{RESET}")
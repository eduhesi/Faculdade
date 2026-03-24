import os
import tarfile
from printer import printer as p, PrinterType

# Ignora diretorios no padrao .{nome}
def compressor(start_path = '.'):
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
            p(f"Arquivo '{tar_name}' já existe. Pulando compressão do diretório '{dir_name}'.", PrinterType.ALERT)
            continue
        try:
            with tarfile.open(os.path.join(start_path, tar_name), "w") as tar:
                tar.add(dir_full_path, arcname=dir_name)
            p(f"Diretório '{dir_full_path}' comprimido em '{tar_name}'")
        except Exception as e:
            p(f"Erro ao comprimir '{dir_full_path}': {e}", PrinterType.ERROR)
            erros.append(dir_name)

    if erros:
        p(f"Falha ao comprimir os diretórios:", PrinterType.ERROR)
        for nome in erros:
            p(f"- {nome}", PrinterType.ERROR_MESSAGE)
    else:
        p(f"Todos os diretórios foram comprimidos com sucesso!", PrinterType.SUCCESS)
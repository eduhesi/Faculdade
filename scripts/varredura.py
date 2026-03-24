import os
from datetime import datetime
from typing import List, Tuple, Optional

def pastas_com_arquivos(
    start_path: str = '.',
    excluidos: Optional[List[str]] = None,
    tipos: Optional[Tuple[str, ...]] = None
) -> List[str]:
    """
    Retorna lista de pastas (relativas a start_path) que contêm arquivos dos tipos especificados,
    ignorando diretórios que contenham qualquer termo em 'excluidos'.
    """
    if excluidos is None:
        excluidos = ['mangafire']
    if tipos is None:
        tipos = ('.tar', '.zip', '.cbz')

    pastas = set()
    for root, _, files in os.walk(start_path):
        rel_path_parts = os.path.relpath(root, start_path).split(os.sep)
        if any(excluido in rel_path_parts for excluido in excluidos):
            continue
        for file in files:
            if file.endswith(tipos):
                rel = os.path.relpath(root, start_path)
                pastas.add(rel)
                break
    return sorted(pastas)

if __name__ == "__main__":
    import sys
    start_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    # Exemplos de uso:
    # pastas = pastas_com_arquivos(start_path, excluidos=['mangafire', 'outro_dir'], tipos=('.zip',))
    pastas = pastas_com_arquivos(start_path)
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = f'log_{now}.txt'
    with open(log_filename, 'w', encoding='utf-8') as f:
        for pasta in pastas:
            f.write(pasta + '\n')
    print(f"Log gerado em: {log_filename}")
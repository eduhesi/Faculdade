import os
import re
from typing import List, Dict, Any
from printer import printer as p, PrinterType

def scan_missing_files(
    start_path: str = '.',
    pattern: str = None,
    pattern_fallback: str = None
) -> Dict[str, Any]:
    """
    Escaneia o diretório procurando arquivos/pastas que seguem o padrão informado,
    identifica números faltantes na sequência, exibe e retorna um resumo.
    """
    if pattern is None:
        pattern = r'c(\d+)$'
    if pattern_fallback is None:
        pattern_fallback = r'c(\d+\.\d+)'
    sequencial_list: List[int] = []
    extra_list: List[str] = []

    for nome in os.listdir(start_path):
        match = re.search(pattern, nome, re.IGNORECASE)
        if match:
            sequencial_list.append(int(match.group(1)))
        else:
            match_full = re.search(pattern_fallback, nome, re.IGNORECASE)
            if match_full:
                extra_list.append(match_full.group(1))

    sequencial_list.sort()
    faltando = []
    if sequencial_list:
        for n in range(sequencial_list[0], sequencial_list[-1]):
            if n not in sequencial_list:
                faltando.append(n)

    total = len(sequencial_list) + len(extra_list)
    esperado = total + len(faltando)

    p(f'Números faltando: {faltando}', PrinterType.ALERT if faltando else PrinterType.SUCCESS)
    p(f'Total na pasta: {total}', PrinterType.OTHER)
    p(f'Total esperado: {esperado}', PrinterType.OTHER)

    return {
        "faltando": faltando,
        "sequencial_list": sequencial_list,
        "extra_list": extra_list,
        "total": total,
        "esperado": esperado
    }
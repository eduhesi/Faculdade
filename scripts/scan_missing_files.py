import os
import subprocess
import sys
import re


start_path = sys.argv[1] if len(sys.argv) > 1 else '.'
sequencial_list = []
extra_list = []
# nomes = ['c001', 'c001.1', 'c003', 'c004', 'c008']

for nome in os.listdir(start_path):
    match = re.search(r'c(\d+)$', nome, re.IGNORECASE)
    if match:
        sequencial_list.append(int(match.group(1)))  # Só a parte inteira
    else:
        # Extrai o número completo após o 'c'
        match_full = re.search(r'c(\d+\.\d+)', nome, re.IGNORECASE)
        if match_full:
            extra_list.append(match_full.group(1))  # Parte com decimal

# Encontrar números faltando na sequência
faltando = []
if sequencial_list:
    for n in range(sequencial_list[0], sequencial_list[-1]):
        if n not in sequencial_list:
            faltando.append(n)
            # faltando.append(f'c{n:03d}')

total = len(sequencial_list) + len(extra_list)
esperado = total + len(faltando)

# base_url = "https://mangafire.to/read/seitokai-yakuindomoo.wo2o/en/chapter-{}"

# for c in faltando:
#     url = base_url.format(c)
#     cmd = [
#         "gallery-dl",
#         "--retries", "0",
#         url
#     ]
#     print(f"Baixando capítulo {f'c{c:03d}'}...")
#     subprocess.run(cmd, check=True)
    
print(f'Números faltando: {faltando}')
print(f'Total na pasta: {total}')
print(f'Total esperado: {esperado}')
print(f'Teste de sanidade 641 - {len(sequencial_list)} = {641 - len(sequencial_list)} == {len(faltando)}')
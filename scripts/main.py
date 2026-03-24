from enum import Enum, auto
import sys
from log import logger
from indexador import indexador
from comparador import comparador
from compressor import compressor
from renomeador import renomear_pastas
from scan_missing_files import scan_missing_files
from varredura import pastas_com_arquivos
from printer import printer as p, PrinterType

class Actions(Enum):
    LOGGER = auto()      # start_path, lista de ignorados?
    INDEXAR = auto()     # start_path
    COMPARAR = auto()    # lista de arquivos
    COMPRIMIR = auto()   # start_path
    RENOMEAR = auto()    # start_path, pattern?
    FALTANTES = auto()   # start_path, pattern base?, pattern auxiliar?
    VARREDURA = auto()   # start_path, lista de excluidos?, lista de tipos?

def print_usage():
    p("Uso: python main.py <acao> [parametros...]", PrinterType.OTHER)
    p("Ações disponíveis: " + ", ".join([a.name.lower() for a in Actions]), PrinterType.ALERT)

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    acao = sys.argv[1].upper()
    parametros = sys.argv[2:]

    try:
        action = Actions[acao]
    except KeyError:
        p(f"Ação desconhecida: {acao}", PrinterType.ERROR)
        print_usage()
        sys.exit(1)

    match action:
        case Actions.LOGGER:
            start_path = parametros[0] if parametros else '.'
            ignorados = parametros[1:] if len(parametros) > 1 else None
            logger(start_path, ignorados)
        case Actions.INDEXAR:
            start_path = parametros[0] if parametros else '.'
            indexador(start_path)
        case Actions.COMPARAR:
            if not parametros:
                p("Uso: python main.py comparar <arquivo1> <arquivo2> ...", PrinterType.OTHER)
                return
            comparador(parametros)
        case Actions.COMPRIMIR:
            start_path = parametros[0] if parametros else '.'
            compressor(start_path)
        case Actions.RENOMEAR:
            start_path = parametros[0] if parametros else '.'
            pattern = parametros[1] if len(parametros) > 1 else None
            renomear_pastas(start_path, pattern)
        case Actions.FALTANTES:
            start_path = parametros[0] if parametros else '.'
            pattern = parametros[1] if len(parametros) == 2 else None
            pattern_fallback = parametros[2] if len(parametros) == 3 else None
            
            scan_missing_files(start_path, pattern, pattern_fallback)
        case Actions.VARREDURA:
            start_path = parametros[0] if parametros else '.'
            pastas = pastas_com_arquivos(parametros[0])
            p(pastas)

if __name__ == '__main__':
    main()
import sys
from log import logger
from indexador import indexador

def main():
  start_path = sys.argv[1] if len(sys.argv) > 1 else '.'
  indexador(start_path)
  logger(start_path)

if __name__ == '__main__':
  main()
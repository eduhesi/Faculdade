# Cores

from enum import Enum


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
MAGENTA = '\033[35m'

class PrinterType(Enum):
  ERROR = RED
  SUCCESS = GREEN
  ALERT = YELLOW
  ERROR_MESSAGE = MAGENTA
  OTHER = BLUE

def printer(message: str, type: PrinterType = PrinterType.OTHER):
  print(f"{type.value}{message}{RESET}")
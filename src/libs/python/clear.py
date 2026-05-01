import platform
import os

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
  
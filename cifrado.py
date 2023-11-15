import msvcrt
from art import *
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    SKYBLUE = '\033[36m'
    ORANGE = '\033[33m'



def getpass(prompt="Put your password: " + bcolors.ORANGE):
    print(bcolors.SKYBLUE)
    print(prompt, end='', flush=True)
    password = ""
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            break
        elif char == '\b':
            password = password[:-1]  # Retroceso (borrar último carácter)
        else:
            password += char
            print('*', end='', flush=True)
    print()  # Nueva línea después de la entrada
    return password



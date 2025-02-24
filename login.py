import os
import time
import hashlib

#Funções externas

from textUtils import *
from mysql_general_config import *
from menu import *

def hash_password(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def login():
    os.system('cls')
    printTitleBarHeavyBorder("Autenticação necessária", YELLOW, YELLOW)
    drawRoundBorderBox(1, 4, 120, 7)
    print('\n')
    gotoxy(3, 5)

    nome = input("Insira o nome de usuário(máx 16 caracteres) | Tecle 0 para sair: ")

    if nome == "0":
        os.system('cls')
        printTitleBar("Encerrando...", YELLOW, YELLOW)
        time.sleep(3)
        os.system('cls')
        printTitleBar("Até logo!", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
        print('\n')
        time.sleep(3)
        exit()


    resultado = executarConsulta(f"SELECT * FROM usuario where nome_usuario = '{nome}'")

    if not resultado:
        gotoxy(3, 6)
        printYellow("Nenhum usuário encontrado com o nome informado...")
        gotoxy(3, 7)
        input("Pressione enter para continuar...")
        login()

    gotoxy(3, 6)
    
    senha = input("Insira sua senha(máx 16 caracteres): ")

    if hash_password(senha) != resultado[0][2]:
        gotoxy(3, 8)
        printRed("Senha incorreta...")
        gotoxy(3, 9)
        input("Pressione enter para encerrar...")
        gotoxy(3, 8)

        time.sleep(.4)
        os.system('cls')
        printTitleBarHeavyBorder("Até Logo!", MAGENTA, MAGENTA)
        time.sleep(3)
        gotoxy(1, 8)
        exit()     

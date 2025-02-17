import os
import time
from mysql_general_config import *
from textUtils import *

## Apenas aqui...

from menu import *
from funcoes_de_cadastro import *
from funcoes_de_listagem import *


def main():
    os.system('cls')
    for n in range(101):
        printProgressBar(n, 1, BRIGHT_GREEN, GREEN, WHITE, BACKGROUND_GREEN)
        time.sleep(0.01)
    time.sleep(1)
    # Menu loop
    while True:
        desenhar_menu()
        opcao = input("Digite a opção desejada: ")
        try:
            if opcao == "1":
                os.system("cls")
                listar_alunos()

            elif opcao == "2":
                os.system("cls")
                listar_funcionarios()

            elif opcao == "3":
                os.system("cls")
                listar_planos()

            elif opcao == "4":
                os.system("cls")
                listar_equipamentos()

            elif opcao == "5":
                os.system("cls")
                listar_fornecedores()

            elif opcao == "6":
                os.system("cls")
                listar_turmas()

            elif opcao == "7":
                os.system("cls")
                cadastrar_aluno()

            elif opcao == "8":
                os.system("cls")
                cadastrar_funcionario()

            elif opcao == "0":
                os.system("cls")
                
                def closing():
                    for n in range(101):
                        printProgressBar(n, 1, RED, RED, WHITE, BACKGROUND_WHITE)
                        time.sleep(0.008)
            
                closing()
                time.sleep(1)
                os.system('cls')
                printBrightCyan("Obrigado por utilizar nosso sistema!")
                break

        except Exception as e:
            print("Opção inválida! Tente novamente...", e)
            input("pressione enter para continuar...")

main()
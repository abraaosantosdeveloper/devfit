import os
import time
from mysql_general_config import *
from textUtils import *

## Apenas aqui...

from menu import *
from funcoes_de_cadastro import *
from funcoes_de_listagem import *
from funcoes_exclusao import *


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

            elif opcao == "9":
                os.system("cls")
                cadastrar_plano()
                return
            
            elif opcao == "10":
                os.system('cls')
                cadastrar_equipamento()

            elif opcao == "11":
                os.system('cls')
                cadastrar_fornecedor()

            elif opcao == "12":
                os.system('cls')
                cadastrar_turma()

           # Funções de atualização devem ser implementadas aqui!!!
           # {...}

            elif opcao == "19":
                os.system('cls')
                excluir_aluno()
            
            elif opcao == "20":
                os.system('cls')
                excluir_funcionario()

            elif opcao == "21":
                os.system('cls')
                excluir_plano()

            elif opcao == "22":
                os.system('cls')
                excluir_equipamento()   

            elif opcao == "23":
                os.system('cls')
                excluir_fornecedor()

            elif opcao == "24":
                os.system('cls')
                excluir_turma()         

            elif opcao == "0":
                os.system("cls")
                
                def closing():
                    for n in range(101):
                        printProgressBar(n, 1, RED, RED, WHITE, BACKGROUND_WHITE)
                        time.sleep(0.008)
            
                closing()
                time.sleep(1)
                os.system('cls')
                printTitleBarHeavyBorder("Obrigado por utilizar nosso sistema!", MAGENTA, MAGENTA)
                time.sleep(4)
                clearScreen()
                break

        except Exception as e:
            print("Opção inválida! Tente novamente...", e)
            input("pressione enter para continuar...")

main()
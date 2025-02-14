import os
import time
from mysql_general_config import *
from textUtils import *
from menu import *


# Funções de Listagem
# Listar Alunos
def listar_alunos():

    resultado = executarConsulta("SELECT * FROM aluno")

    print("="*35 + " Alunos " + "="*35)
    print(f"{'Nome':30}{'CPF':30}{'Data de Nascimento':15}")
    for linha in resultado:
        print(f"{linha[1]:28} | {linha[2]:27} | {str(linha[3]):15}")
    print('\n')
    input("Pressione enter para continuar...")

# Listar funcionários
def listar_funcionarios():

    resultado = executarConsulta("SELECT * FROM funcionario")

    print("="*55 + " Funcionários " + "="*55)
    print(f"{'ID':4}{'CPF':15}{'Nome':30}{'Cargo':18}{'Contato':18}{'Salário':18}{"Contratação":15}")
    for linha in resultado:
        print(f"{linha[0]:2} | {linha[1]:12} | {linha[2]:27} | {linha[4]:15} | {linha[6]:15} | {str(linha[7]):15} | {str(linha[8])}")
    print('\n')
    input("Pressione enter para continuar...")

def listar_planos():
    resultado = executarConsulta("SELECT * FROM plano")

    print("="*35 + " Planos " + "="*35)
    print(f"{'ID':4}{'Valor':18}{'Período':30}{"Descrição":15}")
    for linha in resultado:
        print(f"{linha[0]:2} | R$ {str(linha[1]):12} | {linha[2]:27} | {linha[3]:15}")
    print('\n')
    input("Pressione enter para continuar...")

def listar_equipamentos():
    return

def listar_fornecedores():
    return


# Funções de Cadastro
def cadastrar_funcionario():
    return

def cadastrar_aluno(): 
    os.system("cls")
    print("Cadastro de Alunos")
    print("Digite os dados abaixo:\n")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nasc = input("Data de Nascimento(aaaa-mm-dd): ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")
    turma = int(input("Turma: "))
    plano = input("Plano(Mensal, trimestral ou semestral): ")

    query = f"""INSERT INTO aluno(nome, cpf, nascimento, endereco, contato, turma, plano) VALUES('{nome}', '{cpf}', '{data_nasc}', '{endereco}', '{contato}', '{turma}', '{plano}')"""

    
    try:
        executarComando(query)
        print("Aluno cadastrado com sucesso!")
        input("pressione enter para continuar...")
    except Exception as e:
        print("Erro ao cadastrar aluno: ", e)


def cadastrar_equipamento():
    return

def cadastrar_fornecedor():
    return


def main():
    while True:
        os.system("cls")
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

            elif opcao == "6":
                os.system("cls")
                cadastrar_aluno()

            elif opcao == "0":
                os.system("cls")
            def progress_bar(done):
                printBrightYellow("\rEncerrando sistema: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100), end='')
            
            def closing():
                for n in range(101):
                    progress_bar(n / 100)
                    time.sleep(0.01)
            
            closing()
            time.sleep(1)
            os.system('cls')
            printBrightCyan("Obrigado por utilizar nosso sistema!")
            break
        except Exception as e:
            print("Opção inválida! Tente novamente...", e)
            input("pressione enter para continuar...")

main()
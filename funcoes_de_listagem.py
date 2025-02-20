
from mysql_general_config import *
from textUtils import *


# Funções de Listagem

def listar_alunos():

    resultado = executarConsulta("SELECT * FROM aluno")

    printTitleBar("Alunos", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'Nome':30}{'CPF':20}{'Data de Nasc.':17}{'Contato':14}{'Turma':4}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:27} | {linha[2]:17} | {str(linha[3]):14} | {linha[5]:8} | {linha[6]}")
    print('\n')
    input("Pressione enter para continuar...")

def listar_funcionarios():

    resultado = executarConsulta("SELECT * FROM funcionario")

    printTitleBar("Funcionários", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'CPF':15}{'Nome':30}{'Cargo':18}{'Contato':18}{'Salário':18}{"Contratação":15}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:12} | {linha[2]:27} | {linha[4]:15} | {linha[6]:15} | {str(linha[7]):15} | {str(linha[8])}")
    print('\n')
    input("Pressione enter para continuar...")

def listar_planos():
    resultado = executarConsulta("SELECT * FROM plano")

    printTitleBar("Planos", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    print(f"{'ID':4}{'Valor':18}{'Período':30}{"Descrição":15}")
    for linha in resultado:
        print(f"{linha[0]:2} | R$ {str(linha[1]):12} | {linha[2]:27} | {linha[3]:15}")
    print('\n')
    input("Pressione enter para continuar...")

def listar_equipamentos():
    resultado = executarConsulta("SELECT * FROM equipamento")

    printTitleBar("Equipamentos", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:    
        print(f"{'ID':4}{'Equipamento':30}{'Modalidade':18}{'Preço':10}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:27} | {linha[6]:15} | {str(linha[2])}")
    print('\n')
    input("Pressione enter para continuar...")

def listar_fornecedores():
    resultado = executarConsulta("SELECT * FROM fornecedor where fornecedor_ativo = 1")

    printTitleBar("Fornecedores Ativos", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'Nome':20}{'Endereço':20}{'Telefone':18}{'Email':30}{'Vigencia do contrato':15}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:17} | {linha[2]:17} | {linha[3]:15} | {linha[4]:27} | {str(linha[5]):8}")
    print('\n')
    input("Pressione enter para continuar...")

def listar_turmas():
    resultado = executarConsulta("SELECT * FROM turma")

    printTitleBar("Planos", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'Horário':18}")
        for linha in resultado:
            print(f"{linha[0]:2} | {str(linha[1]):12}")
    print('\n')
    input("Pressione enter para continuar...")




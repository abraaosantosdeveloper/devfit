import os
from mysql_general_config import *
from textUtils import *

def excluir_aluno():
    os.system("cls")
    printTitleBar("Excluir Aluno", BRIGHT_RED, BRIGHT_RED)
    gotoxy(1, 5)


    resultado = executarConsulta("SELECT * FROM aluno")

    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'Nome':30}{'CPF':20}{'Data de Nasc.':17}{'Contato':14}{'Turma':4}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:27} | {linha[2]:17} | {str(linha[3]):14} | {linha[5]:8} | {linha[6]}")
    print('\n')
    input("Pressione enter para continuar...")
    
    id = int(input("Insira o id do aluno que você quer excluir (digite 0 para cancelar): "))
    query = f"""DELETE FROM aluno where id = {id}"""
    
    if id != 0:
        try:
            executarComando(query)
            print("Aluno excluído")
            input("Precione enter para continuar")
        except Exception as e:
            print("Erro ao excluir aluno: ", e)
            input("pressione enter para continuar...")
    else:
        return
        
def excluir_funcionario():
    os.system("cls")
    printTitleBar("Excluir Funcionario", BRIGHT_RED, BRIGHT_RED)
    gotoxy(1, 5)


    resultado = executarConsulta("SELECT * FROM funcionario")

    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'CPF':15}{'Nome':30}{'Cargo':18}{'Contato':18}{'Salário':18}{"Contratação":15}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:12} | {linha[2]:27} | {linha[4]:15} | {linha[6]:15} | {str(linha[7]):15} | {str(linha[8])}")
    print('\n')
    input("Pressione enter para continuar...")
    
    id = int(input("Insira o id do funcionario que você quer excluir (digite 0 para cancelar): "))
    query = f"""DELETE FROM funcionario where id = {id}"""

    if id != 0:
   
        try:
            executarComando(query)
            print("Funcionario excluído")
            input("Precione enter para continuar")
        except Exception as e:
            print("Erro ao excluir funcionario: ", e)
            input("pressione enter para continuar...")
    else:
        return
        
        
def excluir_plano():
    os.system("cls")
    printTitleBar("Excluir plano", BRIGHT_RED, BRIGHT_RED)
    gotoxy(1, 5)

    resultado = executarConsulta("SELECT * FROM plano")

    print(f"{'ID':4}{'Valor':18}{'Período':30}{"Descrição":15}")
    for linha in resultado:
        print(f"{linha[0]:2} | R$ {str(linha[1]):12} | {linha[2]:27} | {linha[3]:15}")
    print('\n')
    input("Pressione enter para continuar...")

    
    id = int(input("Insira o id do plano que você quer excluir (digite 0 para cancelar): "))
    query = f"""DELETE FROM plano where id = {id}"""
    
    if id != 0:
        try:
            executarComando(query)
            print("Plano excluído")
            input("Precione enter para continuar")
        except Exception as e:
            print("Erro ao excluir o plano: ", e)
            input("pressione enter para continuar...")
    else:
        return
        
        
def excluir_equipamento():
    os.system("cls")
    printTitleBar("Excluir equipamento", BRIGHT_RED, BRIGHT_RED)
    gotoxy(1, 5)

    resultado = executarConsulta("SELECT * FROM equipamento")

    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:    
        print(f"{'ID':4}{'Equipamento':30}{'Modalidade':18}{'Preço':10}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:27} | {linha[6]:15} | {str(linha[2])}")
    print('\n')
    input("Pressione enter para continuar...")

    id = int(input("Insira o id do equipamento que você quer excluir (digite 0 para cancelar): "))
    query = f"""DELETE FROM equipamento where id = {id}"""
    
    if id != 0:
   
        try:
            executarComando(query)
            print("Equipamento excluído")
            input("Precione enter para continuar")
        except Exception as e:
            print("Erro ao excluir equipamento: ", e)
            input("pressione enter para continuar...")
    else:
        return


def excluir_fornecedor():
    os.system("cls")
    printTitleBar("Excluir fornecedor", BRIGHT_RED, BRIGHT_RED)
    gotoxy(1, 5)

    resultado = executarConsulta("SELECT * FROM fornecedor where fornecedor_ativo = 1")

    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'Nome':20}{'Endereço':20}{'Telefone':18}{'Email':30}{'Vigencia do contrato':15}")
        for linha in resultado:
            print(f"{linha[0]:2} | {linha[1]:17} | {linha[2]:17} | {linha[3]:15} | {linha[4]:27} | {str(linha[5]):8}")
    print('\n')
    input("Pressione enter para continuar...")
    
    id = int(input("Insira o id do aluno que você quer excluir (digite 0 para cancelar): "))
    query = f"""UPDATE fornecedor set fornecedor_ativo = 0 where id = {id}"""
    
    if id != 0:
   
        try:
            executarComando(query)
            print("Fornecedor excluído")
            input("Precione enter para continuar")
        except Exception as e:
            print("Erro ao excluir fornecedor: ", e)
            input("pressione enter para continuar...")
    else:
        return
        

def excluir_turma():
    os.system("cls")
    printTitleBar("Excluir turma", BRIGHT_RED, BRIGHT_RED)
    gotoxy(1, 5)

    resultado = executarConsulta("SELECT * FROM turma")

    gotoxy(1, 5)
    if not resultado:
        printColored("Não há nenhum registro...", YELLOW)
    else:
        print(f"{'ID':4}{'Horário':18}")
        for linha in resultado:
            print(f"{linha[0]:2} | {str(linha[1]):12}")
    print('\n')
    input("Pressione enter para continuar...")
    
    id = int(input("Insira o id do turma que você quer excluir (digite 0 para cancelar): "))
    query = f"""DELETE FROM turma where id = {id}"""
    
    if id != 0:
   
        try:
            executarComando(query)
            print("Turma excluída")
            input("Precione enter para continuar")
        except Exception as e:
            print("Erro ao excluir turma: ", e)
            input("pressione enter para continuar...")
    else:
        return
import os
from mysql_general_config import *
from textUtils import *

def excluir_aluno():
    os.system("cls")
    printTitleBar("Excluir Aluno", BRIGHT_RED, BRIGHT_RED)
    gotoxy(1, 5)
    
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
    
    id = int(input("Insira o id do aluno que você quer excluir (digite 0 para cancelar): "))
    query = f"""DELETE FROM fornecedor where id = {id}"""
    
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
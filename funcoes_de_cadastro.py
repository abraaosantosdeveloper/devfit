import os
from mysql_general_config import *
from textUtils import *

# Funções de Cadastro
def cadastrar_funcionario():
    os.system("cls")
    printTitleBar("Cadastro de Funcionário", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    nome = input("Insira o nome do funcionario (digite 0 para cancelar): ")
    cpf = input("Insira o cpf do funcionário: ")
    nascimento = input("Insira a data de nascimento(aaaa-mm-dd): ")
    cargo = input("Insira o cargo do funcionario: ")
    especialidade = input("Digite a especialidade: ")
    contato = input("Telefone de contato(somente números): ")
    salario = float(input("Insira o salário do funcionário(xxxxx.xx): "))
    data_contratacao = input("Insira a data de contratação(aaaa-mm-dd): ")
    comando = f"INSERT INTO funcionario (cpf, nome, nascimento, cargo, especialidade, contato, salario, data_contratacao ) VALUES ('{cpf}', '{nome}','{nascimento}', '{cargo}', '{especialidade}', '{contato}', '{salario}', '{data_contratacao}');"
    try:
        executarComando(comando)
        print("Funcionário cadastrado com sucesso!!")
        input("Pressione enter para continuar...")
    except Exception as err:
        print("Erro ao cadastrar funcionário. ", err)
        input("Pressione enter para continuar...")


def cadastrar_aluno(): 
    os.system("cls")
    printTitleBar("Planos", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    nome = input("Insira o nome: ")
    cpf = input("Insira o CPF: ")
    data_nasc = input("Insira a data de dascimento(aaaa-mm-dd): ")
    endereco = input("Informe o endereço: ")
    contato = input("Informe o telefone(Somente números): ")
    turma = int(input("Insira o Id da turma: "))
    plano = int(input("Insira o Id do Plano: "))

    query = f"""INSERT INTO aluno(nome, cpf, nascimento, endereco, contato, turma, plano) VALUES('{nome}', '{cpf}', '{data_nasc}', '{endereco}', '{contato}', '{turma}', '{plano}')"""

    try:
        executarComando(query)
        print("Aluno cadastrado com sucesso!")
        input("pressione enter para continuar...")
    except Exception as e:
        print("Erro ao cadastrar aluno: ", e)
        input("pressione enter para continuar...")



def cadastrar_equipamento():
    return

def cadastrar_fornecedor():
    return

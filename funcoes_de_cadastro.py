import os
import time
from mysql_general_config import *
from textUtils import *
from login import hash_password

# Funções de Cadastro
def cadastrar_funcionario():
    clearScreen()
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
    clearScreen()
    printTitleBar("Cadastro de aluno", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
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
        clearScreen()
        printTitleBar("Aluno cadastrado com sucesso!", GREEN, GREEN)
        gotoxy(1, 5)
        input("pressione enter para continuar...")
    except Exception as e:
        clearScreen()
        printTitleBar("ERRO AO CADASTRAR ALUNO!", RED, RED)
        gotoxy(1, 5)
        print(e)
        input("pressione enter para continuar...")



def cadastrar_equipamento():
    clearScreen()
    printTitleBar("Equipamento", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    descricao = input("Insira a descrição do equipamento: ")
    data_compra = input("Insira a data de compra do equipamento(aaaa-mm-dd): ")
    preco = input("Informe o preço do equipamento: ")
    id_fornecedor = int(input("Informe o id do Fornecedor(Somente números): "))
    ultima_manutencao = input("Insira a data da ultima manutenção(aaaa-mm-dd): ")
    prox_manutencao = input("Insira a data da proxima manutenção(aaaa-mm-dd): ")
    modalidade = input("Insira a modalidade do equipamento: ")

    query = f"""INSERT INTO equipamento(descricao, preco, data_compra, id_fornecedor, ultima_manutencao, proxima_manutencao, modalidade) VALUES('{descricao}', '{preco}', '{data_compra}', '{id_fornecedor}', '{ultima_manutencao}', '{prox_manutencao}','{modalidade}')"""

    try:
        executarComando(query)
        clearScreen()
        printTitleBar("Equipamento cadastrado com sucesso!", GREEN, GREEN)
        gotoxy(1, 5)
        input("pressione enter para continuar...")
    except Exception as e:
        clearScreen()
        printTitleBar("Erro ao cadastrar equipamento", RED, RED)
        gotoxy(1, 5)
        print(e)
        input("pressione enter para continuar...")

def cadastrar_fornecedor():
    clearScreen()
    printTitleBar("Fornecedor", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    nome = input("Insira o nome do Fornecedor: ")
    endereco = input("Insira o endereço do fornecedor: ")
    telefone = input("Insira a data de compra do equipamento(aaaa-mm-dd): ")
    email = input("Informe o email do fornecedor: ")
    vigencia_contrato = input("Insira a data de vigência do contrato(aaaa-mm-dd): ")
    
    query = f"""INSERT INTO fornecedor(nome, endereco, telefone, email, vigencia_contrato) VALUES('{nome}', '{endereco}', '{telefone}', '{email}', '{vigencia_contrato}')"""

    try:
        executarComando(query)
        print("Fornecedor cadastrado com sucesso!")
        input("pressione enter para continuar...")
    except Exception as e:
        print("Erro ao cadastrar Fornecedor: ", e)
        input("pressione enter para continuar...")

def cadastrar_plano():
    os.system("cls")
    printTitleBar("Plano", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    valor = input("Insira o valor do plano: ")
    periodo = input("Insira o periodo do plano: ")
    descricao = input("Descrição do plano")
    query = f"""INSERT INTO plano(valor, periodo, descricao) VALUES('{valor}', '{periodo}','{descricao}')"""

    try:
        executarComando(query)
        print("plano cadastrado com sucesso!")
        input("pressione enter para continuar...")
    except Exception as e:
        print("Erro ao cadastrar plano: ", e)
        input("pressione enter para continuar...")

def cadastrar_turma():
    os.system("cls")
    printTitleBar("Turma", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    horario = input("Insira o horario da turma: ")
    
    query = f"""INSERT INTO turma(horario) VALUES('{horario}')"""

    try:
        executarComando(query)
        print("Turma cadastrado com sucesso!")
        input("pressione enter para continuar...")
    except Exception as e:
        print("Erro ao cadastrar Turma: ", e)
        input("pressione enter para continuar...")

def cadastrar_usuario():
    os.system('cls')
    printTitleBarRoundBorder("Cadastro de usuário", BRIGHT_GREEN, GREEN)
    drawBox(1, 4, 120, 10)
    gotoxy(3, 5)
    nome_usuario = input("Insira o nome de usuário(Máx. 20 caracteres) | digite 0 para encerrar: ")

    if nome_usuario == "0":
        os.system('cls')
        printTitleBarRoundBorder("Até logo!", MAGENTA, MAGENTA)
        time.sleep(2)
        gotoxy(1, 5)
        exit()
    
    gotoxy(3, 6)
    senha = input("Insira sua senha(Máx. 16 caracteres): ")
    hash_senha = hash_password(senha)

    if nome_usuario == "" or senha == "":
        gotoxy(3, 7)
        printColored("Todos os campos são obrigatórios! ")
        gotoxy(3, 8)
        input("Pressione enter para continuar...")
        cadastrar_usuario()

    

    query = f"INSERT INTO usuario(nome_usuario, senha) VALUES ('{nome_usuario}', '{hash_senha}')"
    executarComando(query)
    gotoxy(3, 7)
    print("Usuário cadastrado com sucesso!")
    gotoxy(3, 8)
    input("Pressione enter para continuar...")
    return
    

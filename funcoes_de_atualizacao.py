import os
from mysql_general_config import *
from textUtils import *

def update_aluno():
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
    os.system('cls')

    printTitleBarHeavyBorder("Atualizar registro de aluno", YELLOW, YELLOW)
    gotoxy(1,5)
    id = int(input("Digite o id do Aluno que você deseja atualizar os dados: "))
    if id == 0 or id == "":
        print("Voltando ao menu principal...")
        input("Pressione enter para voltar ao menu...")
        return
    updates = []
    nome = input("Digite o novo nome do Aluno(0 para cancelar): ")
    if nome != "": updates.append(f"nome = '{nome}'")

    cpf = input("Digite o novo CPF do aluno: ")
    if cpf != "": updates.append(f"cpf = '{cpf}'")

    nascimento = input("Digite a nova data de nascimento do aluno (0000-00-00): ")
    if nascimento != "": updates.append(f"nascimento = '{nascimento}'")

    endereco = input("Digite o novo endereço do aluno: ")
    if endereco != "": updates.append(f"endereco = '{endereco}'")

    contato = input("Digite o novo contato do aluno: ")
    if contato != "": updates.append(f"contato = '{contato}'")

    turma = input("Digite a nova turma do aluno: ")
    if turma != "": updates.append(f"turma = '{turma}'")

    plano = input("Digite o novo plano do aluno: ")
    if plano != "": updates.append(f"plano = '{plano}'")

    if nome == "0" or not updates: return
    else: query = f"UPDATE aluno SET {', '.join(updates)} WHERE id = '{id}'"
    
    
    try:
        executarComando(query)
        print("Aluno atualizado com sucesso!")
        input("Pressione enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione enter para voltar ao menu...") 
            

def update_funcionario():
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
    os.system('cls')

    printTitleBarHeavyBorder("Atualizar registro de funcionário", YELLOW, YELLOW)
    gotoxy(1,5)
    id = int(input("Digite o id do Funcionario que você deseja atualizar os dados: "))
    if id == 0 or id == "":
            print("Voltando ao menu principal...")
            input("Pressione enter para voltar ao menu...")
            return
    updates = []
    nome = input("Digite o novo nome do Funcionário(0 para cancelar): ")
    if nome != "": updates.append(f"nome = '{nome}'")

    cpf = input("Digite o novo CPF do Funcionário: ")
    if cpf != "": updates.append(f"cpf = '{cpf}'")

    nascimento = input("Digite a nova data de nascimento do Funcionário (0000-00-00): ")
    if nascimento != "": updates.append(f"nascimento = '{nascimento}'")

    endereco = input("Digite o novo endereço do Funcionário: ")
    if endereco != "": updates.append(f"endereco = '{endereco}'")

    contato = input("Digite o novo contato do funcionário: ")
    if contato != "": updates.append(f"contato = '{contato}'")

    cargo = input("Digite o novo cargo do funcionário: ")
    if cargo != "": updates.append(f"cargo = '{cargo}'")

    especialidade = input("Digite a especialidade: ")
    if especialidade != "": updates.append(f"especialidade = '{especialidade}'")

    salario = input("Digite a correção salarial (separado por ponto '.'): ")
    if salario != "": updates.append(f"salario = '{salario}'")

    contratacao = input("Digite a nova data de contratacao do Funcionário (0000-00-00): ")
    if contratacao != "": updates.append(f"contratacao = '{contratacao}'")

    if nome == "0" or not updates: return
    else: query = f"UPDATE funcionario SET {', '.join(updates)} WHERE id = '{id}'"

    try:
        executarComando(query)
        print("Funcionario atualizado com sucesso!")
        input("Pressione enter para voltar ao menu...")
    except Exception as e:
        if KeyboardInterrupt:
            print("Operação cancelada pelo usuário...")
        print(f"Ocorreu um erro: {e}")
        input("Pressione enter para voltar ao menu...") 
        

def update_equipameto():
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
    os.system('cls')

    printTitleBarHeavyBorder("Atualizar registro de equipamento", YELLOW, YELLOW)
    gotoxy(1,5)
    id = int(input("Digite o id do Equipamento que você deseja atualizar os dados: "))
    if id == 0  or id == "":
        print("Voltando ao menu principal...")
        input("Pressione enter para voltar ao menu...")
        return

    updates = []

    descricao = input("Digite a descrição do Equipamento(ou 0 para cancelar): ")
    if descricao != "": updates.append(f"descricao = '{descricao}'")

    preco = input("Digite o preço do Equipamento (separado por ponto '.'): ")
    if preco != "": updates.append(f"preco = '{preco}'")
    
    id_fornecedor = input("Digite o id do fornecedor: ")
    if id_fornecedor != "": updates.append(f"id_fornecedor = '{id_fornecedor}'")

    ultima_manutencao = input("Digite a data da ultima manutenção(0000-00-00): ")
    if ultima_manutencao != "": updates.append(f"ultima_manutencao = '{ultima_manutencao}'")

    proxima_manutencao = input("Digite data da proxima manutenção(0000-00-00): ")
    if proxima_manutencao != "": updates.append(f"proxima_manutencao = '{proxima_manutencao}'")

    modalidade = input("Digite a modalidade do equipamento: ")
    if modalidade != "": updates.append(f"modalidade = '{modalidade}'")

    data_compra = input("Digite data de compra do equipamento(0000-00-00): ")
    if data_compra != "": updates.append(f"data_compra = '{data_compra}'")

    if descricao == '0' or not updates: return

    else: query = f"UPDATE equipamento SET {', '.join(updates)} WHERE id='{id}'"
    
    
    try:
        executarComando(query)
        print("Equipamento atualizado com sucesso!")
        input("Pressione enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione enter para voltar ao menu...") 
            
def update_plano():
    resultado = executarConsulta("SELECT * FROM plano")

    printTitleBar("Planos", BRIGHT_MAGENTA, BRIGHT_MAGENTA)
    gotoxy(1, 5)
    print(f"{'ID':4}{'Valor':18}{'Período':30}{"Descrição":15}")
    for linha in resultado:
        print(f"{linha[0]:2} | R$ {str(linha[1]):12} | {linha[2]:27} | {linha[3]:15}")
    print('\n')
    input("Pressione enter para continuar...")
    os.system('cls')

    printTitleBarHeavyBorder("Atualizar registro de planos", YELLOW, YELLOW)
    gotoxy(1,5)
    id = int(input("Digite o id do plano que você deseja atualizar os dados: "))
    if id == 0 or id == "":
            print("Voltando ao menu principal...")
            input("Pressione enter para voltar ao menu...")
            return
    
    updates = []

    valor = input("Digite o valor do plano(separado por ponto '.')|(0 para cancelar): ")
    if valor != "": updates.append(f"valor = '{valor}'")

    periodo = input("Digite o periodo do plano: ")
    if periodo != "": updates.append(f"periodo = '{periodo}'")

    descricao = input("Digite a descricao do plano: ")
    if descricao != "": updates.append(f"descricao = '{descricao}'")

    if valor == "0" or not updates: return

    else:
        query = f"UPDATE plano SET {', '.join(updates)} WHERE id = '{id}'"
    
    
    try:
        executarComando(query)
        print("Plano atualizado com sucesso!")
        input("Pressione enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione enter para voltar ao menu...") 
            

def update_turma():
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
    os.system('cls')

    printTitleBarHeavyBorder("Atualizar registro de turma", YELLOW, YELLOW)
    gotoxy(1,5)
    id = int(input("Digite o id da turma que você deseja atualizar os dados: "))
    if id == 0 or id == "":
            print("Voltando ao menu principal...")
            input("Pressione enter para voltar ao menu...")
            return
    
    updates = []

    horario = input("Digite o novo horario da turma: ")
    if horario != "": updates.append(f"horario = '{horario}'")

    if horario == "" or not updates: return
    else: query = f"UPDATE turma SET {', '.join(updates)} WHERE id = '{id}'"
    
    try:
        executarComando(query)
        print("Turma atualizado com sucesso!")
        input("Pressione enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione enter para voltar ao menu...") 
            
        
def update_fornecedor():
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
    os.system('cls')

    printTitleBarHeavyBorder("Atualizar registro de Fornecedor", YELLOW, YELLOW)
    gotoxy(1,5)
    id = int(input("Digite o id do Fornecedor que você deseja atualizar os dados: "))
    if id == 0 or id == "":
            print("Voltando ao menu principal...")
            input("Pressione enter para voltar ao menu...")
            return
    updates = []
    nome = input("Digite o novo nome do Forncedor: ")
    if nome != "": updates.append(f"nome = '{nome}'")

    endereco = input("Digite o novo endereço do Fornecedor: ")
    if endereco != "": updates.append(f"endereco = '{endereco}'")

    telefone = input("Digite o novo telefone do Fornecedor: ")
    if telefone != "": updates.append(f"telefone = {telefone}")

    email = input("Digite o novo email do Fornecedor: ")
    if email != "": updates.append(f"email = '{email}'")

    vigencia_contrato = input("Digite a vigencia do contrato: ")
    if vigencia_contrato != "": updates.append(f"vigencia_contrato = '{vigencia_contrato}'")

    if not updates: return
    else: query = f"UPDATE fornecedor SET {', '.join(updates)} WHERE id = '{id}'"
    
    try:
        executarComando(query)
        print("Fornecedor atualizado com sucesso!")
        input("Pressione enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione enter para voltar ao menu...") 
            
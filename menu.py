from textUtils import *
def desenhar_menu():
    os.system('cls')
       
    # Título do menu
    printTitleBarHeavyBorder("⚽ MENU PRINCIPAL | DEVFIT 🥊", BRIGHT_CYAN, BOLD_BRIGHT_CYAN)
    
    # Caixa 1
    drawRoundBorderBox(1, 4, 30, 3, color=BRIGHT_YELLOW)
    gotoxy(3,5)
    printColored("📃 | Consultar", color=BRIGHT_YELLOW)
    
    # Opções da caixa 1
    drawRoundBorderBox(1, 7, 30, 8)
    gotoxy(3,8)
    print("1 - Alunos")
    gotoxy(3,9)
    print("2 - Funcionários")
    gotoxy(3,10)
    print("3 - Planos")
    gotoxy(3,11)
    print("4 - Equipamentos")
    gotoxy(3,12)
    print("5 - Fornecedores")
    gotoxy(3,13)
    print("6 - Turmas")

    # Caixa 2
    drawRoundBorderBox(31, 4, 30, 3, color=BRIGHT_GREEN)
    gotoxy(33,5)
    printColored("📂 | Cadastrar", color=BRIGHT_GREEN)
    
    # Opções da caixa 2
    drawRoundBorderBox(31, 7, 30, 8)
    gotoxy(33,8)
    print("7 - Aluno")
    gotoxy(33,9)
    print("8 - Funcionário")
    gotoxy(33,10)
    print("9 - Plano")
    gotoxy(33,11)
    print("10 - Equipamento")
    gotoxy(33,12)
    print("11 - Fornecedor")
    gotoxy(33,13)
    print("12 - Turma")

    # Caixa 3
    drawRoundBorderBox(61, 4, 30, 3, color=BRIGHT_BLUE)
    gotoxy(63,5)
    printColored("📝 | Atualizar", color=BRIGHT_BLUE)

    # Opções da caixa 3
    drawRoundBorderBox(61, 7, 30, 8)
    gotoxy(63,8)
    print("13 - Alunos")
    gotoxy(63,9)
    print("14 - Funcionário")
    gotoxy(63,10)
    print("15 - Plano")
    gotoxy(63,11)
    print("16 - Equipamento")
    gotoxy(63,12)
    print("17 - Fornecedor")
    gotoxy(63,13)
    print("18 - Turma")
    
    # Caixa 4
    drawRoundBorderBox(91, 4, 30, 3, color=RED)
    gotoxy(93,5)
    printColored("⛔ | Excluir", color=RED)
    
    # Opções da caixa 4
    drawRoundBorderBox(91, 7, 30, 8)
    gotoxy(93,8)
    print("19 - Aluno")
    gotoxy(93,9)
    print("20 - Funcionário")
    gotoxy(93,10)
    print("21 - Plano")
    gotoxy(93,11)
    print("22 - Equipamento")
    gotoxy(93,12)
    print("23 - Fornecedor")
    gotoxy(93,13)
    print("24 - Turma")

    drawRoundBorderBox(1, 15, 30, 3, color=RED)
    gotoxy(3, 16)
    printRed("Digite 0 para encerrar...")

    # Input
    drawRoundBorderBox(31, 15, 30, 3, color=BRIGHT_CYAN)
    gotoxy(33, 16)
    print("nu - Criar novo usuário")
    drawRoundBorderBox(1, 18, 120, 3, BRIGHT_BLUE)
    gotoxy(3, 19)


from textUtils import *
import time
def desenhar_menu():
    os.system('cls')
    for n in range(101):
        printProgressBar(n, 1, BRIGHT_GREEN, GREEN, WHITE, BACKGROUND_GREEN)
        time.sleep(0.01)
        
    time.sleep(1)
    os.system('cls')
    
    
    # Título do menu
    printTitleBar("⚽ MENU PRINCIPAL | DEVFIT 🥊", BRIGHT_CYAN, BOLD_BRIGHT_CYAN)
    
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

    # Caixa 2
    drawRoundBorderBox(31, 4, 30, 3, color=BRIGHT_GREEN)
    gotoxy(33,5)
    printColored("📂 | Cadastrar", color=BRIGHT_GREEN)
    
    # Opções da caixa 2
    drawRoundBorderBox(31, 7, 30, 8)
    gotoxy(33,8)
    print("6 - Aluno")
    gotoxy(33,9)
    print("7 - Funcionário")
    gotoxy(33,10)
    print("8 - Plano")
    gotoxy(33,11)
    print("9 - Equipamento")
    gotoxy(33,12)
    print("10 - Fornecedor")

    # Caixa 3
    drawRoundBorderBox(61, 4, 30, 3, color=BRIGHT_BLUE)
    gotoxy(63,5)
    printColored("📝 | Atualizar", color=BRIGHT_BLUE)

    # Opções da caixa 3
    drawRoundBorderBox(61, 7, 30, 8)
    gotoxy(63,8)
    print("11 - Alunos")
    gotoxy(63,9)
    print("12 - Funcionário")
    gotoxy(63,10)
    print("13 - Plano")
    gotoxy(63,11)
    print("14 - Equipamento")
    gotoxy(63,12)
    print("15 - Fornecedor")
    
    # Caixa 4
    drawRoundBorderBox(91, 4, 30, 3, color=RED)
    gotoxy(93,5)
    printColored("⛔ | Excluir", color=RED)
    
    # Opções da caixa 4
    drawRoundBorderBox(91, 7, 30, 8)
    gotoxy(93,8)
    print("16 - Aluno")
    gotoxy(93,9)
    print("17 - Funcionário")
    gotoxy(93,10)
    print("18 - Plano")
    gotoxy(93,11)
    print("19 - Equipamento")
    gotoxy(93,12)
    print("20 - Fornecedor")

    drawRoundBorderBox(1, 15, 30, 3, color=RED)
    gotoxy(3, 16)
    printRed("Digite 0 para cancelar...")

    # Input
    drawRoundBorderBox(31, 15, 34, 3, color=BRIGHT_CYAN)
    gotoxy(33, 16)
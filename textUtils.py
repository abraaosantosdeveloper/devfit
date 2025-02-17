import os

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

BOLD_BLACK = '\033[1;30m'
BOLD_RED = '\033[1;31m'
BOLD_GREEN = '\033[1;32m'
BOLD_YELLOW = '\033[1;33m' # orange on some systems
BOLD_BLUE = '\033[1;34m'
BOLD_MAGENTA = '\033[1;35m'
BOLD_CYAN = '\033[1;36m'
BOLD_LIGHT_GRAY = '\033[1;37m'
BOLD_DARK_GRAY = '\033[1;90m'
BOLD_BRIGHT_RED = '\033[1;91m'
BOLD_BRIGHT_GREEN = '\033[1;92m'
BOLD_BRIGHT_YELLOW = '\033[1;93m'
BOLD_BRIGHT_BLUE = '\033[1;94m'
BOLD_BRIGHT_MAGENTA = '\033[1;95m'
BOLD_BRIGHT_CYAN = '\033[1;96m'
BOLD_WHITE = '\033[1;97m'

BACKGROUND_GRAY = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_YELLOW = '\033[43m'
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_MAGENTA = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_LIGHT_GRAY = '\033[47m'
BACKGROUND_DARK_GRAY = '\033[100m'
BACKGROUND_BRIGHT_RED = '\033[101m'
BACKGROUND_BRIGHT_GREEN = '\033[102m'
BACKGROUND_BRIGHT_YELLOW = '\033[103m'
BACKGROUND_BRIGHT_BLUE = '\033[104m'
BACKGROUND_BRIGHT_MAGENTA = '\033[105m'
BACKGROUND_BRIGHT_CYAN = '\033[106m'
BACKGROUND_WHITE = '\033[107m'

RESET = '\033[0m' # called to return to standard terminal text color

# An alternative print function for colored text
# Designed to work almost like the original print function, but with color
def printColored(s:str, color:str = WHITE, end:str="\n")->None: print(color + s + RESET, end=end)

# Print colored text shortcuts
def printBlack(s:str, end:str="\n")->None:				printColored(s,BLACK, end=end)
def printRed(s:str, end:str="\n")->None:				printColored(s,RED, end=end)
def printGreen(s:str, end:str="\n")->None:				printColored(s,GREEN, end=end)
def printYellow(s:str, end:str="\n")->None:				printColored(s,YELLOW, end=end)
def printBlue(s:str, end:str="\n")->None:				printColored(s,BLUE, end=end)
def printMagenta(s:str, end:str="\n")->None:			printColored(s,MAGENTA, end=end)
def printCyan(s:str, end:str="\n")->None:				printColored(s,CYAN, end=end)
def printLightGray(s:str, end:str="\n")->None:			printColored(s,LIGHT_GRAY, end=end)
def printDarkGray(s:str, end:str="\n")->None:			printColored(s,DARK_GRAY, end=end)
def printBrightRed(s:str, end:str="\n")->None:			printColored(s,BRIGHT_RED, end=end)
def printBrightGreen(s:str, end:str="\n")->None:		printColored(s,BRIGHT_GREEN, end=end)
def printBrightYellow(s:str, end:str="\n")->None:		printColored(s,BRIGHT_YELLOW, end=end)
def printBrightBlue(s:str, end:str="\n")->None:			printColored(s,BRIGHT_BLUE, end=end)
def printBrightMagenta(s:str, end:str="\n")->None:		printColored(s,BRIGHT_MAGENTA, end=end)
def printBrightCyan(s:str, end:str="\n")->None:			printColored(s,BRIGHT_CYAN, end=end)

# go to x and y cordinates
# moves the cursor in console...
def gotoxy(x:int,y:int)->None: print ("%c[%d;%df" % (0x1B, y, x), end='')

# trim the string to desired size...
def trim(s:str, size:int)-> str:
	if len(s) <= size: return s
	s2 = s[0:size-1] + '…'
	return s2

# clearScreen...
def clearScreen():
	os.system("cls")

SIMPLE_BORDER_CHARSET = ['┌','└','│','┐','│','┘','─','─']
HEAVY_BORDER_CHARSET = ['┏','┗','┃','┓','┃','┛','━','━']
DOUBLE_BORDER_CHARSET = ['╔','╚','║','╗','║','╝','═','═']
BROAD_BORDER_CHARSET =  ['▛','▙','▌','▜','▐','▟','▀','▄']
ROUND_BORDER_CHARSET =  ['╭','╰','│','╮','│','╯','─','─']

#Function for drawing boxes
#it uses a border charset for draw boxes in console
#suports colors
def drawBox(x, y, w, h, color=WHITE, charSet=SIMPLE_BORDER_CHARSET):
	if (w <= 1) : return
	if (h <=1) : return
	for i in range(x , x + w):
		for j in range(y , y + h):
			gotoxy(i,j)
			print(color,end="")
			if i == x:
				if j == y: print(charSet[0])
				elif j == y+h-1: print(charSet[1])
				else: print(charSet[2])
			elif i == x+w-1:
				if j == y: print(charSet[3])
				elif j < y+h-1: print(charSet[4])
				else: print(charSet[5])
			else:
				if j == y: print(charSet[6])
				elif j == y+h-1: print(charSet[7])
			print(RESET,end="")

# draw box shortcuts
def drawSimpleBorderBox(x,y,w,h, color=WHITE): drawBox(x,y,w,h,color,SIMPLE_BORDER_CHARSET)
def drawHeavyBorderBox(x,y,w,h, color=WHITE): drawBox(x,y,w,h,color,HEAVY_BORDER_CHARSET)
def drawDoubleBorderBox(x,y,w,h, color=WHITE): drawBox(x,y,w,h,color,DOUBLE_BORDER_CHARSET)
def drawBroadBorderBox(x,y,w,h, color=WHITE): drawBox(x,y,w,h,color,BROAD_BORDER_CHARSET)
def drawRoundBorderBox(x,y,w,h, color=WHITE): drawBox(x,y,w,h,color,ROUND_BORDER_CHARSET)

# prints a title bar on the top of console with centered text...
# suport box color and text color
# it assumes the default 120 x 30 windows console

# simple border
def printTitleBar(text:str, boxColor = WHITE, textColor = WHITE):
	x = 60 - (int(len(text)/2))
	drawBox(1,1,120,3,boxColor)
	gotoxy(x,2)
	printColored(text, textColor)

# double border
def printTitleBarDoubleBorder(text:str, boxColor = WHITE, textColor = WHITE):
	x = 60 - (int(len(text)/2))
	drawBox(1,1,120,3,boxColor, DOUBLE_BORDER_CHARSET)
	gotoxy(x,2)
	printColored(text, textColor)

#broad border
def printTitleBarBroadBorder(text:str, boxColor = WHITE, textColor = WHITE):
	x = 60 - (int(len(text)/2))
	drawBox(1,1,120,3,boxColor, BROAD_BORDER_CHARSET)
	gotoxy(x,2)
	printColored(text, textColor)

#heavy border
def printTitleBarHeavyBorder(text:str, boxColor = WHITE, textColor = WHITE):
	x = 60 - (int(len(text)/2))
	drawBox(1,1,120,3,boxColor, HEAVY_BORDER_CHARSET)
	gotoxy(x,2)
	printColored(text, textColor)
	
#round border
def printTitleBarRoundBorder(text:str, boxColor = WHITE, textColor = WHITE):
	x = 60 - (int(len(text)/2))
	drawBox(1,1,120,3,boxColor, ROUND_BORDER_CHARSET)
	gotoxy(x,2)
	printColored(text, textColor)


#prints a progress bar on the selected line
#the bar shows the percentage value from 0% to 100%
#it assumes the default 120 x 30 windows console
def printProgressBar(percentage:float,
	line:int= 27,
	boxColor = WHITE,
	barColor=GREEN,
	textColor = WHITE,
	backgroundTextColor = BACKGROUND_GREEN):

	if line < 0: return
	if line > 27: return
	if percentage < 0: percentage = 0
	if percentage > 100: percentage = 100
	
	drawBox(1,line,120,3,boxColor)
	
	pins = int((percentage / 100) * 118)
	for i in range(pins):
		gotoxy(i+2, line+1)
		printColored("█", barColor)

	text = f"{percentage:.2f}%"
	for j in range(len(text)):
		gotoxy(58+j,line+1)
		if(pins < 58+j): printColored(text[j], textColor)
		else: printColored(text[j], backgroundTextColor+textColor)


# prints a dark gray status bar in the bottom of console with left aligned text...
# suport only text color...
# it assumes the default 120 x 30 windows console
# it also cleans the status bar text area before writing
def printStatusBar(text:str = "", textColor = WHITE):
	gotoxy(1,28); print(" " * 120, end="")
	drawBox(1,27,120,3,DARK_GRAY)
	gotoxy(2,28); printColored(text, textColor, end="")

# info bar shortcuts
def printSuccess(text:str=""):	printStatusBar(f"SUCCESS - {text}", GREEN)
def printInfo(text:str=""):		printStatusBar(f"INFO - {text}", BRIGHT_CYAN)
def printWarning(text:str=""):	printStatusBar(f"WARNING - {text}", YELLOW)
def printError(text:str=""):	printStatusBar(f"ERROR - {text}", RED)

def drawEditField(text:str, line:int, boxColor = WHITE, textColor = WHITE):
	drawBox(1,line,20,3,boxColor)
	drawBox(21,line,100,3,boxColor)
	gotoxy(2,line+1)
	printColored(text,textColor)

def inputxy(x:int, y:int, prompt:str) -> str:
    gotoxy(x,y)
    value = input(prompt)
    return value

def assureInputxy(x:int, y:int, prompt:str) -> str:
    while True:
        gotoxy(x,y)
        value = input(prompt)
        if value != "": return value

def assureInput(prompt:str) -> str:
    while True:
        value = input(prompt)
        if value == "": printError("Invalid Input, Try Again...")
        else: return value

def inputIntxy(x:int, y:int, message:str) -> int:
    while True:
        gotoxy(x,y)
        try: value = int(input(message)); return value
        except: printError("Input data must be an integer number...")

def inputFloatxy(x:int, y:int, message:str) -> float:
    while True:
        gotoxy(x,y)
        try: value = float(input(message)); return value
        except: printError("Input data must be an floating point number...")
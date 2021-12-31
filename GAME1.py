import pygame,sys
pygame.init()
BOARD_WIDTH=600
BOARD_HEIGHT=600
LINE_WIDTH=10
BOARD_COLOR=(150,250,100)
LINE_COLOR=(50,120,55)
BOARD_ROWS=3
BOARD_COLS=3
CIRCLE_RADIUS = 40
CIRCLE_WIDTH = 7
CIRCLE_COLOR=(239,231,200)
RED = (255, 0, 0)
CROSS_WIDTH = 25
SPACE = 55
CROSS_COLOR = (66, 66, 66)
board=np.zeros((BOARD_ROWS,BOARD_COLS))
player=1
#print(board)
def mark_square(row, col, player):
	board[row][col] = player

def available_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for row in range(BOARD_ROWS):

		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False
	return True
def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col  * 200 + 100 ), int( row * 200 + 100 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line(screen,CROSS_COLOR,(col *200 +SPACE,row *200+200-SPACE), (col * 200 + 200-SPACE,row * 200+SPACE ), CROSS_WIDTH )
               pygame.draw.line(screen,CROSS_COLOR,(col *200 +SPACE,row * 200+ SPACE),(col * 200 + 200 - SPACE,row * 200 + 200  - SPACE), CROSS_WIDTH)
def draw_line_4D():
    pygame.draw.line(screen,LINE_COLOR,(70,150),(530,150),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(70,300),(530,300),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(70,450),(530,450),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (150, 80), (150, 520), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (300, 80), (300, 520), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (450, 80), (450, 520), LINE_WIDTH)
def draw_line_3D():
    pygame.draw.line(screen,LINE_COLOR,(50,150),(500,150),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(50,300),(500,300),LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (180, 50), (180, 450), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (360, 50), (360, 450), LINE_WIDTH)
print("*WELCOME TO TIC TAC TOA***")
print("please select the game dimension your want to play ")
dimension=input("A for 3D AND B for 4D")
if dimension=='A':
    screen = pygame.display.set_mode((BOARD_HEIGHT, BOARD_WIDTH))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(BOARD_COLOR)
    draw_line_3D()
elif dimension=='B':
    screen = pygame.display.set_mode((BOARD_HEIGHT, BOARD_WIDTH))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(BOARD_COLOR)
    draw_line_4D()
while(True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pygame.display.update()
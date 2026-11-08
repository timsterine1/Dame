import pygame
import sys

class Block:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.player_color =  None  # "Black", "White" oder None
        self.is_selected = False
        self.can_move = False
        self.have_to_move = False
grid = [[2,0,2,0,2,0,2,0],
        [0,2,0,2,0,2,0,2],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1]]

for ypos in range(len(grid)):
        for xpos in range(len(grid[ypos])):
            block = Block()
            if grid[ypos][xpos] == 1:
                block.player_color = "Black"
            elif grid[ypos][xpos] == 2:
                block.player_color = "White"
            block.xpos = xpos
            block.ypos = ypos
            grid[ypos][xpos] = block
            

pygame.init()
pygame.display.set_caption("Dame")
screen = pygame.display.set_mode((800, 800))
pygame.font.init()

MAIN_FONT_SIZE = 20
MAIN_FONT = pygame.font.SysFont("Arial", MAIN_FONT_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)

FPS = 60
BOARD_SIZE = 8
FIELD_SIZE = screen.get_width() // BOARD_SIZE
LIGHT_FIELD = (240, 217, 181)
DARK_FIELD = (181, 136, 99)


def draw_board(grid):
    for ypos in range(BOARD_SIZE):
        for xpos in range(BOARD_SIZE):
            if (xpos + ypos) % 2 == 0:
                field_color = LIGHT_FIELD
            else:
                field_color = DARK_FIELD
            pygame.draw.rect(screen,field_color,(xpos * FIELD_SIZE, ypos * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE),)

            if grid[ypos][xpos].player_color == "Black":
                color = BLACK
                pygame.draw.circle(screen, color, (xpos * FIELD_SIZE + FIELD_SIZE //2, ypos * FIELD_SIZE + FIELD_SIZE // 2), FIELD_SIZE // 2 - 5)
            elif grid[ypos][xpos].player_color == "White":
                color = WHITE
                pygame.draw.circle(screen, color, (xpos * FIELD_SIZE + FIELD_SIZE //2, ypos * FIELD_SIZE + FIELD_SIZE // 2), FIELD_SIZE // 2 - 5)
                pygame.draw.circle(screen, BLACK, (xpos * FIELD_SIZE + FIELD_SIZE //2, ypos * FIELD_SIZE + FIELD_SIZE // 2), FIELD_SIZE // 2 - 5, 1)

            if grid[ypos][xpos].is_selected:
                pygame.draw.rect(screen, YELLOW , (xpos * FIELD_SIZE, ypos * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE), 5)
            
def get_mouse_pos():
    pos = pygame.mouse.get_pos()
    xpos = pos[0]
    ypos = pos[1]
    return ypos // FIELD_SIZE , xpos //FIELD_SIZE
mouse_was_pressed = False
def check_moves():

    if black_player_turn:
        for ypos in range(BOARD_SIZE):
            for xpos in range(BOARD_SIZE):
                if grid[ypos][xpos].is_selected and grid[ypos][xpos].player_color == "Black":
                    if ypos > 0 and xpos > 0 and grid[ypos - 1][xpos - 1].player_color == None:
                        grid[ypos - 1][xpos - 1].can_move = True
                    if ypos > 0 and xpos < BOARD_SIZE - 1 and grid[ypos - 1][xpos + 1].player_color == None:
                        grid[ypos - 1][xpos + 1].can_move = True
                    #check if the player can move
 
                    #check if the player can jump over an opponent's piece
                    if ypos > 1 and xpos > 1 and grid[ypos - 1][xpos - 1].player_color == "White" and grid[ypos - 2][xpos - 2].player_color == None:
                        grid[ypos][xpos].have_to_move = True
                    if ypos > 1 and xpos < BOARD_SIZE - 2 and grid[ypos - 1][xpos + 1].player_color == "White" and grid[ypos - 2][xpos + 2].player_color == None:
                        grid[ypos][xpos].have_to_move = True
                        
                        
clock = pygame.time.Clock()
game_running = True
black_player_turn = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            sys.exit()


    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # [0] fuer links klick 
        get_mouse_pos()
        if not mouse_was_pressed:
            if grid[get_mouse_pos()[0]][get_mouse_pos()[1]].is_selected == False and grid[get_mouse_pos()[0]][get_mouse_pos()[1]].player_color != None:
                grid[get_mouse_pos()[0]][get_mouse_pos()[1]].is_selected = True # mark the selected field
                for ypos in range(BOARD_SIZE):
                    for xpos in range(BOARD_SIZE):
                        if grid[ypos][xpos].is_selected == True and (ypos != get_mouse_pos()[0] or xpos != get_mouse_pos()[1]): # unmark the other fields
                            grid[ypos][xpos].is_selected = False
                mouse_was_pressed = True
            elif grid[get_mouse_pos()[0]][get_mouse_pos()[1]].is_selected == True:
                grid[get_mouse_pos()[0]][get_mouse_pos()[1]].is_selected = False
                mouse_was_pressed = True
    else:
        mouse_was_pressed = False
       
       
    draw_board(grid)
    check_moves()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
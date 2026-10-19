import pygame
import sys

class Block:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
class Player:
    def __init__(self):
        self.figure_collor = "Blue"
grid = [[1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1]]

for ypos in range(len(grid)):
        for xpos in range(len(grid[ypos])):
            if grid[ypos][xpos] == 1:
                block = Block()
                grid[ypos][xpos] = block
            elif grid[ypos][xpos] == 2:
                block = Block()
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
clock = pygame.time.Clock()
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            sys.exit()

    for ypos in range(BOARD_SIZE):
        for xpos in range(BOARD_SIZE):
            if (xpos + ypos) % 2 == 0:
                field_color = LIGHT_FIELD
            else:
                field_color = DARK_FIELD
            pygame.draw.rect(screen,field_color,(xpos * FIELD_SIZE, ypos * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE),)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
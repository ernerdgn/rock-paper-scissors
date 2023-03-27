import pygame
import random
pygame.init()

# Pixel variables
WIDTH = 750
HEGIHT = 750
IMG_LOCATION_X = 40
IMG_LOCATION_Y = 170
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
LONG_BUTTON_WIDTH = 170
EXIT_BUTTON_LOC_X = 620
EXIT_BUTTON_LOC_Y = 670
ROCK_BUTTON_LOC_X = 30
ROCK_BUTTON_LOC_Y = 100
PAPER_BUTTON_LOC_X = 140
PAPER_BUTTON_LOC_Y = 100
SCISSORS_BUTTON_LOC_X = 250
SCISSORS_BUTTON_LOC_Y = 100
RESULT_LOC_X = 275
RESULT_LOC_Y = 375

# Color variables
BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GRAY = (100,100,100)
LIGHT_GRAY = (180,180,180)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (80,80,255)

# Fonts
font = pygame.font.SysFont("Consolas", 35)
result_font = pygame.font.SysFont("Consolas", 60)

# Texts
rock_text = font.render("Rock", True, WHITE)
paper_text = font.render("Paper", True, WHITE)
scissors_text = font.render("Scissors", True, WHITE)
exit_text = font.render("Exit", True, WHITE)
WIN_text = result_font.render("YOU WON!", True, GREEN)
LOSE_text = result_font.render("YOU LOSE!", True, RED)
DRAW_text = result_font.render("GAME DRAW!", True, BLUE)

# Functions
def random_rps():
    chance = random.randint(0,2)
    if chance == 0:
        return "scissors"
    elif chance == 1:
        return "rock"
    else:
        return "paper"

def check_winner(player, enemy):
    if (player == "rock" and enemy == "scissors") or \
        (player == "paper" and enemy == "rock") or \
        (player == "scissors" and enemy == "paper"):
        return WIN_text
    elif (player == "scissors" and enemy == "rock") or \
        (player == "rock" and enemy == "paper") or \
        (player == "paper" and enemy == "scissors"):
        return LOSE_text
    else:
        return DRAW_text

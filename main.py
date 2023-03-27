import pygame
import sys
import game

pygame.init()

# Set window and display
WIN = pygame.display.set_mode((game.WIDTH, game.HEGIHT))
pygame.display.set_caption("Rock-Paper-Scissors")
WIN.fill(game.BLACK)

# Get images
rock = pygame.image.load("images/rock.png").convert()
paper = pygame.image.load("images/paper.png").convert()
scissors = pygame.image.load("images/scissors.png").convert()
rock_mirrored = pygame.transform.flip(rock, True, False)
paper_mirrored = pygame.transform.flip(paper, True, False)
scissors_mirrored = pygame.transform.flip(scissors, True, False)

element_dict = {
    "paper" : paper_mirrored,
    "rock" : rock_mirrored,
    "scissors" : scissors_mirrored
}

# Buttons
exit_button = pygame.Rect(game.EXIT_BUTTON_LOC_X, game.EXIT_BUTTON_LOC_Y, game.BUTTON_WIDTH, game.BUTTON_HEIGHT)
rock_button = pygame.Rect(game.ROCK_BUTTON_LOC_X, game.ROCK_BUTTON_LOC_Y, game.BUTTON_WIDTH, game.BUTTON_HEIGHT)
paper_button = pygame.Rect(game.PAPER_BUTTON_LOC_X, game.PAPER_BUTTON_LOC_Y, game.BUTTON_WIDTH, game.BUTTON_HEIGHT)
scissors_button = pygame.Rect(game.SCISSORS_BUTTON_LOC_X, game.SCISSORS_BUTTON_LOC_Y, game.LONG_BUTTON_WIDTH, game.BUTTON_HEIGHT)


def main():
    run = True

    clock = pygame.time.Clock()

    while run:
        # Update screen
        #pygame.display.flip()  # paint screen one time
        pygame.display.update()
        clock.tick(60)


        # Get mouse position
        mouse_position = pygame.mouse.get_pos()

        # Printing, drawing and highlighting the button
        # Exit
        if exit_button.x <= mouse_position[0] <= exit_button.x + game.BUTTON_WIDTH and exit_button.y <= mouse_position[1] <= exit_button.y + game.BUTTON_HEIGHT:
            pygame.draw.rect(WIN, game.LIGHT_GRAY, exit_button)
        else:
            pygame.draw.rect(WIN, game.DARK_GRAY, exit_button)
        WIN.blit(game.exit_text, (exit_button.x + 10, exit_button.y + 10))

        # Rock
        if rock_button.x <= mouse_position[0] <= rock_button.x + game.BUTTON_WIDTH and rock_button.y <= mouse_position[1] <= rock_button.y + game.BUTTON_HEIGHT:
            pygame.draw.rect(WIN, game.LIGHT_GRAY, rock_button)
        else:
            pygame.draw.rect(WIN, game.DARK_GRAY, rock_button)
        WIN.blit(game.rock_text, (rock_button.x + 10, rock_button.y + 10))

        # Paper
        if paper_button.x <= mouse_position[0] <= paper_button.x + game.BUTTON_WIDTH and paper_button.y <= mouse_position[1] <= paper_button.y + game.BUTTON_HEIGHT:
            pygame.draw.rect(WIN, game.LIGHT_GRAY, paper_button)
        else:
            pygame.draw.rect(WIN, game.DARK_GRAY, paper_button)
        WIN.blit(game.paper_text, (paper_button.x + 4, paper_button.y + 10))

        # Scissors
        if scissors_button.x <= mouse_position[0] <= scissors_button.x + game.BUTTON_WIDTH and scissors_button.y <= mouse_position[1] <= scissors_button.y + game.BUTTON_HEIGHT:
            pygame.draw.rect(WIN, game.LIGHT_GRAY, scissors_button)
        else:
            pygame.draw.rect(WIN, game.DARK_GRAY, scissors_button)
        WIN.blit(game.scissors_text, (scissors_button.x + 10, scissors_button.y + 10))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    print("shutting down")
                    pygame.quit()
                    sys.exit(0)
                
                if rock_button.collidepoint(event.pos):
                    WIN.blit(rock, (game.IMG_LOCATION_X, game.IMG_LOCATION_Y))
                    player = "rock"
                    enemy = game.random_rps()
                    WIN.blit(element_dict[enemy], (game.IMG_LOCATION_X + 500, game.IMG_LOCATION_Y))
                    pygame.draw.rect(WIN, game.BLACK, (game.RESULT_LOC_X, game.RESULT_LOC_Y, 400, 100))
                    WIN.blit(game.check_winner(player,enemy), (game.RESULT_LOC_X, game.RESULT_LOC_Y))
                
                if paper_button.collidepoint(event.pos):
                    WIN.blit(paper, (game.IMG_LOCATION_X, game.IMG_LOCATION_Y))
                    player = "paper"
                    enemy = game.random_rps()
                    WIN.blit(element_dict[enemy], (game.IMG_LOCATION_X + 500, game.IMG_LOCATION_Y))
                    pygame.draw.rect(WIN, game.BLACK, (game.RESULT_LOC_X, game.RESULT_LOC_Y, 400, 100))
                    WIN.blit(game.check_winner(player,enemy), (game.RESULT_LOC_X, game.RESULT_LOC_Y))
                
                if scissors_button.collidepoint(event.pos):
                    WIN.blit(scissors, (game.IMG_LOCATION_X, game.IMG_LOCATION_Y))
                    player = "scissors"
                    enemy = game.random_rps()
                    WIN.blit(element_dict[enemy], (game.IMG_LOCATION_X + 500, game.IMG_LOCATION_Y))
                    pygame.draw.rect(WIN, game.BLACK, (game.RESULT_LOC_X, game.RESULT_LOC_Y, 400, 100))
                    WIN.blit(game.check_winner(player,enemy), (game.RESULT_LOC_X, game.RESULT_LOC_Y))
    
    if run == False:
        print("shutting down")
        pygame.quit()
        sys.exit(0)

if __name__ == "__main__":
    main()
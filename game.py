import pygame
import random
from functions import *

pygame.init()

# initial set up
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

# game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ''
score = 0
file = open('high_score', 'r')
init_high = int(file.readline())
file.close()
high_score = init_high

# main game loop
run = True
clicking_info = False  

while run:
    try:
        timer.tick(fps)
        screen.fill('gray')
        draw_header(screen, font)
        draw_board(screen, font, score, high_score)
        draw_pieces(screen, font, board_values)
        if spawn_new or init_count < 2:
            board_values, game_over = new_pieces(board_values)
            spawn_new = False
            init_count += 1

        if game_over:
            game_over = check_game_over(board_values)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if click_information(event.pos):
                    clicking_info = True  # Set clicking_info to True when the information icon is clicked

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    clicking_info = False  # Set clicking_info to False when the left mouse button is released

            elif event.type == pygame.KEYUP:
                if game_over:
                    if event.key == pygame.K_RETURN:
                        board_values = [[0 for _ in range(4)] for _ in range(4)]
                        spawn_new = True
                        init_count = 0
                        score = 0
                        direction = ''
                        game_over = False

                elif event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
                else:
                    raise ValueError("Invalid key input")

        if direction:
            board_values, score = take_turn(direction, board_values, score)
            direction = ''
            spawn_new = True

        if game_over:
            draw_over(screen, font)
            if high_score > init_high:
                with open('high_score', 'w') as file:
                    file.write(f'{high_score}')
                    init_high = high_score

        if score > high_score:
            high_score = score

        if clicking_info:  # Draw the information panel if clicking_info is True
            draw_information(screen, font)

        pygame.display.flip()
    
    except Exception as e:
        draw_header(screen, font)
        draw_board(screen, font, score, high_score)
        draw_pieces(screen, font, board_values)
        draw_invalid(screen, font)
        pygame.display.flip()
        pygame.time.wait(2000)
        continue

pygame.quit()
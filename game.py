# game.py
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
while run:
    try:
        timer.tick(fps)
        screen.fill('gray')
        draw_board(screen, font, score, high_score)
        draw_pieces(screen, font, board_values)
        if spawn_new or init_count < 2:
            board_values, game_over = new_pieces(board_values)
            spawn_new = False
            init_count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                # Check if the key corresponds to an arrow key
                if event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
                else:
                    # If not an arrow key, raise an exception
                    raise ValueError("Invalid key input")

                if game_over:
                    if event.key == pygame.K_RETURN:
                        board_values = [[0 for _ in range(4)] for _ in range(4)]
                        spawn_new = True
                        init_count = 0
                        score = 0
                        direction = ''
                        game_over = False

        if direction:
            board_values, score = take_turn(direction, board_values, score)
            direction = ''
            spawn_new = True
        if game_over:
            draw_over(screen, font)
            if high_score > init_high:
                file = open('high_score', 'w')
                file.write(f'{high_score}')
                file.close()
                init_high = high_score

        if score > high_score:
            high_score = score

        pygame.display.flip()
    
    except Exception as e:
        draw_invalid(screen, font)
        pygame.display.flip()
        pygame.time.wait(2000)
        run = False
        print(f"An error occurred: {e}")

pygame.quit()

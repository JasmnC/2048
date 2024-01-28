# functions.py
import pygame
import random

# 2048 game color library
colors = {
    0: (179, 230,230 ), 
    2: (153, 204, 204),  
    4: (102, 204, 204), 
    8: (0, 204, 153),   
    16: (0, 153, 102),  
    32: (102, 255, 204),   
    64: (51, 204, 153),  
    128: (0, 204, 102), 
    256: (0, 153, 51),   
    512: (153, 255, 153), 
    1024: (51, 204, 51), 
    2048: (0, 102, 0), 
    'light text': (0, 102, 102), 
    'dark text': (0, 51, 51),   
    'other': (0, 0, 0),             
    'bg': (204, 238, 238),
    'pop box': (64,64,64) 
}

# draw game over and restart text
def draw_over(screen, font):
    pygame.draw.rect(screen, colors['pop box'], [50, 50, 300, 100], 0, 10)
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text1, (130, 65))
    screen.blit(game_over_text2, (70, 105))


# take your turn based on direction
def take_turn(direc, board, score):
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        board[i - shift - 1][j] *= 2
                        score += board[i - shift - 1][j]
                        board[i - shift][j] = 0
                        merged[i - shift - 1][j] = True

    elif direc == 'DOWN':
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift += 1
                if shift > 0:
                    board[2 - i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                            and not merged[2 - i + shift][j]:
                        board[3 - i + shift][j] *= 2
                        score += board[3 - i + shift][j]
                        board[2 - i + shift][j] = 0
                        merged[3 - i + shift][j] = True

    elif direc == 'LEFT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][j - shift] = board[i][j]
                    board[i][j] = 0
                if board[i][j - shift] == board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                        and not merged[i][j - shift]:
                    board[i][j - shift - 1] *= 2
                    score += board[i][j - shift - 1]
                    board[i][j - shift] = 0
                    merged[i][j - shift - 1] = True

    elif direc == 'RIGHT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board[i][4 - j + shift] == board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                            and not merged[i][3 - j + shift]:
                        board[i][4 - j + shift] *= 2
                        score += board[i][4 - j + shift]
                        board[i][3 - j + shift] = 0
                        merged[i][4 - j + shift] = True
    return board, score


# spawn in new pieces randomly when turns start
def new_pieces(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if board[row][col] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    if count < 1:
        full = True
    return board, full

# draw background for the board
def draw_board(screen, font, score, high_score):
    pygame.draw.rect(screen, colors['bg'], [0, 50, 400, 400], 0, 10)  
    score_text = font.render(f'Score: {score}', True, colors['dark text'])
    high_score_text = font.render(f'High Score: {high_score}', True, colors['dark text'])
    screen.blit(score_text, (10, 460))
    screen.blit(high_score_text, (200, 460)) 

# draw the top bar
def draw_header(screen, font):
    pygame.draw.rect(screen, 'grey', [0, 0, 400, 50])
    info_icon_image = pygame.image.load('info_icon.png')  
    screen.blit(info_icon_image, (400 - 50, 0))

# draw tiles for game
def draw_pieces(screen, font, board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 70, 75, 75], 0, 5)  # Adjust the y-coordinate for the tiles
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 112))  # Adjust the y-coordinate for the text
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, colors['pop box'], [j * 95 + 20, i * 95 + 70, 75, 75], 1, 5)  # Adjust the y-coordinate for the tile border

# draw invalid input to end the game
def draw_invalid(screen, font):
    pygame.draw.rect(screen, colors['pop box'], [50, 50, 300, 100], 0, 10)
    invalid_text1 = font.render('Invalid Input', True, 'white')
    invalid_text2 = font.render('Game Quit', True, 'white')
    screen.blit(invalid_text1, (130, 65))
    screen.blit(invalid_text2, (140, 105))

# check if the game is not over
def check_game_over(board_values):
    all_cells_filled = all(value != 0 for row in board_values for value in row)
    no_valid_moves = not any(board_values[i][j] == board_values[i+1][j] or 
                             board_values[i][j] == board_values[i][j+1]
                             for i in range(len(board_values)-1) 
                             for j in range(len(board_values[0])-1))
    return all_cells_filled and no_valid_moves

# Function to check if the mouse click is on the information icon/button
def click_information(mouse_pos):
    if 400 - 50 <= mouse_pos[0] <= 400 and 0 <= mouse_pos[1] <= 50:
        return True
    return False

# Function to display the instructions panel
def draw_information(screen, font):
    instructions_panel = pygame.Surface((300, 200))  
    instructions_panel.fill(colors['pop box'])
    instructions_text = font.render("Instructions:", True, 'red')
    instructions_panel.blit(instructions_text, (10, 10))
    screen.blit(instructions_panel, (50, 100))

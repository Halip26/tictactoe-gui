import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

window_size = (450, 500)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe Game")

# Initialize variables
table_size = window_size[0]
cell_size = table_size // 3
table_space = 20

player = "X"
winner = None
taking_move = True
running = True
table = [["-" for _ in range(3)] for _ in range(3)]

background_color = (143, 235, 52)
table_color = (50, 50, 50)
line_color = (252, 186, 3)
instructions_color = (17, 53, 165)
game_over_bg_color = (47, 98, 162)
game_over_color = (255, 179, 1)
font = pygame.font.SysFont("Courier New", 35)
FPS = pygame.time.Clock()


def draw_table():
    tb_space_point = (table_space, table_size - table_space)
    cell_space_point = (cell_size, cell_size * 2)
    pygame.draw.line(
        screen,
        table_color,
        [tb_space_point[0], cell_space_point[0]],
        [tb_space_point[1], cell_space_point[0]],
        8,
    )
    pygame.draw.line(
        screen,
        table_color,
        [cell_space_point[0], tb_space_point[0]],
        [cell_space_point[0], tb_space_point[1]],
        8,
    )
    pygame.draw.line(
        screen,
        table_color,
        [tb_space_point[0], cell_space_point[1]],
        [tb_space_point[1], cell_space_point[1]],
        8,
    )
    pygame.draw.line(
        screen,
        table_color,
        [cell_space_point[1], tb_space_point[0]],
        [cell_space_point[1], tb_space_point[1]],
        8,
    )


def change_player():
    global player
    player = "O" if player == "X" else "X"


def move(pos):
    global table, winner, taking_move
    try:
        x, y = pos[0] // cell_size, pos[1] // cell_size
        if table[x][y] == "-":
            table[x][y] = player
            draw_char(x, y, player)
            game_check()
            change_player()
    except:
        print("Only click inside the table!")


def draw_char(verti, horiz, user):
    if user== "O":
        img = pygame.image.load("assets/O.png")
    elif user == "X":
        img = pygame.image.load("assets/X.png")
    img = pygame.transform.scale(img, (cell_size, cell_size))
    screen.blit(
        img,
        (verti * cell_size, horiz * cell_size, cell_size, cell_size),
    )


def message():
    global winner, taking_move
    if winner is not None:
        screen.fill(game_over_bg_color, (130, 445, 193, 35))
        msg = font.render(f"{winner} WIN!!", True, game_over_color)
        screen.blit(msg, (144, 445))
    elif not taking_move:
        screen.fill(game_over_bg_color, (130, 445, 193, 35))
        instructions = font.render("TIE!!", True, game_over_color)
        screen.blit(instructions, (165, 445))
    else:
        screen.fill(background_color, (135, 445, 188, 35))
        instructions = font.render(f"{player} to move", True, instructions_color)
        screen.blit(instructions, (135, 445))


def game_check():
    global winner, taking_move

    # Check vertical
    for x_index, col in enumerate(table):
        win = True
        pattern_list = []
        for y_index, content in enumerate(col):
            if content != player:
                win = False
                break
            else:
                pattern_list.append((x_index, y_index))
        if win:
            pattern_strike(pattern_list[0], pattern_list[-1], "ver")
            winner = player
            taking_move = False
            break

    # Check horizontal
    for row in range(len(table)):
        win = True
        pattern_list = []
        for col in range(len(table)):
            if table[col][row] != player:
                win = False
                break
            else:
                pattern_list.append((col, row))
        if win:
            pattern_strike(pattern_list[0], pattern_list[-1], "hor")
            winner = player
            taking_move = False
            break

    # Check left diagonal
    if all(table[i][i] == player for i in range(3)):
        pattern_strike((0, 0), (2, 2), "left-diag")
        winner = player
        taking_move = False

    # Check right diagonal
    if all(table[2 - i][i] == player for i in range(3)):
        pattern_strike((2, 0), (0, 2), "right-diag")
        winner = player
        taking_move = False

    # Check for draw
    if all(cell != "-" for row in table for cell in row):
        taking_move = False


def pattern_strike(start_point, end_point, line_type):
    mid_val = cell_size // 2

    if line_type == "ver":
        start_x, start_y = (
            start_point[0] * cell_size + mid_val,
            table_space,
        )
        end_x, end_y = (
            end_point[0] * cell_size + mid_val,
            table_size - table_space,
        )

    elif line_type == "hor":
        start_x, start_y = (
            table_space,
            start_point[-1] * cell_size + mid_val,
        )
        end_x, end_y = (
            table_size - table_space,
            end_point[-1] * cell_size + mid_val,
        )

    elif line_type == "left-diag":
        start_x, start_y = table_space, table_space
        end_x, end_y = (
            table_size - table_space,
            table_size - table_space,
        )

    elif line_type == "right-diag":
        start_x, start_y = table_size - table_space, table_space
        end_x, end_y = table_space, table_size - table_space

    pygame.draw.line(screen, line_color, [start_x, start_y], [end_x, end_y], 8)


# Main loop
def main():
    global running
    screen.fill(background_color)
    draw_table()
    while running:
        message()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if taking_move:
                    move(event.pos)

        pygame.display.flip()
        FPS.tick(60)


if __name__ == "__main__":
    main()

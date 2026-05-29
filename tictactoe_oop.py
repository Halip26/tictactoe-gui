import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

window_size = (450, 500)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe Game")


# Classes are used to represent certain objects or entities.
class TicTacToe:
    def __init__(self, table_size):
        self.table_size = table_size
        self.cell_size = table_size // 3
        self.table_space = 20

        self.player = random.choice(["X", "O"])
        self.winner = None
        self.taking_move = True
        self.running = True
        self.table = []
        for col in range(3):
            self.table.append([])
            for row in range(3):
                self.table[col].append("-")

        self.background_color = (143, 235, 52)
        self.table_color = (50, 50, 50)
        self.line_color = (252, 186, 3)
        self.instructions_color = (17, 53, 165)
        self.game_over_bg_color = (47, 98, 162)
        self.game_over_color = (255, 179, 1)
        self.font = pygame.font.SysFont("Courier New", 35)
        self.FPS = pygame.time.Clock()

        # pre-load images to avoid "libpng warning" spam and improve performance
        self.X_IMG = pygame.image.load("assets/X.png")
        self.O_IMG = pygame.image.load("assets/O.png")

        # to avoid this "libpng warning: iCCP: known incorrect sRGB profile"

    # draw a tabular representation
    def draw_table(self):
        tb_space_point = (self.table_space, self.table_size - self.table_space)
        cell_space_point = (self.cell_size, self.cell_size * 2)
        r1 = pygame.draw.line(
            screen,
            self.table_color,
            [tb_space_point[0], cell_space_point[0]],
            [tb_space_point[1], cell_space_point[0]],
            8,
        )
        c1 = pygame.draw.line(
            screen,
            self.table_color,
            [cell_space_point[0], tb_space_point[0]],
            [cell_space_point[0], tb_space_point[1]],
            8,
        )
        r2 = pygame.draw.line(
            screen,
            self.table_color,
            [tb_space_point[0], cell_space_point[1]],
            [tb_space_point[1], cell_space_point[1]],
            8,
        )
        c2 = pygame.draw.line(
            screen,
            self.table_color,
            [cell_space_point[1], tb_space_point[0]],
            [cell_space_point[1], tb_space_point[1]],
            8,
        )

    # to process substitutions
    def change_player(self):
        self.player = "O" if self.player == "X" else "X"

    # process clicks to move
    def move(self, pos):
        try:
            x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
            if self.table[x][y] == "-":
                self.table[x][y] = self.player
                self.draw_char(x, y, self.player)
                self.game_check()
                self.change_player()
        except:
            print("Only click inside the table!")

    # draws the last player character to the selected table cell
    def draw_char(self, x, y, player):
        if self.player == "O":
            img = self.O_IMG
        elif self.player == "X":
            img = self.X_IMG
        img = pygame.transform.scale(img, (self.cell_size, self.cell_size))
        screen.blit(
            img,
            (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size),
        )

    # instructions and game status messages
    def message(self):
        if self.winner is not None:
            # Conditions if there is a winner
            screen.fill(self.game_over_bg_color, (130, 445, 193, 35))
            msg = self.font.render(f"{self.winner} WIN!!", True, self.game_over_color)
            screen.blit(msg, (144, 445))
        elif not self.taking_move:
            # Conditions if the game ends without a winner (draw)
            screen.fill(self.game_over_bg_color, (130, 445, 193, 35))
            instructions = self.font.render("TIE!!", True, self.game_over_color)
            screen.blit(instructions, (165, 445))
        else:
            # Conditions if the game is still in progress and the player must make a move
            screen.fill(self.background_color, (135, 445, 188, 35))
            instructions = self.font.render(
                f"{self.player} to move", True, self.instructions_color
            )
            screen.blit(instructions, (135, 445))

    def game_check(self):
        # vertical check
        for x_index, col in enumerate(self.table):
            win = True
            pattern_list = []
            for y_index, content in enumerate(col):
                if content != self.player:
                    win = False
                    break
                else:
                    pattern_list.append((x_index, y_index))
            if win == True:
                self.pattern_strike(pattern_list[0], pattern_list[-1], "ver")
                self.winner = self.player
                self.taking_move = False
                break

        # horizontal check
        for row in range(len(self.table)):
            win = True
            pattern_list = []
            for col in range(len(self.table)):
                if self.table[col][row] != self.player:
                    win = False
                    break
                else:
                    pattern_list.append((col, row))
            if win == True:
                self.pattern_strike(pattern_list[0], pattern_list[-1], "hor")
                self.winner = self.player
                self.taking_move = False
                break

        # left diagonal examination
        for index, row in enumerate(self.table):
            win = True
            if row[index] != self.player:
                win = False
                break
        if win == True:
            self.pattern_strike((0, 0), (2, 2), "left-diag")
            self.winner = self.player
            self.taking_move = False

        # right diagonal examination
        for index, row in enumerate(self.table[::-1]):
            win = True
            if row[index] != self.player:
                win = False
                break
        if win == True:
            self.pattern_strike((2, 0), (0, 2), "right-diag")
            self.winner = self.player
            self.taking_move = False

        # blank table cells check to draw
        blank_cells = 0
        for row in self.table:
            for cell in row:
                if cell == "-":
                    blank_cells += 1
        if blank_cells == 0:
            self.taking_move = False

    # draw a line to the winning pattern if it already exists
    def pattern_strike(self, start_point, end_point, line_type):
        # gets the middle value of the cell
        mid_val = self.cell_size // 2

        # lines for vertical winning patterns
        if line_type == "ver":
            start_x, start_y = (
                start_point[0] * self.cell_size + mid_val,
                self.table_space,
            )
            end_x, end_y = (
                end_point[0] * self.cell_size + mid_val,
                self.table_size - self.table_space,
            )

        # lines for horizontal winning patterns
        elif line_type == "hor":
            start_x, start_y = (
                self.table_space,
                start_point[-1] * self.cell_size + mid_val,
            )
            end_x, end_y = (
                self.table_size - self.table_space,
                end_point[-1] * self.cell_size + mid_val,
            )

        # lines for diagonal winning patterns from top left to bottom right
        elif line_type == "left-diag":
            start_x, start_y = self.table_space, self.table_space
            end_x, end_y = (
                self.table_size - self.table_space,
                self.table_size - self.table_space,
            )

        # lines for diagonal winning patterns from top right to bottom left
        elif line_type == "right-diag":
            start_x, start_y = self.table_size - self.table_space, self.table_space
            end_x, end_y = self.table_space, self.table_size - self.table_space

        # Variables to draw the line
        pygame.draw.line(screen, self.line_color, [start_x, start_y], [end_x, end_y], 8)

    def restart_game(self):
        self.table = [["-" for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.taking_move = True
        self.player = random.choice(["X", "O"])
        screen.fill(self.background_color)
        self.draw_table()

    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((window_size[0], window_size[1]), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))  # Black with alpha
        screen.blit(overlay, (0, 0))

        # Use pre-loaded images
        if self.winner == "O":
            img = self.O_IMG
        elif self.winner == "X":
            img = self.X_IMG
        else:  # Draw
            img = None

        if img:
            img = pygame.transform.scale(img, (150, 150))
            screen.blit(img, (window_size[0] // 2 - 75, 100))
            msg_text = f"{self.winner} WIN!!"
        else:
            msg_text = "TIE!!"

        # Render Winner Text
        big_font = pygame.font.SysFont("Courier New", 50, bold=True)
        msg = big_font.render(msg_text, True, self.game_over_color)
        msg_rect = msg.get_rect(center=(window_size[0] // 2, 280))
        screen.blit(msg, msg_rect)

        # Render Options
        small_font = pygame.font.SysFont("Courier New", 20, bold=True)
        play_again_msg = small_font.render(
            "Press SPACE to Play Again", True, (255, 255, 255)
        )
        quit_msg = small_font.render("Press ESC to Quit", True, (255, 255, 255))

        screen.blit(
            play_again_msg, play_again_msg.get_rect(center=(window_size[0] // 2, 380))
        )
        screen.blit(quit_msg, quit_msg.get_rect(center=(window_size[0] // 2, 420)))

    def main(self):
        screen.fill(self.background_color)
        self.draw_table()
        while self.running:
            if self.taking_move:
                self.message()

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.taking_move:
                        self.move(self.event.pos)

                if self.event.type == pygame.KEYDOWN:
                    if not self.taking_move:
                        if self.event.key == pygame.K_SPACE:
                            self.restart_game()
                        if self.event.key == pygame.K_ESCAPE:
                            self.running = False

            if not self.taking_move:
                self.draw_game_over()

            pygame.display.flip()
            self.FPS.tick(60)


# for implementation of a TicTacToe game
if __name__ == "__main__":
    g = TicTacToe(window_size[0])
    g.main()

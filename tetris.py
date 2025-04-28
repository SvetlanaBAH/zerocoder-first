import pygame
import random

# Константы
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
BOARD_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Цвета
COLORS = [
    (0, 0, 0),  # Черный
    (255, 0, 0),  # Красный
    (0, 255, 0),  # Зеленый
    (0, 0, 255),  # Синий
    (255, 255, 0),  # Желтый
    (0, 255, 255),  # Циан
    (255, 0, 255),  # Магента
]

# Фигуры Тетриса
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
]


class Tetris:
    def __init__(self):
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = self.new_piece()
        self.current_x = BOARD_WIDTH // 2 - 1
        self.current_y = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        return [[1 if cell else 0 for cell in row] for row in shape]

    def rotate_piece(self):
        self.current_piece = [list(row) for row in zip(*self.current_piece[::-1])]

    def valid_move(self, dx, dy):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_x + x + dx
                    new_y = self.current_y + y + dy
                    if new_x < 0 or new_x >= BOARD_WIDTH or new_y >= BOARD_HEIGHT:
                        return False
                    if new_y >= 0 and self.board[new_y][new_x]:
                        return False
        return True

    def merge_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + y][self.current_x + x] = cell

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])

    def drop(self):
        if self.valid_move(0, 1):
            self.current_y += 1
        else:
            self.merge_piece()
            self.clear_lines()
            self.current_piece = self.new_piece()
            self.current_x = BOARD_WIDTH // 2 - 1
            self.current_y = 0

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.tetris = Tetris()

    def draw_board(self):
        self.screen.fill(COLORS[0])
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.tetris.board[y][x]:
                    pygame.draw.rect(self.screen, COLORS[self.tetris.board[y][x]],
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        for y, row in enumerate(self.tetris.current_piece):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[1],
                                     ((self.tetris.current_x + x) * BLOCK_SIZE,
                                      (self.tetris.current_y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.tetris.valid_move(-1, 0):
                        self.tetris.current_x -= 1
                    if event.key == pygame.K_RIGHT and self.tetris.valid_move(1, 0):
                        self.tetris.current_x += 1
                    if event.key == pygame.K_DOWN:
                        self.tetris.drop()
                    if event.key == pygame.K_UP:
                        self.tetris.rotate_piece()
                        if not self.tetris.valid_move(0, 0):
                            self.tetris.rotate_piece()  # Вернуть обратно, если невалидно

            self.tetris.drop()
            self.draw_board()

        pygame.quit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
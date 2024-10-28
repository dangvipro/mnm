import pygame
import tkinter as tk
from tkinter import messagebox

# Khởi tạo các thông số cơ bản
CELL_SIZE = 20
GRID_SIZE = 30
WIN_CONDITION = 5
WINDOW_SIZE = CELL_SIZE * GRID_SIZE

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Khởi tạo pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Game XO 30x30 - 5 ô thắng")

# Tạo bảng để lưu trữ trạng thái của từng ô
grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = "X"


def check_winner(x, y):
  def count_direction(dx, dy):
    count = 0
    i, j = x, y
    while 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE and grid[i][j] == current_player:
      count += 1
      i += dx
      j += dy
    return count

  directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
  for dx, dy in directions:
    if count_direction(dx, dy) + count_direction(-dx, -dy) - 1 >= WIN_CONDITION:
      return True
  return False


def draw_board():
  screen.fill(WHITE)
  for x in range(0, WINDOW_SIZE, CELL_SIZE):
    pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_SIZE))
  for y in range(0, WINDOW_SIZE, CELL_SIZE):
    pygame.draw.line(screen, BLACK, (0, y), (WINDOW_SIZE, y))

  for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
      if grid[i][j] == "X":
        pygame.draw.line(screen, RED, (j * CELL_SIZE, i * CELL_SIZE), ((j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE), 2)
        pygame.draw.line(screen, RED, ((j + 1) * CELL_SIZE, i * CELL_SIZE), (j * CELL_SIZE, (i + 1) * CELL_SIZE), 2)
      elif grid[i][j] == "O":
        pygame.draw.circle(screen, BLUE, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 2, 2)


# Khởi tạo vòng lặp chính
running = True
while running:
  draw_board()
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x, y = event.pos
      row = y // CELL_SIZE
      col = x // CELL_SIZE
      if grid[row][col] is None:
        grid[row][col] = current_player
        if check_winner(row, col):
          pygame.display.flip()
          tk.Tk().wm_withdraw()
          messagebox.showinfo("Kết thúc", f"Người chơi {current_player} thắng!")
          running = False
        current_player = "O" if current_player == "X" else "X"

pygame.quit()

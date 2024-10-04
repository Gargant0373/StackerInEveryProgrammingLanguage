import pygame
from model.point import Point

def draw_point(screen, point, color, grid_size):
    outer_rect = pygame.Rect(point.x * grid_size, point.y * grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, (50, 50, 50), outer_rect)

    inner_rect = pygame.Rect(
        point.x * grid_size + 2, 
        point.y * grid_size + 2, 
        grid_size - 4, 
        grid_size - 4
    )
    pygame.draw.rect(screen, color, inner_rect)

def draw_board_grid(screen, board_width, board_height, grid_size):
    for x in range(board_width):
        for y in range(board_height):
            rect = pygame.Rect(x * grid_size, y * grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

def draw_board(screen, board, grid_size):
    draw_board_grid(screen, board.width, board.height, grid_size)
    for y, row in enumerate(board.grid):
        for x, cell in enumerate(row):
            if cell:
                draw_point(screen, Point(x, y), cell, grid_size)

def draw_tetromino(screen, tetromino, grid_size):
    for point in tetromino.get_absolute_positions():
        draw_point(screen, point, tetromino.color, grid_size)

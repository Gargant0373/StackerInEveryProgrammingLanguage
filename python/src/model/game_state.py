from model.board import Board
from model.tetromino_shapes import TTetromino, ITetromino, OTetromino, LTetromino, JTetromino, STetromino, ZTetromino
from model.point import Point
import pygame
import random

class GameState:
    def __init__(self, board_width=10, board_height=20):
        self.board = Board(board_width, board_height)
        self.current_tetromino = self.get_random_tetromino()
        self.current_tetromino.anchor = Point(self.board.width // 2, 0)
        self.is_game_over = False
        self.score = 0

    def get_random_tetromino(self):
        shapes = [ITetromino, OTetromino, TTetromino, LTetromino, JTetromino, STetromino, ZTetromino]
        return random.choice(shapes)()

    def move_tetromino(self, direction):
        previous_anchor = self.current_tetromino.anchor
        self.current_tetromino.move(direction)
        if self.board.is_collision(self.current_tetromino):
            self.current_tetromino.undo_move(previous_anchor)
            if direction == Point(0, 1):
                self.board.place_tetromino(self.current_tetromino)
                self.clear_and_reset()

    def hard_drop(self, screen, draw_func, grid_size):
        while not self.board.is_collision(self.current_tetromino):
            self.current_tetromino.move(Point(0, 1))
            if self.board.is_collision(self.current_tetromino):
                self.current_tetromino.move(Point(0, -1))
                break
            screen.fill((0, 0, 0))
            draw_func(screen, self)
            pygame.display.flip()
            pygame.time.wait(30)
        self.board.place_tetromino(self.current_tetromino)
        self.clear_and_reset()

    def rotate_tetromino(self):
        previous_points = self.current_tetromino.points[:]
        self.current_tetromino.rotate()
        if self.board.is_collision(self.current_tetromino):
            self.current_tetromino.undo_rotate(previous_points)

    def clear_and_reset(self):
        rows_cleared = self.board.clear_full_rows()
        self.update_score(rows_cleared)
        self.current_tetromino = self.get_random_tetromino()
        self.current_tetromino.anchor = Point(self.board.width // 2, 0)
        if self.board.is_collision(self.current_tetromino):
            self.is_game_over = True

    def update_score(self, rows_cleared):
        if rows_cleared > 0:
            self.score += (2 * rows_cleared) ** 2

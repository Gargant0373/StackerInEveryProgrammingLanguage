from model.point import Point

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def is_within_bounds(self, point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def is_cell_empty(self, point):
        return self.is_within_bounds(point) and self.grid[point.y][point.x] is None

    def place_tetromino(self, tetromino):
        for point in tetromino.get_absolute_positions():
            if self.is_within_bounds(point):
                self.grid[point.y][point.x] = tetromino.color

    def clear_full_rows(self):
        full_rows = [row for row in self.grid if all(cell is not None for cell in row)]
        rows_cleared = len(full_rows)
        self.grid = [row for row in self.grid if any(cell is None for cell in row)]
        new_rows = [[None for _ in range(self.width)] for _ in range(rows_cleared)]
        self.grid = new_rows + self.grid
        return rows_cleared

    def is_collision(self, tetromino):
        for point in tetromino.get_absolute_positions():
            if not self.is_within_bounds(point) or not self.is_cell_empty(point):
                return True
        return False

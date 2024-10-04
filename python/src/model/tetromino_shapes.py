from model.tetromino import Tetromino
from model.point import Point

class ITetromino(Tetromino):
    def __init__(self):
        points = [Point(0, -1), Point(0, 0), Point(0, 1), Point(0, 2)]
        super().__init__(points)

class OTetromino(Tetromino):
    def __init__(self):
        points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]
        super().__init__(points)

class TTetromino(Tetromino):
    def __init__(self):
        points = [Point(0, 0), Point(-1, 0), Point(1, 0), Point(0, 1)]
        super().__init__(points)

class LTetromino(Tetromino):
    def __init__(self):
        points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(0, 2)]
        super().__init__(points)

class JTetromino(Tetromino):
    def __init__(self):
        points = [Point(0, 0), Point(-1, 0), Point(0, 1), Point(0, 2)]
        super().__init__(points)

class STetromino(Tetromino):
    def __init__(self):
        points = [Point(0, 0), Point(-1, 0), Point(0, 1), Point(1, 1)]
        super().__init__(points)

class ZTetromino(Tetromino):
    def __init__(self):
        points = [Point(0, 0), Point(1, 0), Point(0, 1), Point(-1, 1)]
        super().__init__(points)

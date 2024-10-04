import random
from model.point import Point

class Tetromino:
    def __init__(self, points, anchor=Point(0, 0), color=(255, 255, 255)):
        colors = [(255, 255, 255), (0, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 0), (255, 165, 0), (0, 0, 255)]
        self.points = points
        self.anchor = anchor
        self.color = random.choice(colors)

    def get_absolute_positions(self):
        return [self.anchor.add(point) for point in self.points]

    def move(self, direction):
        self.anchor = Point(self.anchor.x + direction.x, self.anchor.y + direction.y)

    def rotate(self):
        self.points = [Point(-p.y, p.x) for p in self.points]

    def undo_move(self, previous_anchor):
        self.anchor = previous_anchor

    def undo_rotate(self, previous_points):
        self.points = previous_points

    def __repr__(self):
        return f"Tetromino({self.points}, anchor={self.anchor}, color={self.color})"

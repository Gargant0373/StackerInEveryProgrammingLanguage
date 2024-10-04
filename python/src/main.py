import pygame
from game import Game

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def main():
    game = Game(screen, GRID_SIZE, clock)
    game.run()

if __name__ == "__main__":
    main()

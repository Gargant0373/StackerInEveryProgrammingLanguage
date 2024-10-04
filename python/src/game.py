import pygame
from model.point import Point
from model.game_state import GameState
from draw import draw_board, draw_tetromino, draw_board_grid

class Game:
    def __init__(self, screen, grid_size, clock):
        self.screen = screen
        self.grid_size = grid_size
        self.clock = clock
        self.game_state = GameState()
        self.running = True
        self.drop_interval = 500
        self.last_drop_time = pygame.time.get_ticks()
        self.font = pygame.font.SysFont('Arial', 24)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game_state.move_tetromino(Point(-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.game_state.move_tetromino(Point(1, 0))
                elif event.key == pygame.K_DOWN:
                    self.game_state.move_tetromino(Point(0, 1))
                elif event.key == pygame.K_UP:
                    self.game_state.rotate_tetromino()
                elif event.key == pygame.K_SPACE:
                    self.game_state.hard_drop()

    def automatic_drop(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_drop_time > self.drop_interval:
            previous_anchor = self.game_state.current_tetromino.anchor
            self.game_state.move_tetromino(Point(0, 1)) 
            if self.game_state.current_tetromino.anchor == previous_anchor:
                self.game_state.board.place_tetromino(self.game_state.current_tetromino)
                self.spawn_new_tetromino()
            self.last_drop_time = current_time

    def spawn_new_tetromino(self):
        self.game_state.clear_and_reset()
        if self.game_state.is_game_over:
            self.running = False

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.handle_events()
            draw_board(self.screen, self.game_state.board, self.grid_size)
            draw_board_grid(self.screen, self.game_state.board.width, self.game_state.board.height, self.grid_size)
            draw_tetromino(self.screen, self.game_state.current_tetromino, self.grid_size)
            self.render_score()
            self.automatic_drop()
            pygame.display.flip()
            self.clock.tick(60)
            
    def render_score(self):
        score_text = f"Score: {self.game_state.score}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))

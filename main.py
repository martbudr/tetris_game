import pygame

from settings import Settings
from tetris_game import Tetris
from start_window import StartWindow
from game_over_window import GameOverWindow
from quit_window import QuitWindow

class GameRun:
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Tetris Game")
    
    self.tet_game = Tetris(self)
    self.sw = StartWindow(self)
    self.go = GameOverWindow(self)
    self.quit = QuitWindow(self)
    
    self.game_exists = False
    self.game_over = False
    self.game_quit = False
    self.game_running = False
    
    self.FPS = 60

  def game_loop(self):
    '''Triggers appropriate windows depending on the state of the game'''
    while True:
      self._upgrade_window()
        
      self.clock.tick(self.FPS)
      
  def _upgrade_window(self):
    self.screen.fill(self.settings.bg_color)
    
    self._show_windows()
    
    pygame.display.flip()
    
  def _show_windows(self):
    '''Displays appropriate windows'''
    if not self.game_exists:
      self.sw.show_window()
    elif self.game_running:
      self.tet_game.run_game()
    elif self.game_over:
      self.go.show_window()
    elif self.game_quit:
      self.quit.show_window()
      
if __name__ == "__main__":
  game = GameRun()
  game.game_loop()
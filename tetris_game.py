import pygame
import sys
from time import sleep

from settings import Settings
from board import Board
from tetromino import Tetromino

class Tetris:
  def __init__(self):
    '''Initialisation of the game'''
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Tetris Game")
    
    self.board = Board(self)
    
    self.tile_falling = False # a variable to check if there is a generated tetromino falling at the moment (so that if there isn't, a new one can be generated)
  
  def run_game(self):
    '''Game loop'''
    time_elapsed_since_last_movedown = 0
    FPS = 60
    while True:
      self._check_events()
      
      if not self.tile_falling:
        self.tetromino = Tetromino(self)
        self.tile_falling = True
      
      if time_elapsed_since_last_movedown > 3000 and not self.tetromino.collided_down:
        self.tetromino.move_down()
        time_elapsed_since_last_movedown = 0
      
      self._upgrade_screen()
      
      self.clock.tick(FPS)
      time_elapsed_since_last_movedown += FPS
  
  def _check_events(self):
    '''Checks for user input'''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
        
  def _check_keydown_events(self, event):
    '''Checks keydown events and triggers appropriate responses'''
    if event.key == pygame.K_q: 
      sys.exit()
    elif event.key == pygame.K_LEFT:
      self.tetromino.move_left()
    elif event.key == pygame.K_RIGHT:
      self.tetromino.move_right()
    elif event.key == pygame.K_SPACE:
      self.tetromino.move_all_way_down()
  
  def _upgrade_screen(self):
    '''Draws items on screen on every iteration of the game loop'''
    self.screen.fill(self.settings.bg_color)
    
    self.board.draw()
    self.tetromino.draw()
    
    pygame.display.flip()
  
if __name__ == "__main__":
  tetris = Tetris()
  tetris.run_game()
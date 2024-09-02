import pygame
import sys

from window import Window
from button import Button
from tetris_game import Tetris

class StartWindow(Window):
  '''Handles the start menu window'''
  def __init__(self, game_run):
    super().__init__(game_run)
    self.start_button = Button(game_run, "START")
    
  def show_window(self):
    '''Displays window on the screen - overwrites Window method'''
    self._check_events()
    self._upgrade_screen()
    
  def _check_events(self):
    '''Checks for events'''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.exit_game()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          self.exit_game()
        elif event.key == pygame.K_SPACE:
          self._create_new_game()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_click_on_buttons(mouse_pos)
      
    
  def _check_click_on_buttons(self, mouse_pos):
    '''Checks if some button has been clicked on and triggers appropriate reactions'''
    if self.start_button.rect.collidepoint(mouse_pos):
      self._create_new_game()
        
  def _create_new_game(self):
    '''Creates new game'''
    self.game_run.tet_game = Tetris(self.game_run)
    self.game_run.game_exists = True
    self.game_run.game_running = True
    
  def _upgrade_screen(self):
    '''Upgrades screen'''  
    self.start_button.draw()
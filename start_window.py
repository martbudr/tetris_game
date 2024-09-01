import pygame
import sys

from button import Button
from tetris_game import Tetris

class StartWindow:
  '''Handles the start menu window'''
  def __init__(self, game_run):
    self.game_run = game_run
    self.screen = game_run.screen
    self.settings = game_run.settings
    self.start_button = Button(game_run, "START")
  
  def show_window(self):
    self._check_events()
    
    self._upgrade_screen()
    
  def _check_events(self):
    '''Checks for events'''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_click_on_buttons(mouse_pos)
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          sys.exit()
    
  def _check_click_on_buttons(self, mouse_pos):
    '''Checks if some button has been clicked on and triggers appropriate reactions'''
    if self.start_button.rect.collidepoint(mouse_pos):
      self._init_game()
      self.game_run.game_exists = True
      self.game_run.game_running = True
        
  def _init_game(self):
    self.game_run.tet_game = Tetris(self.game_run)  
    
  def _upgrade_screen(self):
    '''Upgrades screen'''  
    self._draw_menu()
    
  def _draw_menu(self):
    '''Draws the start menu'''
    self.start_button.draw()
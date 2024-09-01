import pygame
import sys

from button import Button

class GameOverWindow:
  '''Handles game over screen'''
  def __init__(self, game_run):
    self.game_run = game_run
    self.screen = game_run.screen
    self.settings = game_run.settings
    self.continue_button = Button(game_run, "Continue")
  
  def show_window(self):
    self._check_events()
    self._upgrade_screen()
  
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_button_click(mouse_pos)
        
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          sys.exit()
  
  def _check_button_click(self, mouse_pos):
    '''Checks if button is clicked on'''
    if self.continue_button.rect.collidepoint(mouse_pos):
      self.game_run.game_exists = False
      self.game_run.game_over = False
  
  def _upgrade_screen(self):
    '''Display game over screen'''
    self.game_run.tet_game.show_window()
    
    message_window = pygame.Rect(0, 0, 200, 200)
    message_window.center = self.screen.get_rect().center
    pygame.draw.rect(self.screen, self.settings.message_bg_color, message_window)
    
    self.continue_button.draw()
import pygame
import sys

from button import Button

class QuitWindow:
  def __init__(self, game_run):
    self.game_run = game_run
    self.screen = game_run.screen
    self.settings = game_run.settings
    self.width, self.height = 300, 200
    self.margin_inline = 30
    self.margin_hor = 30
    
    self.text = "Do you want to quit this game?"
    
    self._prep_window()
    
  def _prep_window(self):
    self.message_window = pygame.Rect(0, 0, 400, 200)
    self.message_window.center = self.screen.get_rect().center
    
    
    button_offset_top = 100
    self.yes_button = Button(self.game_run, "Yes", False, 
                             (self.message_window.left + self.margin_inline, self.message_window.top + button_offset_top), width=50)
    self.no_button = Button(self.game_run, "No", False, 
                            (self.message_window.right - self.margin_inline - self.width, self.message_window.top + button_offset_top), width=50)
    
  def show_window(self):
    self._check_events()
    self.game_run.tet_game.show_window()
    self._upgrade_screen()
    
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          sys.exit()
    
  def _upgrade_screen(self):
    '''Shows quit (pause) window on the screen'''
    pygame.draw.rect(self.screen, self.settings.message_bg_color, self.message_window)
    
    self.yes_button.draw()
    self.no_button.draw()
import pygame
import sys

from window import Window
from button import Button

class QuitWindow(Window):
  def __init__(self, game_run):
    super().__init__(game_run)
    
    self.width, self.height = 400, 200
    self.margin_inline = 40
    self.margin_ver = 30
    
    self.text = "Do you want to quit this game?"
    self.font = pygame.sysfont.Font(None, 32)
    self._prep_window()
    
  def _prep_window(self):
    self.message_window = pygame.Rect(0, 0, self.width, self.height)
    self.message_window.center = self.screen.get_rect().center
    
    self.message = self.font.render(self.text, True, self.settings.message_text_color, self.settings.message_bg_color)
    self.message_rect = self.message.get_rect()
    self.message_rect.top = self.message_window.top + self.margin_ver
    self.message_rect.centerx = self.message_window.centerx
    
    button_width, button_height = 100, 50
    self.yes_button = Button(self.game_run, "Yes", False, False,
                             (self.message_window.left + self.margin_inline, 
                              self.message_window.bottom - button_height - self.margin_ver), 
                             width=button_width, height=button_height)
    self.no_button = Button(self.game_run, "No", False, False, 
                            (self.message_window.right - button_width - self.margin_inline, 
                             self.message_window.bottom - button_height - self.margin_ver), 
                            width=button_width, height=button_height)
    
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.exit_game()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          self.quit_game()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_button_click(mouse_pos)
  
  def _check_button_click(self, mouse_pos):
    '''Checks if button is clicked on'''
    if self.yes_button.rect.collidepoint(mouse_pos):
      self.quit_game()
    elif self.no_button.rect.collidepoint(mouse_pos):
      self.game_run.game_running = True
      
    
  def _upgrade_screen(self):
    '''Shows quit (pause) window on the screen'''
    pygame.draw.rect(self.screen, self.settings.message_bg_color, self.message_window)
    
    self.screen.blit(self.message, self.message_rect)
    
    self.yes_button.draw()
    self.no_button.draw()
import pygame

class Button:
  '''Represents a button in game'''
  def __init__(self, game_run, msg, center=True, pos=(), font_size=24, width=100, height=40):
    self.screen = game_run.screen
    self.settings = game_run.settings
    self.button_color = self.settings.button_color
    self.text_color = (255, 255, 255)
    self.font = pygame.font.SysFont(None, font_size)
    
    self.width, self.height = width, height
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.border_rect = pygame.Rect(0, 0, self.width, self.height)
    
    if center == True:
      self.rect.center = self.screen.get_rect().center
      self.border_rect.center = self.rect.center
    else:
      self.rect.x, self.rect.y = pos
      self.border_rect.x, self.border_rect.y = pos
    
    self._prep_msg(msg)
    
  def _prep_msg(self, msg):
    '''Inserts message (msg) into generated image and centers text on the button'''
    self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
    self.msg_image_rect = self.msg_image.get_rect()
    self.msg_image_rect.center = self.rect.center
    
  def draw(self):
    '''Shows the button on the screen'''
    self.screen.fill(self.button_color, self.rect)
    self.screen.blit(self.msg_image, self.msg_image_rect)
    pygame.draw.rect(self.screen, self.settings.button_border_color, self.border_rect, width=1)
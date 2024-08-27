import pygame
from pygame.sprite import Sprite

class Square(Sprite):
  '''Stores a single square'''
  def __init__(self, tet_game, color_id, pos_x, pos_y):
    super().__init__()
    self.screen = tet_game.screen
    self.settings = tet_game.settings
    self.color_id = color_id
    self.rect = pygame.Rect(0, 0, self.settings.square_width, self.settings.square_height)
    self.border = pygame.Rect(0, 0, self.settings.square_width, self.settings.square_height)
    
    self.rect.x, self.rect.y = pos_x, pos_y
    self.border.x, self.border.y = pos_x, pos_y

  def draw(self):
    '''Draws square on screen'''
    pygame.draw.rect(self.screen, self.settings.tile_colors[self.color_id], self.rect)
    pygame.draw.rect(self.screen, self.settings.board_frame_color, self.border, width=1)
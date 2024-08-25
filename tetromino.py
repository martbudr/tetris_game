import pygame
from random import randint

from square import Square

class Tetromino:
  '''Handles tetrominos (tiles) in the game'''
  def __init__(self, tet_game):
    self.tet_game = tet_game
    self.screen = tet_game.screen
    self.settings = tet_game.settings
    self.board = tet_game.board
    
    self.color = self.settings.tile_colors[str(randint(1, self.settings.tile_colors_amt))]
    self.shape = self.settings.tile_shapes[randint(0, self.settings.tile_shapes_amt-1)]
    rotation = randint(0, 3)
    for i in range(rotation):
      self.shape = self._shape_rotate(self.shape)
      
    self.squares = pygame.sprite.Group()
      
    self._place_tet()
    self._prep_tet()
    
  def _shape_rotate(self, shape):
    '''Rotates shape by 90 degrees'''
    return [list(row)[::-1] for row in zip(*shape)]  
    
  def _place_tet(self):
    '''Places tetromino right above the board'''
    self.pos_x = self.settings.board_margin_x + 8 * self.settings.square_width
    self.pos_y = self.settings.board_margin_y - 4 * self.settings.square_height  
    
  def _prep_tet(self):
    '''Prepares tetromino to be moved and displayed (adds squares to group)'''
    for i in range(len(self.shape)):
      for j in range(len(self.shape[0])):
        if self.shape[i][j] == 1:
          square = Square(self.tet_game, self.color, 
                         self.pos_x + j * self.settings.square_width, 
                         self.pos_y + i * self.settings.square_height)
          self.squares.add(square)  
    
  def draw(self):
    '''Draw tetromino on screen'''
    for square in self.squares:
      square.draw()
    
  def move_down(self):
    '''Moves tetromino down'''
    for square in self.squares:
      square.rect.y += self.settings.square_height
      square.border.y += self.settings.square_height
  
  def move_left(self):
    '''Moves tetromino left'''
    pass
  
  def move_right(self):
    '''Moves tetromino right'''
    pass  
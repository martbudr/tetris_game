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
    
    self.squares = pygame.sprite.Group()
    
    self.color_id = str(randint(1, self.settings.tile_colors_amt))
    self.shape = self.settings.tile_shapes[randint(0, self.settings.tile_shapes_amt-1)]
    rotation = randint(0, 3)
    for i in range(rotation):
      self.shape_rotate()
    
    self.collided_down = False
      
    self._place_tet()
    self._prep_tet()
    
  def shape_rotate(self):
    '''Rotates shape by 90 degrees'''
    self.shape = [list(row)[::-1] for row in zip(*self.shape)]  
    
    if len(self.squares):
      self.squares.empty()
      self._prep_tet()
      
  def move_into_board(self):
    '''Moves the tetromino inside the board if it has fallen outside'''
    max_out = 0
    for square in self.squares:
      square_i, square_j = self.board.get_square_place(square.rect.x, square.rect.y)
      if square_j < 0:
        max_out = min(max_out, square_j)
      elif square_j >= self.settings.grid_columns:
        max_out = max(max_out, square_j-self.settings.grid_columns+1)   
        
    while max_out < 0:
      self._move_squares_right()
      max_out += 1
    while max_out > 0:
      self._move_squares_left()
      max_out -= 1
    
  def _place_tet(self):
    '''Places tetromino right above the board'''
    self.pos_x = self.settings.board_margin_x + 8 * self.settings.square_width
    self.pos_y = self.settings.board_margin_y - 4 * self.settings.square_height  
    
  def _prep_tet(self):
    '''Prepares tetromino to be moved and displayed (adds squares to group)'''
    for i in range(len(self.shape)):
      for j in range(len(self.shape[0])):
        if self.shape[i][j] == 1:
          square = Square(self.tet_game, self.color_id, 
                         self.pos_x + j * self.settings.square_width, 
                         self.pos_y + i * self.settings.square_height)
          self.squares.add(square) 
    
  def draw(self):
    '''Draw tetromino on screen'''
    for square in self.squares:
      square.draw()
    
  def move_down(self):
    '''Moves tetromino down''' 
    if self._check_down_collision():
      self.collided_down = True
      return
       
    self.pos_y += self.settings.square_height
    for square in self.squares:
      square.rect.y += self.settings.square_height
      square.border.y += self.settings.square_height
      
  def move_all_way_down(self):
    '''Moves tetromino down up to a point where there is a collision'''
    while not self.collided_down:
      self.move_down()
  
  def move_left(self):
    '''Moves tetromino left'''
    if self._check_left_collision() or self.collided_down:
      return
    
    self._move_squares_left()
  
  def _move_squares_left(self):
    '''Function to move all squares left'''
    self.pos_x -= self.settings.square_width
    for square in self.squares:
      square.rect.x -= self.settings.square_width
      square.border.x -= self.settings.square_width
  
  def move_right(self):
    '''Moves tetromino right'''
    if self._check_right_collision() or self.collided_down:
      return
    
    self._move_squares_right()
    
  def _move_squares_right(self):
    '''Function to move all squares right'''
    self.pos_x += self.settings.square_width
    for square in self.squares:
      square.rect.x += self.settings.square_width
      square.border.x += self.settings.square_width    
      
  def _check_down_collision(self):
    '''Check if there is a collision of at least one square with bottom border or square below
    If True returned, then there is a collision'''
    for square in self.squares:
      square_i, square_j = self.board.get_square_place(square.rect.x, square.rect.y)
      if square_i == self.settings.grid_rows-1 \
          or (square_i >= -1 and self.board.grid[square_i+1][square_j] != None):
        return True
      
    return False    
  
  def _check_left_collision(self):
    '''Check if there is a collision of at least one square with left border or square
    If True returned, then there is a collision'''
    for square in self.squares:
      square_i, square_j = self.board.get_square_place(square.rect.x, square.rect.y)
      if square_j == 0 \
          or (square_i >= 0 and self.board.grid[square_i][square_j-1] != None):
        return True
      
    return False    
  
  def _check_right_collision(self):
    '''Check if there is a collision of at least one square with right border or square
    If True returned, then there is a collision'''
    for square in self.squares:
      square_i, square_j = self.board.get_square_place(square.rect.x, square.rect.y)
      if square_j == self.settings.grid_columns-1 \
          or (square_i >= 0 and self.board.grid[square_i][square_j+1] != None):
        return True
      
    return False 
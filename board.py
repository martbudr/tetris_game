import pygame

class Board:
  def __init__(self, tet_game):
    '''Init the board'''
    self.screen = tet_game.screen
    self.settings = tet_game.settings
    self.grid = [[None for j in range(self.settings.grid_columns)] for i in range(self.settings.grid_rows)] # access: first row, then column
    
    self.border_left = self.settings.board_margin_x
    self.border_right = self.settings.board_margin_x + self.settings.grid_columns * self.settings.square_width
    self.border_top = self.settings.board_margin_y
    self.border_bottom = self.settings.board_margin_y + self.settings.grid_rows * self.settings.square_height
    
  def draw(self):
    '''Draw board on screen'''
    # iterate: first down, then right
    for i in range(self.settings.grid_rows):
      for j in range(self.settings.grid_columns):
        pos_x, pos_y = self._get_square_pos(i, j)
        
        if self.grid[i][j] != None:
          self.fill_square(pos_x, pos_y, self.settings.tile_colors[self.grid[i][j]])
          
        self.draw_square_border(pos_x, pos_y)
        
  def fill_square(self, pos_x, pos_y, color):
    '''Visually fills square with color'''
    rect = pygame.Rect(0, 0, self.settings.square_width, self.settings.square_height)
    rect.x, rect.y = pos_x, pos_y
    pygame.draw.rect(self.screen, color, rect)
        
  def draw_square_border(self, pos_x, pos_y):
    '''Draws border around a square'''
    frame = pygame.Rect(0, 0, self.settings.square_width, self.settings.square_height)
    frame.x, frame.y = pos_x, pos_y
    pygame.draw.rect(self.screen, self.settings.board_frame_color, frame, width=1)
    
  def _get_square_pos(self, i, j):
    '''Returns position of a square on the screen as a (pos_x, pos_y)'''  
    pos_x = self.settings.board_margin_x + j * self.settings.square_width
    pos_y = self.settings.board_margin_y + i * self.settings.square_height
    return pos_x, pos_y
    
  def get_square_place(self, pos_x, pos_y):
    '''Returns place of square on the board as a (i, j) position'''
    j = int((pos_x - self.settings.board_margin_x) / self.settings.square_width)
    i = int((pos_y - self.settings.board_margin_y) / self.settings.square_height)
    return i, j
  
  def place_tetromino(self, tetromino):
    '''Places tetromino on the board'''
    for square in tetromino.squares:
      square_i, square_j = self.get_square_place(square.rect.x, square.rect.y)
      self.grid[square_i][square_j] = tetromino.color_id
import pygame

class Board:
  def __init__(self, tet_game):
    '''Init the board'''
    self.screen = tet_game.screen
    self.settings = tet_game.settings
    self.grid = [[None for j in range(self.settings.grid_columns)] for i in range(self.settings.grid_rows)] # access: first row, then column
    
  def draw(self):
    '''Draw board on screen'''
    # iterate: first down, then right
    for i in range(self.settings.grid_rows):
      for j in range(self.settings.grid_columns):
        pos_x = self.settings.board_margin_x + j * self.settings.square_width
        pos_y = self.settings.board_margin_y + i * self.settings.square_height
        
        if self.grid[i][j] != None:
          self.fill_square(pos_x, pos_y, self.settings.colors[self.grid[i][j]])
          
        self.draw_square_border(pos_x, pos_y)
        
  def fill_square(self, pos_x, pos_y, color):
    '''Fills square with color'''
    rect = pygame.Rect(0, 0, self.settings.square_width, self.settings.square_height)
    rect.x, rect.y = pos_x, pos_y
    pygame.draw.rect(self.screen, color, rect)
        
  def draw_square_border(self, pos_x, pos_y):
    '''Draws border around a square'''
    frame = pygame.Rect(0, 0, self.settings.square_width, self.settings.square_height)
    frame.x, frame.y = pos_x, pos_y
    pygame.draw.rect(self.screen, self.settings.board_frame_color, frame, width=1)
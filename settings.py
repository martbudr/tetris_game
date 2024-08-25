class Settings:
  '''Przechowuje ustawienia dot. gry'''
  def __init__(self):
    self.screen_width, self.screen_height = 1200, 750
    self.bg_color = (130, 130, 130)
    
    # Board settings
    self.grid_rows, self.grid_columns = 30, 20
    self.board_margin_x, self.board_margin_y = 300, 100
    self.square_width = self.square_height = 20
    self.board_frame_color = (255, 255, 255)
    
    # Tetromino settings
    self.tile_colors = {
      '1': (10, 10, 10),
    }
    self.tile_colors_amt = len(self.tile_colors)
    self.tile_shapes = [
      [[1, 1, 1, 1],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]],
      [[1, 1, 1],
       [1, 0, 0],
       [0, 0, 0]],
      [[1, 1, 1],
       [0, 1, 0],
       [0, 0, 0]],
      [[1, 1, 1],
       [0, 0, 1],
       [0, 0, 0]],
      [[1, 1, 0],
       [0, 1, 1],
       [0, 0, 0]],
      [[0, 1, 1],
       [1, 1, 0],
       [0, 0, 0]],
      [[1, 1],
       [1, 1]]
    ]
    self.tile_shapes_amt = len(self.tile_shapes)
class Settings:
  '''Przechowuje ustawienia dot. gry'''
  def __init__(self):
    self.screen_width, self.screen_height = 1200, 750
    self.bg_color = (255, 204, 211)
    
    # Board settings
    self.grid_rows, self.grid_columns = 22, 14
    self.board_margin_x, self.board_margin_y = 300, 150
    self.square_width = self.square_height = 26
    self.board_frame_color = (255, 255, 255)
    
    # Score settings
    self.square_score = 20
    
    # Tetromino settings
    self.tile_colors = {
      '1': (10, 10, 10),
      '2': (50, 50, 50),
      '3': (100, 100, 100),
      '4': (150, 150, 150)
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
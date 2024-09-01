import pygame
import sys

from board import Board
from tetromino import Tetromino
from game_stats import GameStats
from scoreboard import Scoreboard

class Tetris:
  def __init__(self, game_run):
    '''Initialisation of the game'''
    self.game_run = game_run
    self.settings = game_run.settings
    self.screen = game_run.screen
    
    self.stats = GameStats()
    self.sb = Scoreboard(self)
    self.board = Board(self)
    
    self.time_elapsed_since_last_movedown = 0
    
    self.game_not_over = True
    self.tile_falling = False # a variable to check if there is a generated tetromino falling at the moment (so that if there isn't, a new one can be generated)
  
  def run_game(self):
    '''Single instance of game loop'''
    self._check_events()
    
    if self.game_run.game_running:
      if not self.tile_falling:
        self.tetromino = Tetromino(self)
        self.tile_falling = True
      
      self._move_tetromino_down()
        
      if self.tetromino.collided_down:
        self._handle_tetromino_down()
      
    self._upgrade_screen()
    
    self.time_elapsed_since_last_movedown += self.game_run.FPS
    
  def show_window(self):
    '''Show window (outside this class)'''
    self._upgrade_screen()
    
  def _check_events(self):
    '''Checks for user input'''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.trigger_game_over()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
        
  def _check_keydown_events(self, event):
    '''Checks keydown events and triggers appropriate responses'''
    if event.key == pygame.K_q: 
      self._pause_game()
    elif self.game_run.game_running:
      if event.key == pygame.K_LEFT:
        self.tetromino.move_left()
      elif event.key == pygame.K_RIGHT:
        self.tetromino.move_right()
      elif event.key == pygame.K_UP:
        self.tetromino.shape_rotate()
        self.tetromino.move_into_board()
      elif event.key == pygame.K_SPACE:
        self.tetromino.move_all_way_down()
    
  def _pause_game(self):
    '''Puts the game on hold'''
    self.game_run.game_running = False
    self.game_run.game_quit = True  
      
  def trigger_game_over(self):
    '''Reaction on game end'''
    self.game_run.game_running = False
    self.game_run.game_over = True
    self.stats.save_high_score()
  
  def _move_tetromino_down(self):
    '''Moves tetromino down if sufficient time has passed'''
    if self.time_elapsed_since_last_movedown > 3000 and not self.tetromino.collided_down:
      self.tetromino.move_down()
      self.time_elapsed_since_last_movedown = 0
  
  def _handle_tetromino_down(self):
    '''Reaction when the tetromino hits something (bottom border or another tetromino)'''
    if not self._check_place_possible():
      self.trigger_game_over()
    else:
      self.board.place_tetromino(self.tetromino)
      self._remove_full_rows()
      
      self.tile_falling = False
  
  def _check_place_possible(self):
    '''Checks if it is possible to place tetromino in its current place'''
    for square in self.tetromino.squares:
      square_i, square_j = self.board.get_square_place(square.rect.x, square.rect.y)
      if square_i < 0:
        return False
    return True
  
  def _remove_full_rows(self):
    '''Removes full rows from the board'''
    full_row_numbers = self._get_full_rows()
    for row_num in full_row_numbers:
      self.board.delete_row(row_num)
      self.stats.score += self.settings.grid_columns * self.settings.square_score
    self.sb.prep_score()
    self.sb.check_high_score()
    
  def _get_full_rows(self):
    '''Returns full rows (checks only those where the new tetromino fell)'''
    row_numbers = set()
    for square in self.tetromino.squares:
      square_i, square_j = self.board.get_square_place(square.rect.x, square.rect.y)
      if square_i not in row_numbers and self._check_one_row(square_i):
        row_numbers.add(square_i)
    return row_numbers
  
  def _check_one_row(self, row_number):
    '''Checks one row - if it is full or not'''
    for j in range(self.settings.grid_columns):
      if self.board.grid[row_number][j] == None:
        return False
    return True
  
  def _upgrade_screen(self):
    '''Draws items on screen on every iteration of the game loop'''        
    self.sb.show_scores()
    
    self.board.draw()
    self.tetromino.draw()
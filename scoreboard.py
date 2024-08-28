import pygame.font

class Scoreboard:
  '''Class dedicated to displaying score information on the screen'''
  def __init__(self, tet_game):
    self.screen = tet_game.screen
    self.settings = tet_game.settings
    self.stats = tet_game.stats
    
    self.text_color = (50, 50, 50)
    self.font = pygame.font.SysFont(None, 48)
    
    self.prep_score()
    
  def prep_score(self):
    '''Prepares score to be displayed on the screen'''
    self.score_image = self.font.render(str(self.stats.score), True, self.text_color, self.settings.bg_color)
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen.get_rect().right - 300
    self.score_rect.top = self.settings.board_margin_y
  
  def show_score(self):
    '''Displays score on the screen'''
    self.screen.blit(self.score_image, self.score_rect)
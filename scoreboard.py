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
    self._prep_high_score()
    
  def prep_score(self):
    '''Prepares score to be displayed on the screen'''
    text = f"Score: {self.stats.score}"
    self.score_image = self.font.render(text, True, self.text_color, self.settings.bg_color)
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen.get_rect().right - 100
    self.score_rect.top = self.settings.board_margin_y
    
  def _prep_high_score(self):
    '''Prepares high score to be displayed on the screen'''
    text = f"High score: {self.stats.high_score}"
    self.high_score_image = self.font.render(text, True, self.text_color, self.settings.bg_color)
    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.right = self.screen.get_rect().right - 100
    self.high_score_rect.top = self.score_rect.bottom + 30
  
  def show_scores(self):
    '''Displays score on the screen'''
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    
  def check_high_score(self):
    if self.stats.score <= self.stats.high_score:
      return
    
    self.stats.high_score = self.stats.score
    self._prep_high_score()
import sys

class Window:
  def __init__(self, game_run):
    self.game_run = game_run
    self.screen = game_run.screen
    self.settings = game_run.settings
    
  def show_window(self):
    '''Displays window on the screen'''
    self._check_events()
    if self.game_run.game_exists:
      self.game_run.tet_game.show_window()
    self._upgrade_screen()
    
  def exit_game(self):
    '''Exits entire game''' 
    self.game_run.tet_game.trigger_game_over()
    sys.exit() 
    
  def quit_game(self):
    '''Quits current game that is being played'''
    self.game_run.tet_game.stats.save_high_score()
    self.game_run.init_running()
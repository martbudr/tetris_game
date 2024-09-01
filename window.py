import sys

class Window:
  def __init__(self, game_run):
    self.tet_game = game_run.tet_game
    self.screen = game_run.screen
    self.settings = game_run.settings
    
  def show_window(self):
    self._check_events()
    self._upgrade_screen()
    
  def quit_game(self):
    self.tet_game.trigger_game_over()
    sys.exit()
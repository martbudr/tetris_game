from pathlib import Path
from os.path import exists

class GameStats:
  def __init__(self):
    self.score = 0
    self._read_high_score()
    
  def _read_high_score(self):
    self.high_score_path = Path('high_score.txt')
    self.high_score = 0
    if exists(self.high_score_path):
      self.high_score = int(self.high_score_path.read_text().splitlines()[0].strip())
    
  def save_high_score(self):
    '''Zapisuje najlepszy wynik w pliku'''
    self.high_score_path.write_text(str(self.high_score)) 
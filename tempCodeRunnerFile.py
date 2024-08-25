
        self.tile_falling = True
      
      self._upgrade_screen()
      self.clock.tick(60)
  
  def _check_events(self):
    '''Checks for user input'''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
        
  def _check_keydown_events(self, event):
    '''Checks keydown events and triggers appropriate responses'''
    if event.key == pygame.K_q:
      sys.exit()
  
  def _upgrade_screen(self):
    '''Draws items on screen on every iteration of the game loop'''
    self.screen.fill(self.settings.bg_color)
    
    self.board.draw()
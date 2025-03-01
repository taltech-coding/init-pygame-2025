# TODO: If self.lives is equal to zero or less than zero (<=), then
#       set self.state to STATE_GAME_OVER and clear self.fruits.
if self.lives <= 0:
    self.state = STATE_GAME_OVER
    self.fruits.clear()
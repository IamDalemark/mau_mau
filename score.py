import PySimpleGUI as sg
class Player:
  def __init__(self, player_count) -> int:
    self.player_count = player_count
    self.score = 0
    
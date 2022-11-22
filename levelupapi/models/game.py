from django.db import models
from .gamer import Gamer
from .game_type import GameType

class Game(models.Model):
  
  title = models.CharField(max_length=50)
  maker = models.CharField(max_length=50)
  number_of_players = models.IntegerField(max_length=50)
  skill_level = models.IntegerField(max_length=50)
  game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
  gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)

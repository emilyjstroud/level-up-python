from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game
from levelupapi.models import GameType
from levelupapi.models import Gamer

class GameView(ViewSet):
  
  def retrieve(self, request, pk):
    game = Game.objects.get(pk=pk)
    
    game_type = request.query_params.get('type', None)
    if game_type is not None:
      games = games.filter(game_type_id=game_type)
    
    serializer = GameSerializer(game)
    return Response(serializer.data)
  
  def list(self, request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST operations

    Returns
        Response -- JSON serialized game instance
    """
    gamer = Gamer.objects.get(uid=request.data["user_id"])
    game_type = GameType.objects.get(pk=request.data["game_type"])

    game = Game.objects.create(
        title=request.data["title"],
        maker=request.data["maker"],
        number_of_players=request.data["number_of_players"],
        skill_level=request.data["skill_level"],
        gamer=gamer,
        game_type=game_type
    )
    serializer = GameSerializer(game)
    return Response(serializer.data)
  
class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ('id', 'title', 'maker', 'number_of_players', 'skill_level', 'game_type', 'gamer')

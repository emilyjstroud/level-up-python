from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models import Game

class EventView(ViewSet):
  def retrieve(self, request, pk):
    event = Event.objects.get(pk=pk)
    serializer = EventSerializer(event)
    return Response(serializer.data)
    
    
  def list(self, request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    
    game = Game.objects.get(pk=request.data["game"])
    
    event = Event.objects.create(
        description=request.data["description"],
        date=request.data["date"],
        time=request.data["time"],
        game=game
    )
    serializer = EventSerializer(event)
    return Response(serializer.data)
    
  
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time')

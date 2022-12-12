from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models import Game
from rest_framework.decorators import action
from levelupapi.models import Gamer
from levelupapi.models import EventGamer

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
    
  def update(self, request, pk):
    event = Event.objects.get(pk=pk)
    event.description = request.data["description"]
    event.date = request.data["date"]
    event.time = request.data["time"]
    
    game = Game.objects.get(pk=request.data["game"])
    game = game
    event.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  @action(methods=['post'], detail=True)
  def signup(self, request, pk):
      """Post request for a user to sign up for an event"""

      gamer = Gamer.objects.get(user=request.data["user_id"])
      event = Event.objects.get(pk=pk)
      attendee = EventGamer.objects.create(
          gamer=gamer,
          event=event
      )
      return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
  @action(methods=['delete'], detail=True)
  def leave(self,request, pk):
    
      gamer = Gamer.objects.get(user=request.data["user_id"])
      event = Event.objects.get(pk=pk)
      attendee = EventGamer.objects.remove(
        gamer=gamer,
        event=event
      )
      return Response({'message': 'Gamer removed'}, status=status.HTTP_204_NO_CONTENT)  
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'game', 'organizer',
          'description', 'date', 'time',
          'joined')

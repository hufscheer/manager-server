from rest_framework import serializers
from game.domain import GameTeamPlayer

class GameTeamPlayerGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeamPlayer
        fields = ('id', 'name', 'description')
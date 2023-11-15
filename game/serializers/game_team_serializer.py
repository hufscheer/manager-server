from rest_framework import serializers
from game.domain import GameTeam

class GameTeamSaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeam
        fields = '__all__'

class GameTeamRequestSerializer(serializers.Serializer):
    teamIds = serializers.ListField(child=serializers.IntegerField(), source='team_ids')
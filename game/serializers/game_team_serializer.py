from rest_framework import serializers
from game.domain import GameTeam, GameTeamPlayer

class GameTeamSaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeam
        fields = '__all__'

class GameTeamRequestSerializer(serializers.Serializer):
    teamIds = serializers.ListField(child=serializers.IntegerField(), source='team_ids')

class GameTeamPlayerRequestSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeamPlayer
        fields = ('name', 'description',)

class GameTeamPlayerSaveSerialzier(serializers.ModelSerializer):

    class Meta:
        model = GameTeamPlayer
        fields = '__all__'
from rest_framework import serializers
from game.domain import GameTeamPlayer, GameTeam

class GameTeamPlayerGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameTeamPlayer
        fields = ('id', 'name', 'description')

class GameTeamInfoSerializer(serializers.ModelSerializer):
    gameTeamId = serializers.IntegerField(source='id')
    gameTeamName = serializers.CharField(source='team.name')
    logoImageUrl = serializers.CharField(source='team.logo_image_url')
    score = serializers.IntegerField()

    class Meta:
        model = GameTeam
        fields = ('gameTeamId', 'gameTeamName', 'logoImageUrl', 'score')
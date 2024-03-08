from rest_framework import serializers
from game.domain import LineupPlayer, GameTeam

class LineupPlayerGetSerializer(serializers.ModelSerializer):
    isCaptain = serializers.BooleanField(source='is_captain')
    
    class Meta:
        model = LineupPlayer
        fields = ('id', 'name', 'description', 'number', 'isCaptain')

class GameTeamInfoSerializer(serializers.ModelSerializer):
    gameTeamId = serializers.IntegerField(source='id')
    gameTeamName = serializers.CharField(source='league_team.name')
    logoImageUrl = serializers.CharField(source='league_team.logo_image_url')
    score = serializers.IntegerField()

    class Meta:
        model = GameTeam
        fields = ('gameTeamId', 'gameTeamName', 'logoImageUrl', 'score')
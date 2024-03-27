from rest_framework import serializers
from game.domain import LineupPlayer, GameTeam

class LineupPlayerGetSerializer(serializers.ModelSerializer):
    isCaptain = serializers.BooleanField(source='is_captain')
    leagueTeamPlayerId = serializers.IntegerField(source='league_team_player_id')

    class Meta:
        model = LineupPlayer
        fields = ('id', 'name', 'description', 'number', 'isCaptain', 'leagueTeamPlayerId')

class LineupPlayerNameNumberGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = LineupPlayer
        fields = ('id', 'name', 'number')

class GameTeamInfoSerializer(serializers.ModelSerializer):
    gameTeamId = serializers.IntegerField(source='id')
    gameTeamName = serializers.CharField(source='league_team.name')
    logoImageUrl = serializers.CharField(source='league_team.logo_image_url')
    score = serializers.IntegerField()

    class Meta:
        model = GameTeam
        fields = ('gameTeamId', 'gameTeamName', 'logoImageUrl', 'score')

class GameTeamNameInfoSerializer(serializers.ModelSerializer):
    gameTeamId = serializers.IntegerField(source='id')
    gameTeamName = serializers.CharField(source='league_team.name')
    
    class Meta:
        model = GameTeam
        fields = ('gameTeamId', 'gameTeamName')
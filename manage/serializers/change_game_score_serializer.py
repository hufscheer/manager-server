from rest_framework import serializers
from manage.models import Game, Record

class GameInfoGetSerializer(serializers.ModelSerializer):
    team1Score = serializers.IntegerField(source='first_team_score')
    team2Score = serializers.IntegerField(source='second_team_score')

    class Meta:
        model = Game
        fields = ('name', 'team1Score', 'team2Score')

class GameScoreChangePostSerializer(serializers.ModelSerializer):
    playerName = serializers.CharField(source='player_name')
    scoredAt = serializers.DateTimeField(source='scored_at')

    class Meta:
        model = Record
        fields = ('playerName', 'team', 'scoredAt', 'score', 'game')


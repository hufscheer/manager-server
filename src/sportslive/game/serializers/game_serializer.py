from rest_framework import serializers

from game.domain import Game
from sport.domain import Sport

class GameRequestSerializer(serializers.ModelSerializer):
    sportsId = serializers.IntegerField(source='sport_id')
    startTime = serializers.DateTimeField(source='start_time')
    videoId = serializers.CharField(allow_null=True, required=False, source='video_id')
    teamIds = serializers.ListField(child=serializers.IntegerField(), source='team_ids')

    class Meta:
        model = Game
        fields = ('sportsId', 'startTime', 'name', 'videoId', 'teamIds')

class GameSaveSerializer(serializers.ModelSerializer):
    video_id = serializers.CharField(allow_null=True, required=False)
    
    class Meta:
        model = Game
        fields = '__all__'

class GameChangeSerializer(GameRequestSerializer):
    gameQuarter = serializers.CharField(source='game_quarter')
    gameName = serializers.CharField(source='name')

    class Meta:
        model = Game
        fields = ('sportsId', 'startTime', 'gameName', 'videoId', 'gameQuarter', 'state',)

class _SportsInfoSerializer(serializers.ModelSerializer):
    sportsId = serializers.IntegerField(source='id')
    sportsName = serializers.CharField(source='name')

    class Meta:
        model = Sport
        fields = ('sportsId', 'sportsName')

class GameInfoResponseSerializer(serializers.ModelSerializer):
    sports = _SportsInfoSerializer(source='sport')
    startTime = serializers.DateTimeField(source='start_time')
    gameName = serializers.CharField(source='name')
    videoId = serializers.CharField(source='video_id')
    gameQuarter = serializers.CharField(source='game_quarter')

    class Meta:
        model = Game
        fields = ('sports', 'startTime', 'gameName', 'state', 'videoId', 'gameQuarter', 'state')
from rest_framework import serializers

from game.domain import Game

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

class GameChangeRequestSerializer(GameRequestSerializer):
    gameQuarter = serializers.CharField(source='game_quarter')
    
    class Meta:
        model = Game
        fields = ('sportsId', 'startTime', 'name', 'videoId', 'gameQuarter', 'state',)

class GameExtraInfoResponseSerializer(serializers.Serializer):
    sportName = serializers.CharField(source='sport_name')
    state = serializers.CharField()
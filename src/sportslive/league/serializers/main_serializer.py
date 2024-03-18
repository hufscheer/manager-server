from rest_framework import serializers
from league.domain import League
from game.domain import Game

class _MainGameInfoSerializer(serializers.ModelSerializer):
    startTime = serializers.DateTimeField(source='start_time')

    class Meta:
        model = Game
        fields = ('id', 'startTime', 'name', 'round',)

class MainListGetSerializer(serializers.ModelSerializer):
    leagueName = serializers.CharField(source='name')
    playingGameData = _MainGameInfoSerializer(many=True, source='playing_game_datas')

    class Meta:
        model = League
        fields = ('leagueName', 'playingGameData',)
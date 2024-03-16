from rest_framework import serializers
from league.domain import League
from sport.domain import Sport

class _SportDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sport
        fields = ('id', 'name')

class _LeagueGetSerializer(serializers.ModelSerializer):
    leagueId = serializers.IntegerField(source='id')
    startAt = serializers.DateTimeField(source='start_at')
    endAt = serializers.DateTimeField(source='end_at')
    inProgressRound = serializers.IntegerField(source='in_progress_round')
    maxRound = serializers.IntegerField(source='max_round')
    sportData = _SportDataSerializer(source='sport_datas', many=True)

    class Meta:
        model = League
        fields = ('leagueId' ,'name', 'startAt', 'endAt', 'inProgressRound', 'maxRound', 'sportData')

class LeagueListGetSerializer(serializers.Serializer):
    playing = _LeagueGetSerializer(many=True)
    scheduled = _LeagueGetSerializer(many=True)
    finished = _LeagueGetSerializer(many=True)
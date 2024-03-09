from rest_framework import serializers
from league.domain import League

class LeagueGetSerializer(serializers.ModelSerializer):
    leagueId = serializers.IntegerField(source='id')
    startAt = serializers.DateTimeField(source='start_at')
    endAt = serializers.DateTimeField(source='end_at')
    inProgressRound = serializers.IntegerField(source='in_progress_round')
    maxRound = serializers.IntegerField(source='max_round')

    class Meta:
        model = League
        fields = ('leagueId' ,'name', 'startAt', 'endAt', 'inProgressRound', 'maxRound')
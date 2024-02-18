from rest_framework import serializers
from league.domain import League

class LeagueGetSerializer(serializers.ModelSerializer):
    leagueId = serializers.IntegerField(source='id')
    startAt = serializers.DateTimeField(source='start_at')
    endAt = serializers.DateTimeField(source='end_at')

    class Meta:
        model = League
        fields = ('leagueId' ,'name', 'startAt', 'endAt')

class AllLeagueGetSerializer(serializers.Serializer):
    leagues = LeagueGetSerializer(many=True)
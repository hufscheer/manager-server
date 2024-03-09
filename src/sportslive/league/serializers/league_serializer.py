from rest_framework import serializers
from league.domain import League

class _LeagueRegistrationSerializer(serializers.ModelSerializer):
    startAt = serializers.DateTimeField(source='start_at')
    endAt = serializers.DateTimeField(source='end_at')
    maxRound = serializers.IntegerField(source='max_round')

    class Meta:
        model = League
        fields = ('name', 'startAt', 'endAt', 'maxRound')

class LeagueSportRegistrationSerializer(serializers.Serializer):
    leagueData = _LeagueRegistrationSerializer(source='league_data')
    sportData = serializers.ListField(child=serializers.IntegerField(), source='sport_data')

class _LeagueChangeSerializer(_LeagueRegistrationSerializer):
    inProgressRound = serializers.IntegerField(source='in_progress_round')

    class Meta:
        model = League
        fields = ('name', 'startAt', 'endAt', 'maxRound', 'inProgressRound')

class LeagueSportChangeSerializer(serializers.Serializer):
    leagueData = _LeagueChangeSerializer(source='league_data')
    sportData = serializers.ListField(child=serializers.IntegerField(), source='sport_data')
    leagueId = serializers.IntegerField(source='league_id')
    
class LeagueDeleteSerializer(serializers.Serializer):
    leagueId = serializers.IntegerField(source='league_id')

class LeagueRegisterResponseSerializer(serializers.Serializer):
    leagueId = serializers.IntegerField(source='league_id')
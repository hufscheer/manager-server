from rest_framework import serializers
from league.domain import League

class LeagueRegistrationSerializer(serializers.ModelSerializer):
    startAt = serializers.DateTimeField(source='start_at')
    endAt = serializers.DateTimeField(source='end_at')
    maxRound = serializers.IntegerField(source='max_round')
    inProgressRound = serializers.IntegerField(source='in_progress_round')

    class Meta:
        model = League
        fields = ('name', 'startAt', 'endAt', 'maxRound', 'inProgressRound')

class LeagueSportRegistrationSerializer(serializers.Serializer):
    leagueData = LeagueRegistrationSerializer(source='league_data')
    sportData = serializers.ListField(child=serializers.IntegerField(), source='sport_data')


class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = ('manager', 'organization', 'name', 'start_at', 'end_at', 'max_round', 'in_progress_round')

class LeagueSportChangeSerializer(LeagueSportRegistrationSerializer):
    leagueId = serializers.IntegerField(source='league_id')
    
class LeagueDeleteSerializer(serializers.Serializer):
    leagueId = serializers.IntegerField(source='league_id')

class LeagueRegisterResponseSerializer(serializers.Serializer):
    leagueId = serializers.IntegerField(source='league_id')
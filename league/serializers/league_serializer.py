from rest_framework import serializers
from league.domain import League

class LeagueRegistrationSerializer(serializers.ModelSerializer):
    startAt = serializers.DateTimeField(source='start_at')
    endAt = serializers.DateTimeField(source='end_at')
    class Meta:
        model = League
        fields = ('name', 'startAt', 'endAt')

class LeagueSportRegistrationSerializer(serializers.Serializer):
    leagueData = LeagueRegistrationSerializer(source='league_data')
    sportData = serializers.ListField(child=serializers.IntegerField(), source='sport_data')


class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = ('administrator', 'organization', 'name', 'start_at', 'end_at')

class LeagueSportChangeSerializer(LeagueSportRegistrationSerializer):
    leagueId = serializers.IntegerField(source='league_id')
    
class LeagueDeleteSerializer(serializers.Serializer):
    leagueId = serializers.IntegerField(source='league_id')

class LeagueRegisterResponseSerializer(serializers.Serializer):
    leagueId = serializers.IntegerField(source='league_id')
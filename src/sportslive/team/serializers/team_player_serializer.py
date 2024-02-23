from rest_framework import serializers
from team.domain import LeagueTeamPlayer

class TeamPlayerRegisterRequestSerializer(serializers.ModelSerializer):
    description = serializers.CharField(allow_null=True, allow_blank=True, required=False)

    class Meta:
        model = LeagueTeamPlayer
        fields = ('name', 'description', 'number')

class TeamPlayerChangeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeagueTeamPlayer
        fields = ('name', 'description', 'number')

class TeamPlayersResponseSerialier(serializers.ModelSerializer):

    class Meta:
        model = LeagueTeamPlayer
        fields = ('id', 'name', 'description', 'number')
from rest_framework import serializers
from team.domain import LeagueTeamPlayer

class TeamPlayerRegisterRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeagueTeamPlayer
        fields = ('name', 'description')

class TeamPlayerChangeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeagueTeamPlayer
        fields = ('name', 'description')

class TeamPlayersResponseSerialier(serializers.ModelSerializer):

    class Meta:
        model = LeagueTeamPlayer
        fields = ('id', 'name', 'description')
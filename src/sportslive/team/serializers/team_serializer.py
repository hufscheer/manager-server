from rest_framework import serializers
from team.domain import LeagueTeam

class TeamRegisterRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    logo = serializers.ImageField()
    
class TeamSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeagueTeam
        fields = '__all__'

class TeamChangeRequestSerializer(TeamRegisterRequestSerializer):
    name = serializers.ListField(child=serializers.CharField())
    logo = serializers.ListField(child=serializers.ImageField())
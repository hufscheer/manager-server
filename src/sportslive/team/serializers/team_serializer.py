from rest_framework import serializers
from team.domain import LeagueTeam

class TeamRegisterRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    logo = serializers.ImageField()
    
class TeamSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeagueTeam
        fields = '__all__'

class TeamChangeRequestSerializer(serializers.Serializer):
    name = serializers.ListField(child=serializers.CharField(), required=False)
    logo = serializers.ListField(child=serializers.ImageField(), required=False)

class TeamRegisterResponseSerializer(serializers.Serializer):
    teamIds = serializers.ListField(child=serializers.IntegerField(), source='team_ids')
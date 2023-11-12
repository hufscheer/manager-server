from rest_framework import serializers
from team.domain import Team

class TeamRegisterRequestSerializer(serializers.Serializer):
    names = serializers.ListField(child=serializers.CharField())
    logos = serializers.ListField(child=serializers.ImageField())
    
class TeamSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

class TeamChangeRequestSerializer(TeamRegisterRequestSerializer):
    pass
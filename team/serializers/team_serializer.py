from rest_framework import serializers
from team.domain import Team

class TeamRegisterRequestSerializer(serializers.Serializer):
    name = serializers.ListField(child=serializers.CharField())
    logo = serializers.ListField(child=serializers.ImageField(), source='logo')
    
class TeamSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

class TeamChangeRequestSerializer(TeamRegisterRequestSerializer):
    pass
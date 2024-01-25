from rest_framework import serializers
from team.domain import LeagueTeam

class TeamGetSerializer(serializers.ModelSerializer):
    logoImageUrl = serializers.CharField(source='logo_image_url')

    class Meta:
        model = LeagueTeam
        fields = ('id', 'name', 'logoImageUrl')
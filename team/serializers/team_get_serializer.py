from rest_framework import serializers
from team.domain import Team

class TeamGetSerializer(serializers.ModelSerializer):
    logoImageUrl = serializers.CharField(source='logo_image_url')

    class Meta:
        model = Team
        fields = ('id', 'name', 'logoImageUrl')
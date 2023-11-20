from rest_framework import serializers
from team.domain import TeamPlayer

class TeamPlayerRegisterRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamPlayer
        fields = ('name', 'description')

class TeamPlayerChangeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamPlayer
        fields = ('name', 'description')
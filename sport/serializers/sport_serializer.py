from rest_framework import serializers
from sport.domain import Sport

class SportsNameResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sport
        fields = ('name',)
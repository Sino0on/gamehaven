from rest_framework import serializers
from game.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Application

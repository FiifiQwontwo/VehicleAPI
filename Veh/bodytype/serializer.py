from .models import BodyType
from rest_framework import serializers


class ListBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ('id', 'body_type', 'picture', 'description')

from .models import VehicleModel
from rest_framework import serializers


class ModelListSerializer(serializers.ModelSerializer):
    make_name = serializers.CharField(source='make_name.make_name')

    class Meta:
        model = VehicleModel
        fields = "__all__"
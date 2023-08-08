from .models import VehicleModel
from rest_framework import serializers


class ModelListSerializer(serializers.ModelSerializer):
    make = serializers.CharField(source='make.make_name')


    class Meta:
        model = VehicleModel
        fields = "__all__"
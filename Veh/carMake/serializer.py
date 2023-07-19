from rest_framework import serializers
from .models import VehicleMake


class ListVehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleMake
        fields = ('make_name', 'logo')


class CreateVehicleSerializers(serializers.ModelSerializer):
    logo = serializers.FileField()

    class Meta:
        model = VehicleMake
        fields = ('make_name', 'logo')

    def save(self):
        new_vehicle = VehicleMake(
            make_name=self.validated_data['make_name'],
            logo=self.validated_data['logo'],
            # data=validated_data['data'],
        )
        new_vehicle.save()
        return new_vehicle

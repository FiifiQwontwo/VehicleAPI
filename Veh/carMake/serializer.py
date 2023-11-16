from rest_framework import serializers
from .models import VehicleMake
from vehModels.serializer import ModelListSerializer


class ListVehicleSerializers(serializers.ModelSerializer):
    models = ModelListSerializer(many=True, read_only=True)

    class Meta:
        model = VehicleMake
        fields = ('id', 'make_name',  'logo', 'is_car', 'is_motor', 'is_tractor','models')


class VehicleMakeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMake
        fields = ('id', 'make_name', 'logo', 'is_car', 'is_motor', 'is_tractor')


class UpdateVehicleSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(required=False)

    class Meta:
        model = VehicleMake
        fields = '__all__'

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class CreateVehicleSerializers(serializers.ModelSerializer):
    logo = serializers.FileField()

    class Meta:
        model = VehicleMake
        fields = ('make_name', 'logo', 'is_car', 'is_motor', 'is_tractor')

    def generate_filename(self, make_name, image_extension):
        filename = f"{make_name.replace(' ', '_').lower()}.{image_extension}"
        return filename

    def save(self, **kwargs):
        make_name = self.validated_data.get('make_name')
        logo = self.validated_data.get('logo')
        is_car = self.validated_data.get('is_car')
        is_motor = self.validated_data.get('is_motor')
        is_tractor = self.validated_data.get('is_tractor')

        if make_name and logo:
            image_extension = logo.name.split('.')[-1]
            filename = self.generate_filename(make_name, image_extension)
            logo.name = filename

            new_vehicle = VehicleMake(
                make_name=make_name,
                logo=logo,
                is_car=is_car,
                is_tractor=is_tractor,
                is_motor=is_motor,
            )
            new_vehicle.save()
            return new_vehicle


